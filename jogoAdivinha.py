from flask import Flask, render_template, request, jsonify
from random import randint

app = Flask(__name__)
pensaNumero = randint(0, 100)
palpite = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adivinhar', methods=['POST'])
def adivinhar():
    global palpite
    palpite += 1
    numUsuario = int(request.form['numero'])
    resposta = ''
    if numUsuario == pensaNumero:
        resposta = f"Parabéns! Você acertou o número em {palpite} palpites!"
        palpite = 0
    elif numUsuario < pensaNumero:
        resposta = "O valor é maior, tente novamente..."
    else:
        resposta = "O valor é menor, tente novamente..."
    return jsonify(resposta=resposta)

if __name__ == '__main__':
    app.run(debug=True)
