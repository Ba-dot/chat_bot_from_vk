import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
from datetime import datetime
import random
import time

session = vk_api.VkApi(token='ваш токен')
session_api = session.get_api()
longpool = VkLongPoll(session)

hello_list = ('и тебе привет','привет','доброго времени суток)','привет ковбой)','здрасти',)
while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print("сообщение пришло в ", event.datetime)
            print("текст сообщения", event.text)
            response = event.text.lower()
            if event.from_user and not event.from_me:
                if response.find('привет') >= 0 or response.find('здравствуй') >= 0 or response.find('hello') >= 0:
                    time.sleep(random.uniform(0.5,4.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                    'message' : random.choice(hello_list),
                                                    'random_id':'0'})
                elif response.find('как дела?') >= 0:
                    time.sleep(random.uniform(0.5,4.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                    'message' : '',
                                                    'random_id':'0',
                                                    'sticker_id':'9045'})
                elif response.find('фото') >= 0:
                    time.sleep(random.uniform(0.5, 4.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': '',
                                                     'random_id': '0',
                                                     'atachment': 'вставляйте id - профиля_файла'})