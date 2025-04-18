from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
import json
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from config import Config
from utils.email_utils import test_smtp_connection, read_emails_from_excel, send_email
import time

# Carrega as variáveis de ambiente
load_dotenv()

# Cria a instância do Flask
app = Flask(__name__)
app.config.from_object(Config)

# Verifica se a pasta de uploads existe, se não, cria
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Função para verificar se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Rota principal
@app.route('/')
def index():
    return render_template('index.html', providers=app.config['DEFAULT_PROVIDERS'])

# Rota para testar conexão com servidor de email
@app.route('/test_connection', methods=['POST'])
def test_connection():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    smtp_server = data.get('smtp_server')
    smtp_port = int(data.get('smtp_port'))
    
    success, message = test_smtp_connection(email, password, smtp_server, smtp_port)
    
    return jsonify({
        'success': success,
        'error': message if not success else None
    })

# Rota para enviar emails
@app.route('/send_emails', methods=['POST'])
def send_emails():
    try:
        # Dados do formulário
        email_provider = request.form.get('email_provider')
        smtp_server = request.form.get('smtp_server')
        smtp_port = int(request.form.get('smtp_port'))
        sender_email = request.form.get('email')
        password = request.form.get('password')
        subject = request.form.get('subject')
        body = request.form.get('body')
        cc = request.form.get('cc')
        
        # Processa arquivo Excel
        excel_file = request.files.get('excel_file')
        if not excel_file or not allowed_file(excel_file.filename):
            flash('Arquivo Excel inválido!', 'danger')
            return redirect(url_for('index'))
        
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(excel_file.filename))
        excel_file.save(excel_path)
        
        # Processa anexos
        attachments = request.files.getlist('attachments')
        attachment_paths = []
        
        for attachment in attachments:
            if attachment and allowed_file(attachment.filename):
                filename = secure_filename(attachment.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                attachment.save(path)
                attachment_paths.append(path)
        
        # Lê emails do Excel
        email_list = read_emails_from_excel(excel_path)
        
        if not email_list:
            flash('Nenhum email válido encontrado no arquivo!', 'danger')
            return redirect(url_for('index'))
        
        # Envia emails
        success_count = 0
        fail_count = 0
        
        for recipient in email_list:
            success, message = send_email(
                sender_email, password, smtp_server, smtp_port,
                recipient, subject, body, cc, attachment_paths
            )
            
            if success:
                success_count += 1
            else:
                fail_count += 1
            
            # Pequena pausa entre envios para evitar bloqueios
            time.sleep(1)
        
        # Limpa arquivos temporários
        os.remove(excel_path)
        for path in attachment_paths:
            os.remove(path)
        
        flash(f'Envio concluído! Sucesso: {success_count}, Falhas: {fail_count}', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        flash(f'Erro ao processar envio: {str(e)}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)