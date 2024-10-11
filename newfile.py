import asyncio
from telethon import TelegramClient, errors

# Ваши данные
API_ID = '28953736'  # Ваш API ID
API_HASH = '58712218f5a2d39b2d0b04d711e4ab50'  # Ваш API HASH
PHONE_NUMBER = '+79935831593'  # Ваш номер телефона
CHANNELS = ['@kupitrafik', '@trafic_kuplya_prodazha', '@trafikstt', '@buytraf', '@cpa4life', '@logovo_traferov']  # Ваши каналы
MESSAGE = '''НАБОР В ЗАКРЫТЫЙ ТГК ПО ЗАРАБОТКУ! 😳

ТЕМКИ, СХЕМЫ ЗАРАБОТКА, АБУЗЫ, РАЗДАЧИ ЧЕКОВ КБ, БЕСПЛАТНЫЕ КРЕО ДЛЯ АРБИТРАЖА И МНОГОЕ ДРУГОЕ! 💸 

ПЕРЕХОДИ К НАМ В ТЕЛЕГРАМ КАНАЛ. 😉

ССЫЛКА: https://t.me/+cA9btn1-nCtkZDNi 🔗''' # Сообщение, которое нужно отправить

async def send_message(client):
    while True:
        for channel in CHANNELS:
            try:
                await client.send_message(channel, MESSAGE)
                print(f'Сообщение отправлено в {channel}')
                await asyncio.sleep(1)  # Небольшая пауза между отправками
            except errors.FloodWait as e:
                print(f'Слишком частые запросы. Подождите {e.seconds} секунд.')
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f'Ошибка при отправке сообщения: {e}')
        
        await asyncio.sleep(30)  # Ждем 10 минут

async def main():
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        await send_message(client)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
