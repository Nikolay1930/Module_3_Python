import vk_api
from course import *
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from wiki import *


token = 'vk1.a.geUZPZjlh_I30_stLqMG6qYjDS-Fg4POq8pXz6jUHR96KfOLlo0vyEJnEQHrifjd-81OY9ChyT7B_2HnwNvI6UBhpxeNCU4ik_o2SnzSd1yAf4Erl1-9umBYmo1F5rSrQvG50HGcFofyueXonQdMc_KHt_s84VyDirKrz-So6MvHuuoEUWfRrx-WyiV647tsyGPmSrf3HcGAukOBf79IlQ'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        msg_id = randint(1, 10 ** 7)
        print(msg)
        if msg[:2] == '-к':
            res = f'1$ = {get_course("R01235")}'
        elif msg.startswith('-в'):
            res = get_wiki_article(msg[3:])
        else:
            res = 'Не понимаю, что ты хочешь'
        vk.messages.send(user_id=user_id, random_id=msg_id, message=res)
        print(res)