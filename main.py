import telebot
from openai import OpenAI
import time
from io import BytesIO

from config import TOKENT
from config import gptApi

from pathlib import Path



bot = telebot.TeleBot(TOKENT)
client = OpenAI(api_key=gptApi)



user_states = {}  # Состояния пользователей (включено/выключено взаимодействие)

@bot.message_handler(commands=['start'])
def start(message):
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Здравствуйте {first_name}, я ваш личнй ассистент. Чем могу помочь?\n\nopen source at <no link>")
    time.sleep(2)
    bot.send_message(message.chat.id, 'Введите /help для подробной информации')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Основные комманды:\n/image: для генерации фото \n /tts: Создать речь из текста (папример /tts hello)\n/help: показать справочное сообщение/ ')

@bot.message_handler(commands=['tts'])
def text_to_speech(message):
    command_parts = message.text.split(maxsplit=1)

    if len(command_parts) < 2 or not command_parts[1].strip():
        bot.send_message(message.chat.id, "Вы не ввели описание для генерации фото. Пожалуйста, укажите описание.")
        return
    
    prompt = command_parts[1].strip()

    bot.send_message(message.chat.id, "Пожалуйста, подождите...")

    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=prompt,
    response_format='opus'
    )

    
    temp_file = BytesIO()
    temp_file.write(response.read())
    temp_file.seek(0)
    bot.send_voice(message.chat.id, temp_file)

@bot.message_handler(commands=['image'])
def img_generate(message):
    
    command_parts = message.text.split(maxsplit=1)

    # Проверка на наличие текста в аргументе
    if len(command_parts) < 2 or not command_parts[1].strip():
        bot.send_message(message.chat.id, "Вы не ввели описание для генерации фото. Пожалуйста, укажите описание.")
        return

    # Получаем текст после команды /image
    prompt = command_parts[1].strip()

    bot.send_message(message.chat.id, "Пожалуйста, подождите...")

    response = client.images.generate(
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
   
    )

    bot.send_photo(message.chat.id, response.data[0].url)
    

@bot.message_handler(content_types=['text'])
def assistant(message): 
    prompt = message.text

    response = client.completions.create(
        model='text-davinci-003',
        prompt= prompt,
        max_tokens=4000,
        temperature=0.7,
        n=1,
        stop=None
        )
    assistant_reply = response.choices[0].text

    # Отправка ответа от ассистента
    bot.send_message(message.chat.id, f"Ответ ассистента: {assistant_reply}")


   
    

bot.polling(none_stop=True)




