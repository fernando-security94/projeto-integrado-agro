import numpy as np

# Dados dos participantes
participantes = [{
    "Nome":"Alice",
    "Localização":"EUA",
    "Afiliação":"Universidade A",
    "Interesses":["Física", "Astronomia"]

},
{
    "Nome":"Bob",
    "Localização":"Brasil",
    "Afiliação":"Universidade B",
    "Interesses":["Biologia", "Astronomia"]
},
{
    "Nome":"Charlie",
    "Localização":"Índia",
    "Afiliação":"Universidade C",
    "Interesses":["Química", "Engenharia"]
}
]

# Utilizando sets para identificar regiões
regioes = set(participante["Localização"] for participante in participantes)

# Utilizando um dicionário para categorizar afiliações
afiliacoes = {}
for participante in participantes:
    afiliacao = participante["Afiliação"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
        afiliacoes[afiliacao].append(participante["Nome"])

# Utilizando numpy para analisar areas de interesse
areas_interesse = np.array([interesse for participante in participantes for interesse in participante["Interesses"]])

interesse_unico, contagem = np.unique(areas_interesse, return_counts=True)

area_popular = interesse_unico[np.argmax(contagem)]

# Resultados
print(f'Regiões dos participantes: {regioes}\n')

print(f'Afiliações dos participantes:')
for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {",".join(nomes)}')

print(f'Área de interesse popular: {area_popular}\n')
