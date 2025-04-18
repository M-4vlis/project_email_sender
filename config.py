import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', '16')) * 1024 * 1024
    
    # Lista de extensões permitidas
    ALLOWED_EXTENSIONS = {'xls', 'xlsx', 'csv', 'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'gif'}
    
    # Configurações de email padrão
    DEFAULT_PROVIDERS = {
        'gmail': {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'use_tls': True
        },
        'outlook': {
            'smtp_server': 'smtp-mail.outlook.com',
            'smtp_port': 587,
            'use_tls': True
        },
        'office365': {
            'smtp_server': 'smtp.office365.com',
            'smtp_port': 587,
            'use_tls': True
        },
        'yahoo': {
            'smtp_server': 'smtp.mail.yahoo.com',
            'smtp_port': 587,
            'use_tls': True
        },
        'custom': {
            'smtp_server': '',
            'smtp_port': 587,
            'use_tls': True
        }
    }