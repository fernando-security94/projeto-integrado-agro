"""
main.py — Gerenciamento de Configuração com Git/GitHub
=======================================================
Disciplina : Projeto de Software
Unidade    : U4 — Projeto de Software Avançado
Aula       : A1 — Gerenciamento de Configuração

Demonstra o fluxo completo de SCM (Software Configuration Management):
  1. Clone     → obter artefatos do repositório remoto
  2. Trabalho  → modificar e criar artefatos localmente
  3. Status    → verificar o que mudou
  4. Add       → mover alterações para staging area
  5. Commit    → salvar snapshot com mensagem descritiva
  6. Push      → publicar no repositório remoto (GitHub)
  7. Verificação → confirmar estado final do repositório remoto

Execute com:
    python main.py
"""

from config      import SEP
from repositorio import (
    clonar_repositorio,
    verificar_status,
    adicionar_staging,
    realizar_commit,
    publicar_push,
    exibir_log,
    exibir_repositorio_remoto,
)
from artefatos import (
    modificar_artefato,
    criar_artefato,
    exibir_artefatos_locais,
)


def cabecalho() -> None:
    print(SEP)
    print("  GERENCIAMENTO DE CONFIGURAÇÃO — Git & GitHub")
    print("  Disciplina: Projeto de Software | U4 — A1")
    print(SEP)


def secao(titulo: str) -> None:
    print(f"\n{'#' * 60}")
    print(f"  {titulo}")
    print(f"{'#' * 60}")


def main() -> None:
    cabecalho()

    # ------------------------------------------------------------------
    # ETAPA 1 — Clonar repositório remoto
    # ------------------------------------------------------------------
    secao("ETAPA 1 — Clone do repositório remoto")
    artefatos_locais = clonar_repositorio()

    # ------------------------------------------------------------------
    # ETAPA 2 — Exibir estado inicial dos artefatos locais
    # ------------------------------------------------------------------
    secao("ETAPA 2 — Artefatos obtidos (estado inicial local)")
    exibir_artefatos_locais(artefatos_locais)

    # ------------------------------------------------------------------
    # ETAPA 3 — Trabalho local: modificar e criar artefatos
    # ------------------------------------------------------------------
    secao("ETAPA 3 — Trabalho local (modificações e novas funcionalidades)")

    print(f"\n{SEP}")
    print("  Modificando artefatos existentes...")
    print(SEP)
    modificar_artefato(artefatos_locais, "app.py",   "def autenticar_usuario(cpf, senha): pass")
    modificar_artefato(artefatos_locais, "utils.py", "def formatar_data(data): return data.strftime('%d/%m/%Y')")

    print(f"\n{SEP}")
    print("  Criando novos artefatos...")
    print(SEP)
    criar_artefato(
        artefatos_locais,
        "relatorio.py",
        "def gerar_relatorio_mensal(dados):\n    \"\"\"Gera relatório consolidado por mês.\"\"\"\n    pass",
    )
    criar_artefato(
        artefatos_locais,
        "testes.py",
        "import unittest\n\nclass TestApp(unittest.TestCase):\n    def test_autenticar(self):\n        self.assertTrue(True)",
    )

    # ------------------------------------------------------------------
    # ETAPA 4 — git status
    # ------------------------------------------------------------------
    secao("ETAPA 4 — Verificação de status (git status)")
    resultado_status = verificar_status(artefatos_locais)

    todos_alterados = resultado_status["modificados"] + resultado_status["novos"]

    # ------------------------------------------------------------------
    # ETAPA 5 — git add
    # ------------------------------------------------------------------
    secao("ETAPA 5 — Staging area (git add .)")
    adicionar_staging(todos_alterados)

    # ------------------------------------------------------------------
    # ETAPA 6 — git commit
    # ------------------------------------------------------------------
    secao("ETAPA 6 — Commit das alterações (git commit)")
    hash_commit = realizar_commit(
        "feat: autenticacao, formatacao de data, relatorio mensal e testes unitarios",
        artefatos_locais,
    )

    # ------------------------------------------------------------------
    # ETAPA 7 — git push
    # ------------------------------------------------------------------
    secao("ETAPA 7 — Publicação no repositório remoto (git push)")
    publicar_push(artefatos_locais, hash_commit)

    # ------------------------------------------------------------------
    # ETAPA 8 — Histórico de commits
    # ------------------------------------------------------------------
    secao("ETAPA 8 — Histórico de commits (git log)")
    exibir_log()

    # ------------------------------------------------------------------
    # ETAPA 9 — Verificação final no repositório remoto
    # ------------------------------------------------------------------
    secao("ETAPA 9 — Estado final do repositório remoto (GitHub)")
    exibir_repositorio_remoto()

    print(f"\n{SEP}")
    print("  Fluxo SCM concluído com sucesso!")
    print(f"{SEP}\n")


if __name__ == "__main__":
    main()