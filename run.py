from app import app
import os

if __name__ == '__main__':
    # Garante que a pasta de uploads existe
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Executa a aplicação
    app.run(host='0.0.0.0', port=5000, debug=True)