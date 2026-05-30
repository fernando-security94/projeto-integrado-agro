"""
Ambientes virtuais em Python (venv)

Um ambiente virtual carrega toda a sua instalação do Python
para uma pasta no caminho escolhido.
Ao instalar um ambiente virtual, a instalação do ambiente virtual
será usada.
- venv é o modo utilizado para criar ambientes virtuais. 
- Qualquer nome pode ser atribuído a um ambiente virtual, mas os mais comuns são:
- venv; env; .venv; .env

Como criar venv 
Digitar no terminal:
python -m venv venv 

Dentro do venv temos:

- include - 
- lib - Tudo o que for instalado será enviado para essa pasta
- scripts - Possui todos os executáveis, tanto para ativar o venv
quanto para os executáveis de Python, e pip que é instalador de pacotes
do Python.


Como achar a pasta do Python:
Terminal: gcm python -Syntax

Como ativar o venv:
Terminal: venv\Scripts\Activate

Comando pip é utilizado para instalar módulos de forma local ou globaln
"""