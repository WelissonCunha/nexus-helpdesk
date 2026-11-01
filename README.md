
# 🚀 Nexus HelpDesk

**Sistema inteligente de gerenciamento de chamados de suporte técnico (Help Desk).**

O **Nexus HelpDesk** é uma plataforma SaaS (Software as a Service) desenvolvida para facilitar o gerenciamento de solicitações de suporte técnico, centralizando atendimentos, organizando equipes e proporcionando maior controle sobre os chamados.

A proposta é oferecer uma solução moderna, intuitiva e escalável, permitindo que diferentes empresas utilizem a mesma plataforma de forma independente e segura.

---

## 🎯 Objetivo do projeto

Desenvolver uma plataforma de Help Desk multiempresa (Multi-Tenant), permitindo que pequenas e médias empresas gerenciem seus próprios ambientes de suporte técnico sem compartilhar informações entre organizações.

O sistema busca simplificar a abertura, distribuição, acompanhamento e resolução de chamados, melhorando a comunicação entre usuários e equipes de TI.

## ✨ Funcionalidades

### 🏢 Gestão de organizações
- Cadastro e gerenciamento de empresas.
- Ambientes independentes para cada organização.
- Controle de usuários vinculados às organizações.
- Isolamento de dados entre empresas (Multi-Tenant).

### 🎫 Gerenciamento de chamados
- Abertura de chamados de suporte.
- Identificação de prioridades.
- Acompanhamento de status.
- Atribuição de chamados aos técnicos.
- Histórico de interações e comentários.
- Controle do ciclo de atendimento.

### 👥 Gestão de usuários e permissões
- Administradores.
- Técnicos de suporte.
- Solicitantes.
- Controle de acesso baseado em funções (RBAC).

### 📊 Dashboard
- Visão geral dos chamados.
- Indicadores de atendimento.
- Chamados abertos, em andamento e concluídos.
- Acompanhamento da produtividade da equipe.

> **Nota:** As funcionalidades acima representam o escopo planejado do projeto. A implementação está em desenvolvimento.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.12+ | Linguagem principal |
| Django 5.2 LTS | Framework backend |
| Bootstrap 5 | Interface e responsividade |
| PostgreSQL 16 | Banco de dados |
| Docker | Containerização |
| Gunicorn | Servidor de aplicação |
| Git e GitHub | Versionamento de código |

---

## 🏗️ Arquitetura do projeto

O Nexus HelpDesk está sendo desenvolvido com uma arquitetura modular, separando as principais responsabilidades do sistema.

```text
nexus-helpdesk/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── organizations/
│   ├── tickets/
│   └── dashboard/
│
├── templates/
│
├── static/
│
├── requirements.txt
├── .env
├── docker-compose.yml
├── manage.py
└── README.md
```

### Organização dos módulos

- **organizations:** gerenciamento de empresas, usuários vinculados e permissões.
- **tickets:** gerenciamento dos chamados e interações.
- **dashboard:** indicadores e visualização geral do suporte.
- **config:** configurações centrais do Django.

---

## ⚙️ Instalação e execução

### Pré-requisitos

- Python 3.12 ou superior.
- Git.
- Docker Desktop.
- PostgreSQL 16 (via Docker).

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/nexus-helpdesk.git

cd nexus-helpdesk
```

### 2. Criar ambiente virtual

```powershell
python -m venv venv
```

### 3. Ativar o ambiente virtual (Windows)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\venv\Scripts\Activate.ps1
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar o banco de dados

Iniciar os serviços definidos no Docker Compose:

```bash
docker compose up -d
```

O ambiente PostgreSQL utiliza as seguintes configurações previstas:

| Configuração | Valor |
|---|---|
| Imagem | postgres:16 |
| Banco | nexus_db |
| Usuário | nexus_user |
| Porta | 5432 |

### 6. Executar as migrações

```bash
python manage.py makemigrations

python manage.py migrate
```

### 7. Criar usuário administrador

```bash
python manage.py createsuperuser
```

### 8. Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Segurança

A segurança é um dos pilares do desenvolvimento do Nexus HelpDesk.

Entre as práticas previstas estão:

- Autenticação de usuários.
- Controle de acesso baseado em funções (RBAC).
- Isolamento de dados entre organizações.
- Proteção contra acessos não autorizados.
- Armazenamento seguro de credenciais.
- Gerenciamento de sessões.
- Proteção contra vulnerabilidades comuns em aplicações web.
- Boas práticas de desenvolvimento com Django.

---

## 🗺️ Roadmap de desenvolvimento

- [x] Inicialização do projeto Django.
- [x] Configuração da estrutura modular.
- [x] Criação do aplicativo Organizations.
- [x] Criação do aplicativo Tickets.
- [x] Criação do aplicativo Dashboard.
- [x] Verificação inicial do projeto Django.
- [ ] Configuração e integração com PostgreSQL.
- [ ] Implementação da autenticação.
- [ ] Implementação do isolamento multiempresa.
- [ ] Desenvolvimento do gerenciamento de chamados.
- [ ] Implementação dos níveis de acesso.
- [ ] Desenvolvimento do dashboard.
- [ ] Implementação do sistema de comentários.
- [ ] Testes automatizados.
- [ ] Containerização completa.
- [ ] Deploy em ambiente de produção.

---

## 💡 Visão do produto

O Nexus HelpDesk nasce com a proposta de transformar o atendimento de suporte técnico em um processo mais organizado, transparente e eficiente.

Mais do que um sistema para registrar problemas, a plataforma pretende conectar empresas, usuários e equipes de TI em um único ambiente de gerenciamento.

**Nexus HelpDesk: conectando pessoas, organizando soluções.**

---

## 📌 Status do projeto

<em>Em desenvolvimento 🚧</em>

Projeto desenvolvido como iniciativa independente, com foco em desenvolvimento web, arquitetura SaaS, gerenciamento de serviços de TI e segurança da informação.

---

**Nexus HelpDesk © 2026**  
*Todos os direitos reservados.*
