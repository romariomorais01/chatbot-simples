from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def saudacao_inicial():
    hora = datetime.now().hour
    if 6 <= hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def responder(mensagem):
    mensagem = mensagem.lower()
    if mensagem == "sair":
        return "Bot: Até logo!"
    elif "oi" in mensagem:
        return "Bot: Olá, tudo bem?"
    elif "tudo" in mensagem:
        return "Bot: Que bom! Em que posso te ajudar hoje?"
    elif "tchau" in mensagem:
        return "Bot: Até mais!"
    else:
        return "Bot: Não entendi, pode repetir?"

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "")
    resposta = responder(mensagem)
    return jsonify({"resposta": resposta})

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"saudacao": saudacao_inicial()})

if __name__ == "__main__":
    app.run(debug=True)