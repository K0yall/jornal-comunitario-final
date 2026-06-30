# Infraestrutura de Automação para Jornal Comunitário 📰

Este repositório contém o projeto de uma API REST voltada para a gestão de notícias de um Jornal Comunitário, integrada a um fluxo de automação DevOps com pipeline de Integração Contínua (CI). Trabalho desenvolvido para a disciplina de Cloud Computing do Curso de Bacharelado em Sistemas de Informação - UNIDAVI.

## 🎓 Identificação e Autoria

* **Instituição:** Centro Universitário para o Desenvolvimento do Alto Vale do Itajaí (UNIDAVI)
* **Curso:** Bacharelado em Sistemas de Informação
* **Disciplina:** Cloud Computing
* **Professor:** Prof. Esp. Ademar Perfoll Junior
* **Acadêmico:** Lucas Gilmar da Silva
* **Data de Entrega:** 30 de junho de 2026

---
## 📂 Estrutura de Diretórios do Projeto

```text
repositorio-trabalho-final/
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuração do pipeline de CI (GitHub Actions)
├── api/
│   ├── data/
│   │   └── noticias.json   # Banco de dados simulado (10+ registros)
│   ├── tests/
│   │   └── test_api.py     # Suite com 4 testes unitários automatizados
│   └── app.py              # Código-fonte principal da API Flask
└── requirements.txt        # Gerenciador de dependências do projeto
```
---
## 🛠️ Tecnologias Utilizadas

* **Python 3.10** - Linguagem de programação base.
* **Flask 3.0.3** - Micro-framework para exposição das rotas RESTful.
* **Pytest 8.2.2** - Framework para automação e execução dos testes unitários.
* **Flake8 7.1.0** - Linter utilizado para análise estática e garantia dos padrões PEP 8.
* **GitHub Actions** - Plataforma de CI/CD para orquestração da esteira automatizada.

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de possuir o **Python 3.10+** instalado em sua máquina de desenvolvimento.

### Passo a Passo

1. **Instale as dependências obrigatórias:**
   ```bash
   pip install -r requirements.txt

No Windows (PowerShell): $env:PYTHONPATH="api"
No Linux / macOS: export PYTHONPATH=$PYTHONPATH:$(pwd)/api

Inicie o servidor da API: python api/app.py (http://localhost:5000)

## 🧪 Como Executar os Testes Unitários Localmente
Para rodar a suíte contendo os 4 testes unitários criados (retorno 200, validação do JSON, erro 404 e o teste de integridade de versão de autoria própria), utilize o comando:
pytest api/tests/
