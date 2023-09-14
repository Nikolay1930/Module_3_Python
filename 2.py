import vk_api
from pprint import pprint
from course import *

token = 'vk1.a.geUZPZjlh_I30_stLqMG6qYjDS-Fg4POq8pXz6jUHR96KfOLlo0vyEJnEQHrifjd-81OY9ChyT7B_2HnwNvI6UBhpxeNCU4ik_o2SnzSd1yAf4Erl1-9umBYmo1F5rSrQvG50HGcFofyueXonQdMc_KHt_s84VyDirKrz-So6MvHuuoEUWfRrx-WyiV647tsyGPmSrf3HcGAukOBf79IlQ'
vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    print(messages)
    if messages['count'] != 0:
        msg = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        msg_id = messages['items'][0]['last_message']['id']
        if msg.lower() == 'курс':
            vk.method('messages.send', {'user_id': user_id, 'random_id': msg_id, 'message': get_course("R01235")})
            print(get_course("R01235"))
        else:
            vk.method('messages.send', {'user_id': user_id, 'random_id': msg_id, 'message': msg})