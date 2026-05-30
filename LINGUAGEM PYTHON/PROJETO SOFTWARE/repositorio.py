"""
repositorio.py — Simulação do Repositório Git/GitHub
======================================================
Disciplina : Projeto de Software
Unidade    : U4 — Projeto de Software Avançado
Aula       : A1 — Gerenciamento de Configuração

Simula as operações essenciais do Git:
  - clone   → obter artefatos do repositório remoto
  - status  → verificar itens alterados/novos
  - add     → mover para staging area
  - commit  → salvar snapshot com mensagem
  - push    → publicar no repositório remoto
"""

import os
import datetime
from config import REPO_NOME, REPO_URL, BRANCH_PADRAO, ARTEFATOS_INICIAIS, SEP, SEP_MENOR


# ---------------------------------------------------------------------------
# Estado interno (simula o repositório em memória)
# ---------------------------------------------------------------------------
_repositorio = {
    "nome"    : REPO_NOME,
    "url"     : REPO_URL,
    "branch"  : BRANCH_PADRAO,
    "artefatos": {},        # nome → conteúdo (versão remota "confirmada")
    "staging"  : [],        # arquivos prontos para commit
    "log_commits": [],      # histórico de commits
}


def clonar_repositorio() -> dict[str, str]:
    """
    Simula 'git clone <url>'.
    Retorna dicionário com os artefatos baixados para o computador local.
    """
    print(f"\n{SEP}")
    print(f"  git clone {_repositorio['url']}")
    print(SEP)
    print(f"  Clonando em '{_repositorio['nome']}'...")

    # Popula o repositório remoto simulado com os artefatos iniciais
    for item in ARTEFATOS_INICIAIS:
        _repositorio["artefatos"][item["nome"]] = item["conteudo"]

    for nome in _repositorio["artefatos"]:
        print(f"  remote: recebendo '{nome}' ... OK")

    total = len(_repositorio["artefatos"])
    print(f"\n  Receiving objects: 100% ({total}/{total}), done.")
    print(f"  Resolving deltas: 100%, done.")

    return dict(_repositorio["artefatos"])   # cópia local


def verificar_status(artefatos_locais: dict[str, str]) -> dict[str, list[str]]:
    """
    Simula 'git status'.
    Compara o estado local com o remoto e retorna listas de modificados e novos.
    """
    print(f"\n{SEP}")
    print(f"  git status")
    print(SEP)
    print(f"  On branch {_repositorio['branch']}")

    modificados = []
    novos       = []

    for nome, conteudo in artefatos_locais.items():
        if nome not in _repositorio["artefatos"]:
            novos.append(nome)
        elif conteudo != _repositorio["artefatos"][nome]:
            modificados.append(nome)

    if not modificados and not novos:
        print("  nothing to commit, working tree clean")
    else:
        if modificados:
            print("\n  Changes not staged for commit:")
            for m in modificados:
                print(f"    modified:   {m}")
        if novos:
            print("\n  Untracked files:")
            for n in novos:
                print(f"    {n}")

    return {"modificados": modificados, "novos": novos}


def adicionar_staging(artefatos: list[str]) -> None:
    """
    Simula 'git add .'
    Move os artefatos para a staging area.
    """
    print(f"\n{SEP}")
    print(f"  git add .")
    print(SEP)

    _repositorio["staging"] = list(artefatos)
    for nome in artefatos:
        print(f"  staged: {nome}")

    print(f"\n  {len(artefatos)} arquivo(s) na staging area.")


def realizar_commit(mensagem: str, artefatos_locais: dict[str, str]) -> str:
    """
    Simula 'git commit -m "<mensagem>"'.
    Grava snapshot dos artefatos em staging com hash e timestamp.
    Retorna o hash simulado do commit.
    """
    print(f"\n{SEP}")
    print(f'  git commit -m "{mensagem}"')
    print(SEP)

    if not _repositorio["staging"]:
        print("  nothing to commit, staging area empty")
        return ""

    # Gera hash simplificado (7 chars) baseado em timestamp
    ts   = datetime.datetime.now()
    hash_commit = format(int(ts.timestamp()) % 0xFFFFFFF, "07x")

    # Salva no log
    entrada = {
        "hash"     : hash_commit,
        "mensagem" : mensagem,
        "timestamp": ts.strftime("%d/%m/%Y %H:%M:%S"),
        "arquivos" : list(_repositorio["staging"]),
    }
    _repositorio["log_commits"].append(entrada)

    # Confirma na área de staging
    for nome in _repositorio["staging"]:
        if nome in artefatos_locais:
            # Atualiza o conteúdo "local confirmado" (aguarda push para remoto)
            pass

    n = len(_repositorio["staging"])
    print(f"  [{BRANCH_PADRAO} {hash_commit}] {mensagem}")
    print(f"  {n} file(s) changed")
    for arq in _repositorio["staging"]:
        print(f"    create/modify: {arq}")

    _repositorio["staging"] = []   # limpa staging após commit
    return hash_commit


def publicar_push(artefatos_locais: dict[str, str], hash_commit: str) -> None:
    """
    Simula 'git push'.
    Sincroniza o repositório remoto com o estado local confirmado.
    """
    print(f"\n{SEP}")
    print(f"  git push")
    print(SEP)

    # Atualiza o repositório remoto
    _repositorio["artefatos"].update(artefatos_locais)

    print(f"  Enumerating objects: {len(artefatos_locais)}, done.")
    print(f"  Counting objects: 100%, done.")
    print(f"  Writing objects: 100%, done.")
    print(f"  To {_repositorio['url']}")
    print(f"     {hash_commit}  {BRANCH_PADRAO} -> {BRANCH_PADRAO}")


def exibir_log() -> None:
    """Exibe o histórico de commits do repositório."""
    print(f"\n{SEP}")
    print("  git log --oneline")
    print(SEP)

    if not _repositorio["log_commits"]:
        print("  (nenhum commit registrado)")
        return

    for entrada in reversed(_repositorio["log_commits"]):
        print(f"  {entrada['hash']}  {entrada['mensagem']}  ({entrada['timestamp']})")
        for arq in entrada["arquivos"]:
            print(f"           └─ {arq}")


def exibir_repositorio_remoto() -> None:
    """Exibe o estado atual do repositório remoto (simulação do GitHub)."""
    print(f"\n{SEP}")
    print(f"  Repositório remoto: {_repositorio['url']}")
    print(f"  Branch: {_repositorio['branch']}")
    print(SEP)
    print("  Artefatos disponíveis no GitHub:")
    print(f"  {SEP_MENOR}")
    for nome, conteudo in _repositorio["artefatos"].items():
        linhas = conteudo.count("\n") + 1
        print(f"  📄 {nome:<30} ({linhas} linha(s))")
    print(f"  {SEP_MENOR}")
    print(f"  Total: {len(_repositorio['artefatos'])} artefato(s)")