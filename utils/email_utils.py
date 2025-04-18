import smtplib
import pandas as pd
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError

def test_smtp_connection(email, password, smtp_server, smtp_port):
    """
    Testa a conexão com o servidor SMTP
    Retorna: (sucesso: bool, mensagem: str)
    """
    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.ehlo()  # Identificação com o servidor
        server.starttls()  # Inicia criptografia TLS
        server.login(email, password)
        server.quit()
        return True, "Conexão estabelecida com sucesso!"
    except smtplib.SMTPAuthenticationError:
        return False, "Erro de autenticação: verifique seu email e senha."
    except smtplib.SMTPConnectError:
        return False, "Erro ao conectar ao servidor: verifique o endereço e porta."
    except Exception as e:
        return False, f"Erro: {str(e)}"

def read_emails_from_excel(file_path):
    """
    Lê endereços de email de um arquivo Excel/CSV
    Retorna: lista de emails válidos
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        # Tenta encontrar a coluna com emails
        email_column = None
        for col in df.columns:
            if 'email' in col.lower() or '@' in str(df[col].iloc[0]):
                email_column = col
                break
        
        if email_column is None:
            raise ValueError("Nenhuma coluna de email encontrada!")
        
        # Extrai e valida emails
        emails = []
        for email in df[email_column].tolist():
            try:
                valid = validate_email(str(email))
                emails.append(valid.email)
            except EmailNotValidError:
                continue
        
        return emails
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo: {str(e)}")

def create_message(sender_email, recipient_email, subject, body, cc=None, attachments=None):
    """
    Cria um objeto de mensagem de email com anexos
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    if cc:
        msg['Cc'] = cc
    
    # Adiciona o corpo do email
    msg.attach(MIMEText(body, 'plain'))
    
    # Adiciona anexos
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                    msg.attach(part)
    
    return msg

def send_email(sender_email, password, smtp_server, smtp_port, recipient_email, subject, body, cc=None, attachments=None):
    """
    Envia um email individual
    Retorna: (sucesso: bool, mensagem: str)
    """
    try:
        msg = create_message(sender_email, recipient_email, subject, body, cc, attachments)
        
        with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.login(sender_email, password)
            recipients = [recipient_email]
            if cc:
                recipients.append(cc)
            server.send_message(msg, from_addr=sender_email, to_addrs=recipients)
        
        return True, "Email enviado com sucesso!"
    except Exception as e:
        return False, f"Erro ao enviar email: {str(e)}"