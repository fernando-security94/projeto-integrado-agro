# Calculo de media utilizando funcoes

notas = [8, 7.5, 3.75, 3, 8.5]

#funcao que calcula a media
def calculo_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

# funcao lambda que arredonda a media com 2 casas decimais
# lambda foi escolhida por ser chamada apenas uma vez.
arredonda_media = lambda media: round(media, 2)

# chama a função passando as notas como parametro
media = calculo_media(notas)
media_final = arredonda_media(media)

print(f'Notas do estudante: {notas}')
print(f'A média final é {media_final}')

if media_final < 6:
    print("Aluno reprovado!\n")
else:
    print("Aluno aprovado!")


