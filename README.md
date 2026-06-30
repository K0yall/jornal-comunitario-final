# Infraestrutura de Automação para Jornal Comunitário 📰

Este repositório contém o projeto de uma API REST voltada para a gestão de notícias de um Jornal Comunitário, integrada a um fluxo de automação DevOps com pipeline de Integração Contínua (CI). Trabalho desenvolvido para a disciplina de Cloud Computing do Curso de Bacharelado em Sistemas de Informação - UNIDAVI.

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
