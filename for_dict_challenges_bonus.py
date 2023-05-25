"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
from typing import Dict, Tuple, List


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def make_freq_dict_by_key(messages_list: List[Dict], key: str) -> Dict:
    """
    Принимает список словарей с информацией по сообщениям в чате
    и ключ, по которому необходимо осуществить подбор данных.
    Например, если передать ключ "sent_by",
    то функуия сначала создаст список, сотоязий из id пользователей, кто написал каждое сообщение,
    а потом создаст частотный словарь, где ключами будут id пользователей,
    а значениями - количество сообщений, написанных ими в чате.
    :param messages_list: список словарей с информацией по сообщениям в чате
    :param key: ключ,
    по которому необходимо осуществить подбор данных по сообщениям
    :return: частотный словарь
    """
    some_list = [message[key] for message in messages_list if message[key]]
    freq_dict = {value: some_list.count(value) for value in set(some_list)}
    return freq_dict


def find_items_with_max_values(freq_dict: Dict) -> Tuple[List, int]:
    """
    Функция определяет ключи с максимальным значением.
    :param freq_dict: словарь, значения в котором являются целыми числами
    :return: кортеж из двух элементов.
    Первый элемент - список ключей с максимальным значением
    Второй элемент - максимальное значение (целое число)
    """
    max_freq = max(freq_dict.values())
    max_freq_items = [name for name, freq in freq_dict.items() if freq == max_freq]
    return max_freq_items, max_freq


def users_wrote_max(messages_list: List[Dict]) -> Tuple[List, int]:
    """
    Функция вычисляет пользователей, которые написали максимальное количество сообщений в чате
    :param messages_list: список словарей с информацией по сообщениям в чате
    :return кортеж из двух элементов.
    Первый элемент - список id пользователей.
    Второй элемент - максимальное число сообщений
    """
    return find_items_with_max_values(make_freq_dict_by_key(messages_list, 'sent_by'))


def users_got_max_replies_by_one_message(messages_list: List[Dict]) -> Tuple[List, int]:
    """
    Функция вычисляет пользователей, сообщения которых получили максимальное количество ответов
    (к одному сообщению)
    :param messages_list: список словарей с информацией по сообщениям в чате
    :return: кортеж из двух элементов.
    Первый элемент - список id пользователей
    Второй элемент - максимальное число ответов на сообщение
    """
    messages_with_max_replies = find_items_with_max_values(make_freq_dict_by_key(messages_list, 'reply_for'))
    users_got_max_replies = [message['sent_by'] for message in messages_list if
                             message['id'] in messages_with_max_replies[0]]
    max_replies_by_one_message = messages_with_max_replies[1]
    return users_got_max_replies, max_replies_by_one_message


def users_got_max_replies_total(messages_list: List[Dict]) -> Tuple[List, int]:
    """
    Функция вычисляет пользователей,
    которые суммарно получили максимальное количество ответов на все свои сообщения
    :param messages_list: список словарей с информацией по сообщениям в чате
    :return: кортеж из двух элементов.
    Первый элемент - список id пользователей
    Второй элемент - максимальное число ответов
    """
    replies_cnt_by_message = make_freq_dict_by_key(messages_list, 'reply_for')
    messages_with_reply_info = dict()
    for message_with_reply in replies_cnt_by_message.keys():
        message_info = dict()
        for message in messages_list:
            if message['id'] == message_with_reply:
                message_info['sent_by'] = message['sent_by']
                message_info['replies_cnt'] = replies_cnt_by_message[message_with_reply]
        messages_with_reply_info[message_with_reply] = message_info

    total_replies_cnt_by_users = dict()
    for message in messages_with_reply_info.values():
        if message['sent_by'] in total_replies_cnt_by_users:
            total_replies_cnt_by_users[message['sent_by']] += message['replies_cnt']
        else:
            total_replies_cnt_by_users[message['sent_by']] = message['replies_cnt']

    return find_items_with_max_values(total_replies_cnt_by_users)


