from flask import Flask, render_template, request

# para usar emojis - win + period

app = Flask(__name__)


# app route cria uma nova pagina no formulario
# que são caminhos dentro do site como 
# pagina sobre mim e inicio

@app.route('/')
def index():
    nome = "Poliane Novaes"
    return render_template('index.html', nome=nome)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.form == 'POST':
        nome = request.form['nome']
        mensagem = request.form['mensagem']
        return f"Obrigado, {nome}! Sua mensagem foi recebida: {mensagem}"
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)