"""
artefatos.py — Modificação e Criação de Artefatos Locais
=========================================================
Disciplina : Projeto de Software
Unidade    : U4 — Projeto de Software Avançado
Aula       : A1 — Gerenciamento de Configuração

Responsável por simular o trabalho do desenvolvedor na máquina local:
  - modificar artefatos existentes (clonados do repositório remoto)
  - criar novos artefatos (funcionalidades implementadas pelo time)
"""

import datetime
from config import SEP


def modificar_artefato(artefatos_locais: dict[str, str], nome: str, nova_linha: str) -> None:
    """
    Simula a edição de um arquivo já existente no computador local.
    Acrescenta nova_linha ao conteúdo do artefato informado.
    """
    if nome not in artefatos_locais:
        print(f"  [AVISO] Artefato '{nome}' não encontrado localmente.")
        return

    ts = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    artefatos_locais[nome] += f"\n# Alterado em {ts}\n{nova_linha}"

    print(f"  ✏  Artefato modificado  → {nome}")
    print(f"     Conteúdo adicionado  : \"{nova_linha}\"")


def criar_artefato(artefatos_locais: dict[str, str], nome: str, conteudo: str) -> None:
    """
    Simula a criação de um novo arquivo no computador local
    (nova funcionalidade desenvolvida pelo membro do time).
    """
    ts = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    artefatos_locais[nome] = f"# Criado em {ts}\n{conteudo}"

    print(f"  ✚  Novo artefato criado → {nome}")


def exibir_artefatos_locais(artefatos_locais: dict[str, str]) -> None:
    """Exibe o conteúdo completo de todos os artefatos presentes no computador local."""
    print(f"\n{SEP}")
    print("  Artefatos no computador local:")
    print(SEP)

    for nome, conteudo in artefatos_locais.items():
        print(f"\n  📄 {nome}")
        print("  " + "-" * 40)
        for linha in conteudo.splitlines():
            print(f"    {linha}")