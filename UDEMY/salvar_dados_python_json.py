import json

# people = {
#     "nome": "Fernando",
#     "sobrenome": "Ribeiro",
#     "enderecos": [
#         {"rua1": "R1", "numero" : "32"},
#         {"rua2": "R2", "numero": "55"},
#     ],
#     "altura": 1.82,
#     "numeros_preferidos": (2, 4, 5, 7, 10),
#     "dev": True,
#     "nada": None, 
# }

# with open("salvar_dados_python_json.json", "w", encoding="utf-8") as file:
#     json.dump(people, file, indent=2)


# Utilizando função load. O arquivo está sendo carregado de fora do Python, pois foi salvo anteriormente.
# Utilizar json para apenas dados simples, apesar de haver algumas conversões de Python para json,
# e depois de json para python, muda novamente. Uma tupla vira array, e depois volta como lista.
# sets em Python não são suportados em json

with open("salvar_dados_python_json.json", 'r', encoding="utf-8") as file:
    person = json.load(file)
    print(person)
    print(type(person))