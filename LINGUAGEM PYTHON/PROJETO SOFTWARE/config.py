"""
config.py — Configurações Centralizadas
========================================
Disciplina : Projeto de Software
Unidade    : U4 — Projeto de Software Avançado
Aula       : A1 — Gerenciamento de Configuração

Centraliza constantes e parâmetros usados pelos demais módulos,
facilitando manutenção e evitando "magic strings" espalhados no código.
"""

# ---------------------------------------------------------------------------
# Dados do repositório simulado
# ---------------------------------------------------------------------------
REPO_NOME    = "projeto2025_SCM"
REPO_URL     = "https://github.com/usuario/projeto2025_SCM.git"
BRANCH_PADRAO = "main"

# ---------------------------------------------------------------------------
# Artefatos que compõem o projeto (simulação local)
# ---------------------------------------------------------------------------
ARTEFATOS_INICIAIS = [
    {"nome": "README.md",      "conteudo": "# projeto2025_SCM\nProjeto de Software 2025"},
    {"nome": "app.py",         "conteudo": "# Módulo principal da aplicação\nprint('Iniciando app...')"},
    {"nome": "utils.py",       "conteudo": "# Funções utilitárias compartilhadas"},
    {"nome": "config.json",    "conteudo": '{"versao": "1.0.0", "debug": false}'},
]

# ---------------------------------------------------------------------------
# Mensagens de log
# ---------------------------------------------------------------------------
SEP = "=" * 60
SEP_MENOR = "-" * 40
