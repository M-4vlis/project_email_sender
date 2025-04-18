
# Aplicação de Envio de E-mails em Massa

Este projeto nasceu da necessidade de automatizar o envio de e-mails para **centenas de fornecedores** com solicitações de cotação. No trabalho, minha equipe enfrentava uma tarefa repetitiva, demorada e propensa a erros humanos.

A ideia foi criar uma aplicação web intuitiva que **permite enviar e-mails personalizados em massa** usando um arquivo Excel como base. E o melhor: deixei ela mais robusta para que **qualquer pessoa** consiga usar, mesmo sem conhecimento técnico. É só preencher os campos, subir os arquivos e *puf*, e-mail enviado! 🚀

---

## Visão Geral

- Interface web simples e intuitiva  
- Suporte a diferentes provedores de e-mail (Gmail, Outlook, Yahoo, etc.)  
- Possibilidade de configurar servidor SMTP personalizado  
- Suporte a anexos e campo CC  
- Barra de progresso e feedback visual em tempo real  
- Tema escuro 💻🌙  

---

## Tecnologias Utilizadas

| Camada                    | Tecnologias |
|---------------------------|-------------|
| **Frontend**              | `HTML`, `CSS`, `JavaScript`, `jQuery` |
| **Backend**               | `Python`, `Flask` |
| **Envio de E-mails**      | `Flask-Mail` |
| **Estilização e UI**      | `Bootstrap` (layout responsivo), `Font Awesome` (ícones) |
| **Banco de Dados**        | Não utilizado. Dados manipulados em memória durante o envio |

---

## Como Usar

### 1. 📁 Clone o repositório

```bash
git clone https://github.com/seu-usuario/email-mass-sender.git
cd email-mass-sender
```

### 2. 📦 Crie o ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. ▶️ Inicie o servidor Flask

```bash
flask run
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## Como Funciona

1. Escolha o provedor de e-mail ou configure manualmente  
2. Preencha seu e-mail e senha (use senha de aplicativo, se necessário)  
3. Faça o upload de um arquivo Excel contendo os e-mails dos destinatários  
4. Preencha o assunto, corpo do e-mail e, se quiser, adicione anexos  
5. Clique em **Enviar Emails** e veja a mágica acontecer ✨  

---

## Formato Esperado do Arquivo Excel

| Email               | Nome (opcional) |
|---------------------|-----------------|
| fornecedor@teste.com | Fornecedor A    |
| exemplo@teste.com    | Fornecedor B    |

---

## Funcionalidades Extras

| Recurso                        | Descrição |
|-------------------------------|-----------|
| 🌑 **Modo Escuro**            | Ativável com um clique. Seu olho agradece. |
| 🔌 **Teste de Conexão SMTP**  | Verifica se sua conta está funcionando antes de disparar tudo |
| 📎 **Upload de Anexos**       | Suporta `.jpg`, `.png`, `.gif`, `.pdf`, `.xlsx`, `.docx`, entre outros |
| 📤 **Barra de Progresso**     | Veja em tempo real o andamento dos envios |

---

## Por que usar essa aplicação?

Porque ninguém merece ficar copiando e colando e-mails o dia inteiro.  
Automatizar é viver melhor. Mais produtividade, menos estresse, mais tempo pro café! ☕

---

## Contribuindo

Se quiser contribuir, fique à vontade!  
Sugestões, melhorias, bugs ou ideias malucas são sempre bem-vindas! 😄

---

## Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para usar, modificar e compartilhar!

---

Feito com 💡, café ☕ e umas boas horas de código por [Mario](https://github.com/M-4vlis)