def users_wrote_messages_seen_by_max_users(messages_list: List[Dict]) -> Tuple[List, int]:
    """
    Функция вычисляет пользователей,
    сообщения которых увидело максимальное количество уникальных пользователей
    :param messages_list: список словарей с информацией по сообщениям в чате
    :return: кортеж из двух элементов.
    Первый элемент - список id пользователей
    Второй элемент - максимальное число уникальных пользователей, увидевших сообщения
    """
    sent_by_seen_by_dict = dict()

    for message in messages_list:
        sent_by = message['sent_by']
        seen_by = message['seen_by']
        if sent_by not in sent_by_seen_by_dict:
            sent_by_seen_by_dict[sent_by] = []
        if sent_by in sent_by_seen_by_dict:
            sent_by_seen_by_dict[sent_by].extend(seen_by)

    for item in sent_by_seen_by_dict:
        unique_ids = set(sent_by_seen_by_dict[item])
        sent_by_seen_by_dict[item] = len(unique_ids)

    return find_items_with_max_values(sent_by_seen_by_dict)


def count_messages_by_time_period(messages_list: List[Dict], start_hour: int, finish_hour: int) -> int:
    """
    Функуия считает количество сообщений, написанных в определённые часы
    :param messages_list: список словарей с информацией по сообщениям в чате
    :param start_hour: час начала
    :param finish_hour: час окончания
    :return: количество сообщений, написанных в определённые часы
    """
    count = len([message for message in messages_list if start_hour <= message['sent_at'].hour < finish_hour])
    return count


def find_prime_time_period(messages_list, *hours: int) -> str:
    """
    Функуия определяет, в какой из периодов времени в сутках написано больше всего сообщений в чате
    :param messages_list: список словарей с информацией по сообщениям в чате
    :param hours: часы, определяющие временные границы периодов для подсчёта сообщений
    :return: строка с информацией о периоде времени, когда написано максимальное количество сообщений
    """
    time_periods = []
    time_periods.extend([(0, hours[0]), (hours[-1], 24)])
    for n in range(len(hours)):
        if n < len(hours) - 1:
            time_periods.append((hours[n], hours[n + 1]))

    messages_by_time_dict = {time_period: count_messages_by_time_period(messages_list, time_period[0], time_period[1])
                             for time_period in time_periods}
    prime_time_info = find_items_with_max_values(messages_by_time_dict)

    match prime_time_info[0][0]:
        case (0, 12):
            return 'утром (до 12 часов)'
        case (12, 18):
            return 'днём (12-18 часов)'
        case (18, 24):
            return 'вечером (после 18 часов)'

    return f'c {prime_time_info[0][0][0]} до {prime_time_info[0][0][1]} часов'


def messages_with_longest_threads(message_list: List[Dict]) -> Tuple[List, int]:
    """
    Функция вычисляет сообщения, которые стали началом для самых длинных тредов (цепочек ответов)
    :param message_list: список словарей с информацией по сообщениям в чате
    :return: кортеж из двух элементов.
    Первый элемент - список id сообщений
    Второй элемент - максимальное число сообщений в треде
    """
    reply_messages = [message for message in message_list if message['reply_for']]
    reply_messages_ids = [message['id'] for message in reply_messages]
    reply_chain_length_by_message = dict()

    for message in reply_messages:
        count = 2
        parent_message_id = message['reply_for']
        while parent_message_id in reply_messages_ids:
            count += 1
            parent_message_id = reply_messages[reply_messages_ids.index(parent_message_id)]['reply_for']
        reply_chain_length_by_message[parent_message_id] = count

    return find_items_with_max_values(reply_chain_length_by_message)


if __name__ == "__main__":
    messages = generate_chat_history()

    print(f'1. Пользователи с id {users_wrote_max(messages)[0]} написал(и) сообщений больше всех '
          f'({users_wrote_max(messages)[1]} шт.)')

    print(f'2а. Сообщения с максимальным количеством ответов были отправлены пользователями '
          f'с id {users_got_max_replies_by_one_message(messages)[0]} '
          f'({users_got_max_replies_by_one_message(messages)[1]} ответа(-ов))')

    print(f'2б. Больше всего ответов (суммарно на все свои сообщения)'
          f' получили пользователи с id {users_got_max_replies_total(messages)[0]} '
          f'({users_got_max_replies_total(messages)[1]} ответа(-ов))')

    print(f'3. Id пользователей, сообщения которых видело больше всего уникальных пользователей: '
          f'{users_wrote_messages_seen_by_max_users(messages)[0]}')

    print(f'4. Больше всего сообщений в чате {find_prime_time_period(messages, 12, 18)}')

    print(f'5. Id сообщений, которые стали началом для самых длинных тредов '
          f'{list(map(str, messages_with_longest_threads(messages)[0]))} '
          f'(длина треда - {messages_with_longest_threads(messages)[1]} сообщений)')