from config import *
from telethon import TelegramClient, events
from models import telegram_users, _event_

client = TelegramClient('sessions/bot', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('🥳Приветствую, скоро новый год, поэтому давайте сыграем в тайного санту!🥳 \nВведите секретный код, чтобы узнать правила!')


@client.on(events.NewMessage(pattern='ЦКБ2023'))
async def rules(event):
    await event.respond('Суть игры состоит в обмене подарками между всеми участниками.🎁🎁🎁 '
                        '\nИмя человека, которому вы дарите подарок, выбирается случайным образом и сообщается только вам. '
                        'До момента обмена подарками никто не знает, кто кому дарит подарок. '
                        'И ни один участник, не знает, кому выпало его имя. '
                        '\nДля участия заполните свой профиль /profile')


@client.on(events.NewMessage(pattern='/profile'))
async def profile(event):
    await event.respond('Для участия вам нужно пройти небольшой опрос')
    await event.respond('Как вас зовут?')

    # await event.respond('В каком отделе вы работаете?')
    # await event.respond('Расскажите о своих интересах, хобби')
    # await event.respond('Чего вы ждете от 2023 года?')


def main():
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
