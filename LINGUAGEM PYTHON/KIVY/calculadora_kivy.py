# app de calculadora com Python, Kivy and KivyMD

# aplicacao de calculadora em Python
# utilizando Kivy and KivyMD

from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    MDTextField:
        id: entrada
        hint_text: "0"
        font_size: 32
        halign: "right"
        readonly: True  # impedir digitação manual
        size_hint_y: 0.2

    GridLayout:
        cols: 4
        spacing: 10
        size_hint_y: 0.8

        MDRaisedButton:
            text: "7"
            on_release: app.adicionar_texto('7')

        MDRaisedButton:
            text: "8"
            on_release: app.adicionar_texto('8')

        MDRaisedButton:
            text: "9"
            on_release: app.adicionar_texto('9')

        MDRaisedButton:
            text: "/"
            on_release: app.adicionar_texto('/')

        MDRaisedButton:
            text: "4"
            on_release: app.adicionar_texto('4')

        MDRaisedButton:
            text: "5"
            on_release: app.adicionar_texto('5')

        MDRaisedButton:
            text: "6"
            on_release: app.adicionar_texto('6')

        MDRaisedButton:
            text: "*"
            on_release: app.adicionar_texto('*')

        MDRaisedButton:
            text: "1"
            on_release: app.adicionar_texto('1')

        MDRaisedButton:
            text: "2"
            on_release: app.adicionar_texto('2')

        MDRaisedButton:
            text: "3"
            on_release: app.adicionar_texto('3')

        MDRaisedButton:
            text: "-"
            on_release: app.adicionar_texto('-')

        MDRaisedButton:
            text: "0"
            on_release: app.adicionar_texto('0')

        MDRaisedButton:
            text: "."
            on_release: app.adicionar_texto('.')

        MDRaisedButton:
            text: "C"
            on_release: app.limpar()

        MDRaisedButton:
            text: "+"
            on_release: app.adicionar_texto('+')

    MDRaisedButton:
        text: "="
        on_release: app.calcular()
        size_hint_y: 0.2
'''


class CalculadoraApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def adicionar_texto(self, texto):
        entrada = self.root.ids.entrada
        if entrada.text == "0":
            entrada.text = texto
        else:
            entrada.text += texto

    def limpar(self):
        self.root.ids.entrada.text = "0"

    def calcular(self):
        try:
            resultado = eval(self.root.ids.entrada.text)
            self.root.ids.entrada.text = str(resultado)
        except:
            self.root.ids.entrada.text = "Erro"


if __name__ == '__main__':
    CalculadoraApp().run()
