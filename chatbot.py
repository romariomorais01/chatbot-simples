from datetime import datetime

def saudacao_inicial():
    hora = datetime.now().hour
    if 6<= hora <12:
        return "Bom dia!"
    elif 12<= hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    

def chatbot ():
    print (f"Chatbot iniciado! {saudacao_inicial()} Para encerrar, digite 'sair'")
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() =="sair":
            print ("Bot: Até logo!")
            break
        elif "oi" in mensagem.lower():
            print("Bot: Olá, tudo bem?")
        elif "tudo" in mensagem.lower():
            print("Que bom! Em que posso te ajudar hoje?")
        elif "tchau" in mensagem.lower ():
            print ("Bot: Até mais!")
        else:
            print("Bot: Não entendi, pode repetir?")

chatbot()