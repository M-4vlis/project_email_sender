# Email Sender: Envio de E-mails em Massa

A Email Sender é uma aplicação web desenvolvida para automatizar o envio de e-mails em massa, ideal para pessoas ou equipes que realizam tarefas repetitivas de envio de e-mails para múltiplos destinatários, como no caso de solicitação de cotações para fornecedores.

Com ela, você pode enviar e-mails personalizados para centenas de contatos em um processo simples, rápido e eficiente, poupando horas de trabalho manual.


## Funcionalidades

- Envio de e-mails personalizados em massa: Envie e-mails de forma automatizada para diversos destinatários a partir de uma lista de e-mails.

- Integração com diversos provedores de e-mail: Gmail, Outlook, Yahoo e configuração personalizada com qualquer provedor SMTP.

- Modo Escuro: Para tornar a interface mais agradável em ambientes com pouca luz.

- Testar Conexão: Verifique se a configuração do servidor SMTP está correta antes de iniciar o envio.

- Upload de Lista de Contatos (Excel): Faça upload de um arquivo Excel (.xlsx, .xls, .csv) com os e-mails dos destinatários.

- Anexos e Cópia (CC): Envie arquivos em anexo e inclua destinatários em cópia.

- Feedback e Progresso: Receba informações em tempo real sobre o progresso do envio de e-mails.


## Tecnologias Usadas

    Frontend: HTML, CSS, JavaScript (com jQuery para algumas interações)

    Backend: Python (Flask)

    Banco de Dados: Não utilizado (o armazenamento de dados é feito em memória durante o envio)

    Outras Bibliotecas:

        Bootstrap (para layout responsivo)

        Font Awesome (para ícones)

        Flask-Mail (para o envio de e-mails)


## Como Rodar o Projeto

Pré-requisitos

1. Python 3.x: Caso ainda não tenha o Python instalado, baixe e instale a versão mais recente aqui.

2. Bibliotecas do Python: O projeto utiliza algumas bibliotecas que precisam ser instaladas. Para isso, basta rodar o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

3. Arquivo Excel com os E-mails: Prepare um arquivo com os e-mails dos destinatários, em um formato .xlsx, .xls ou .csv.


## Passo a Passo para Executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/email-sender.git
cd email-sender
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação Flask:
```bash
python app.py
```

4. Abra o navegador e acesse o endereço:
```bash
    http://localhost:5000
```


## Como Usar

1. Configuração Inicial

    Seleção do Provedor de E-mail: Escolha o provedor de e-mail que você usará (ex: Gmail, Outlook, Yahoo). Se não estiver usando um dos provedores pré-configurados, escolha a opção "Custom" e insira manualmente as configurações do seu servidor SMTP.

    Autenticação: Insira seu e-mail e senha. Lembre-se de usar senhas de app para provedores como Gmail, caso tenha autenticação de dois fatores ativada.

2. Enviar E-mail em Massa

    Arquivo Excel: Faça upload de um arquivo Excel com os e-mails dos destinatários.

    Assunto e Corpo: Preencha o assunto e o corpo do e-mail. O corpo do e-mail pode incluir formatação HTML se necessário.

    Anexos: Faça upload de arquivos que deseja enviar junto com o e-mail (opcional).

    Email em Cópia (CC): Se necessário, adicione um e-mail para ser colocado em cópia (CC).

3. Testar Conexão

Antes de enviar os e-mails, você pode testar a conexão com o servidor SMTP para garantir que as configurações estão corretas. Clique no botão "Testar Conexão" e aguarde a confirmação.

4. Enviar E-mails

Após configurar tudo, clique no botão "Enviar Emails" para iniciar o processo de envio. Durante o envio, você verá um indicador de progresso para acompanhar o status.


## Modo Escuro

A aplicação possui um modo escuro que pode ser ativado clicando no ícone de lua no canto superior direito. O modo escuro melhora a experiência visual em ambientes com pouca luz.


## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, enviar pull requests e compartilhar melhorias!


## Licença

Este projeto é de código aberto e distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.


## Observações Finais

Caso esteja enfrentando problemas com o envio de e-mails, verifique as configurações do seu provedor de e-mail e se a autenticação de dois fatores está ativada.

Lembre-se de garantir que os arquivos Excel com os e-mails estejam formatados corretamente para evitar problemas no processamento.