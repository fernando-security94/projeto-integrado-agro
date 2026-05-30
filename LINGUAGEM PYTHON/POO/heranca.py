from abc import ABC, abstractmethod


class Pai:
    def exibir_mensagem(self):
        print("Método definido na classe pai")

class Filha(Pai):
    ...

teste = Filha()
teste.exibir_mensagem()


# leitor e extrator de pdf
class ExtratorBase(ABC):
    def carregar_doc(self):
        print("Essa função carregará o arquivo PDF ou imagem para o sistema")
        pass

    @abstractmethod
    def extrair_texto(self):
        raise NotImplementedError
    
# criar a classe que extrai do PDF
class ExtratorPDF(ExtratorBase):
    def extrair_texto(self):
        print("Algoritmo para extração de texto do PDF.")
        pass

class ExtratorImagem(ExtratorBase):
    def extrair_texto(self):
        print("Algoritmo para extração de texto de uma image.")
        pass





"""
Começaremos importando a classe ABC e o decorator abstractmethod,
que serão usados para criar uma classe base abstrata, 
a qual chamaremos de ExtratorBase. 
Essa classe implementará um método para carregar o arquivo no sistema e um método abstrato 
para extrair o texto do documento. 
Este segundo método será abstrato, pois o algoritmo para extração do texto será diferente, 
dependendo do tipo arquivo.

O próximo passo é criar uma classe para cada tipo de documento, 
implementando o algoritmo necessário para a 
extração do texto na função extrair_texto().
"""