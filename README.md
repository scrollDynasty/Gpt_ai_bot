# Gpt_ai_bot

## 🌟 Collaboration
This project is a collaborative effort between **scrollDynasty** and **VladislavXD**. Together, we've built a powerful Telegram bot leveraging OpenAI's GPT capabilities. The current version of this project is **1.0.0**.

---

## 📚 Project Overview
Gpt_ai_bot is a Telegram bot designed to:
- Generate text-based responses using OpenAI models.
- Convert text to speech (TTS).
- Create AI-generated images.

Whether you're looking for an intelligent assistant or fun AI-generated content, this bot has you covered!

---

## 🔧 Features
- **/start**: Initiate the bot and get a welcome message.
- **/help**: Learn about all available commands.
- **/tts [text]**: Convert your input text to speech.
- **/image [description]**: Generate an AI-based image from a text prompt.
- **Intelligent Chat Assistant**: Responds to any text input with smart replies.

---

## ⚖️ Installation Guide
Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/scrollDynasty/Gpt_ai_bot.git
cd Gpt_ai_bot
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Bot
Update the `config.py` file with your credentials:

```python
# config.py
CHAT_ID = -1002003233027  # Replace with your Telegram chat ID
TOKENT = 'your-telegram-bot-token'  # Replace with your Telegram bot token
gptApi = 'your-openai-api-key'  # Replace with your OpenAI API key
```

### 5. Run the Bot
```bash
python3 main.py
```

---

## ℹ️ Usage
- Open Telegram and start a chat with your bot.
- Use `/help` to explore available commands.
- Enjoy your AI-powered assistant!

---

## ✨ Future Plans
- Add more TTS voices.
- Enhance image generation with more customizable options.
- Implement advanced conversational capabilities.

---

## ✨ Credits
Special thanks to **scrollDynasty** and **VladislavXD** for their dedication and collaborative efforts in building this project.

