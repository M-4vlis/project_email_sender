// Configurações padrão dos provedores de email
const emailProviders = {
    gmail: {
        smtp_server: 'smtp.gmail.com',
        smtp_port: 587
    },
    outlook: {
        smtp_server: 'smtp-mail.outlook.com',
        smtp_port: 587
    },
    office365: {
        smtp_server: 'smtp.office365.com',
        smtp_port: 587
    },
    yahoo: {
        smtp_server: 'smtp.mail.yahoo.com',
        smtp_port: 587
    },
    custom: {
        smtp_server: '',
        smtp_port: 587
    }
};

// Função para atualizar configurações SMTP quando mudar o provedor
function updateConfig() {
    const provider = document.getElementById('emailProvider').value;
    const smtpServerInput = document.getElementById('smtpServer');
    const smtpPortInput = document.getElementById('smtpPort');
    const customConfigDiv = document.getElementById('customConfig');
    const loginInstructions = document.getElementById('loginInstructions');
    const instructionsText = document.getElementById('instructionsText');

    const config = emailProviders[provider];
    smtpServerInput.value = config.smtp_server;
    smtpPortInput.value = config.smtp_port;

    // Mostrar ou esconder a área de configuração customizada
    if (provider === 'custom') {
        smtpServerInput.removeAttribute('readonly');
        smtpPortInput.removeAttribute('readonly');
        customConfigDiv.style.display = 'block';
    } else {
        smtpServerInput.setAttribute('readonly', 'readonly');
        smtpPortInput.setAttribute('readonly', 'readonly');
        customConfigDiv.style.display = 'none';
    }

    // Mostrar instruções baseadas no provedor
    switch (provider) {
        case 'gmail':
            loginInstructions.style.display = 'block';
            instructionsText.textContent = "📧 Gmail: Ative o 'Acesso a apps menos seguros' ou crie uma senha de app.";
            break;
        case 'outlook':
        case 'office365':
            loginInstructions.style.display = 'block';
            instructionsText.textContent = "📧 Outlook/Office365: Verifique se o acesso SMTP está habilitado na sua conta.";
            break;
        case 'yahoo':
            loginInstructions.style.display = 'block';
            instructionsText.textContent = "📧 Yahoo: Ative o acesso SMTP e gere uma senha de aplicativo nas configurações.";
            break;
        case 'custom':
            loginInstructions.style.display = 'none';
            instructionsText.textContent = '';
            break;
        default:
            loginInstructions.style.display = 'none';
            instructionsText.textContent = '';
    }
}

// Função para testar conexão com o servidor de email
function testConnection() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const smtpServer = document.getElementById('smtpServer').value;
    const smtpPort = document.getElementById('smtpPort').value;
    const connectionStatus = document.getElementById('connectionStatus');

    if (!email || !password || !smtpServer || !smtpPort) {
        connectionStatus.textContent = '⚠️ Preencha todos os campos de conexão!';
        connectionStatus.className = 'text-warning';
        return;
    }

    connectionStatus.textContent = '⌛ Testando conexão...';
    connectionStatus.className = 'text-info';

    fetch('/test_connection', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, smtp_server: smtpServer, smtp_port: smtpPort })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                connectionStatus.textContent = '✅ Conexão estabelecida com sucesso!';
                connectionStatus.className = 'text-success';
            } else {
                connectionStatus.textContent = `❌ Erro: ${data.error}`;
                connectionStatus.className = 'text-danger';
            }
        })
        .catch(error => {
            connectionStatus.textContent = '❌ Erro ao testar conexão!';
            connectionStatus.className = 'text-danger';
        });
}

// Função para mostrar progresso de envio
function showProgress(show, current = 0, total = 0) {
    const progressContainer = document.getElementById('progressContainer');
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');

    if (show) {
        progressContainer.style.display = 'block';
        const percentage = (current / total) * 100;
        progressBar.style.width = `${percentage}%`;
        progressText.textContent = `Enviados: ${current} de ${total}`;
    } else {
        progressContainer.style.display = 'none';
    }
}

// Configuração inicial quando a página carregar
document.addEventListener('DOMContentLoaded', function () {
    updateConfig();

    const excelInput = document.getElementById('excelFile');
    const attachmentsInput = document.getElementById('attachments');

    excelInput.addEventListener('change', function () {
        if (this.files.length > 0 && this.files[0].size > 16 * 1024 * 1024) {
            alert('O arquivo Excel é muito grande! O tamanho máximo é 16MB.');
            this.value = '';
        }
    });

    attachmentsInput.addEventListener('change', function () {
        let totalSize = 0;
        for (let i = 0; i < this.files.length; i++) {
            totalSize += this.files[i].size;
        }
        if (totalSize > 16 * 1024 * 1024) {
            alert('O tamanho total dos anexos é muito grande! O máximo permitido é 16MB.');
            this.value = '';
        }
    });
});

const body = document.body;
const darkBtn = document.getElementById('toggleDarkMode');
const darkIcon = document.getElementById('darkModeIcon');

// Verifica o estado do Modo Escuro ao carregar
if (localStorage.getItem('darkMode') === 'enabled') {
    body.classList.add('dark-mode');
    darkIcon.classList.replace('fa-moon', 'fa-sun');
}

// Alterna o Modo Escuro ao clicar no botão
darkBtn.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    const isDark = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark ? 'enabled' : 'disabled');
    darkIcon.classList.toggle('fa-moon');
    darkIcon.classList.toggle('fa-sun');
});
