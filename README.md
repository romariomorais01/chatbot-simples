### ✨ Sugestão de atualização para o `README.md`

```markdown
# Chatbot em Python 🤖

Um chatbot simples desenvolvido em Python para treinar lógica de programação e estruturas básicas.  
Evoluiu para uma **API Flask**, permitindo integração com aplicações externas (frontend, Postman, etc.).

## 🚀 Funcionalidades
- Cumprimento inicial baseado no horário do dia (bom dia, boa tarde, boa noite).
- Reconhecimento de palavras-chave como "oi", "tchau", "tudo bem".
- Comando especial para encerrar a conversa (`sair`).
- Exposição como API REST com rotas:
  - `GET /saudacao` → retorna saudação baseada no horário.
  - `POST /chat` → recebe mensagem e retorna resposta do bot.

## 🛠️ Tecnologias utilizadas
- Python 3.x
- Biblioteca padrão (`datetime` para saudação)
- Flask (para criação da API)

## ▶️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot.git
   cd chatbot
   ```
2. Instale as dependências:
   ```bash
   pip install flask
   ```
3. Execute o servidor:
   ```bash
   python app.py
   ```
4. Acesse no navegador ou Postman:
   - `http://127.0.0.1:5000/saudacao` (GET)
   - `http://127.0.0.1:5000/chat` (POST com JSON body)

   Exemplo de body:
   ```json
   { "mensagem": "oi" }
   ```

## 📸 Prints da evolução
- Chatbot codigo inicial
  <img width="966" height="271" alt="image" src="https://github.com/user-attachments/assets/833d032c-682d-4fbc-afe7-68d215ceafda" />

- Código atualizado com Flask.
  <img width="1162" height="977" alt="image" src="https://github.com/user-attachments/assets/c5895344-b7d3-48ea-81ee-50f2ba10c184" />


## 🔮 Próximos passos
- Deploy em nuvem (Railway/Render/Heroku).
- Criar interface web simples para interação.
- Expandir respostas e funcionalidades do bot.
