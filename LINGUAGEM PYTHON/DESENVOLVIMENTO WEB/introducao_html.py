from IPython.display import HTML

# criando pagina HTML com Python

html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Exemplo de Front-end com Python</title>
        <style>
            body{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0; 
            }

            h1{
                font-size: 48px;
                color: #333;
            }

            p{
                font-size: 24px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <h1>Olá, minha vida! ❤️</h1>

        <p>Criei esta página pra dizer que te amo!❤️❤️❤️</p>
    </body>
    </html>
'''

# salvar como HTML 
with open("pagina_gatinha.html", "w", encoding='utf-8') as f:
    f.write(html_code)

print("Arquivo HTML criado com sucesso")
