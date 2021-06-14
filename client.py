"""Реализовать простое клиент-серверное взаимодействие по протоколу 
JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции.
    Функции клиента:
        сформировать presence-сообщение;
        отправить сообщение серверу;
        получить ответ сервера;
        разобрать сообщение сервера;
        параметры командной строки скрипта client.py <addr> [<port>]:
            addr — ip-адрес сервера;
            port — tcp-порт на сервере, по умолчанию 7777."""

from socket import *
import pickle
import time
import argparse

def main():

    parser = argparse.ArgumentParser(description='Client')
    parser.add_argument('-a', '--address', default='localhost')
    parser.add_argument('-p', '--port', default=7777, type=int)

    socket_client = socket_open(parser.parse_args().address, parser.parse_args().port)
    
    socket_work(socket_client)
    socket_close(socket_client)



def socket_open(addr='localhost', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8887))
    print('client socket open')
    return s

def socket_close(s):
    s.close()
    print('client socket close')

def presence_msg(name="anonymous"):
    return {
        "action": "presence",
        "time": time.time(),
        "user": {
            "account_name": name,
            "status": "Yep, I am here!"
        }   
    } 


def server_msg(s):
    data = s.recv(1024)

    if pickle.loads(data)["response"] == 100:
        print('базовое уведомление')
    elif pickle.loads(data)["response"] == 101:
        print('важное уведомление')
    elif pickle.loads(data)["response"] == 200:
        print('Все ОК!')
    elif pickle.loads(data)["response"] == 201:
        print('объект создан!')
    elif pickle.loads(data)["response"] == 202:
        print('подтверждение!')
    elif pickle.loads(data)["response"] == 400:
        print('неправильный запрос/JSON-объект!')
    elif pickle.loads(data)["response"] == 401:
        print('не авторизован!')
    elif pickle.loads(data)["response"] == 402:
        print('неправильный логин/пароль!')
    elif pickle.loads(data)["response"] == 403:
        print('пользователь заблокирован!')
    elif pickle.loads(data)["response"] == 404:
        print('пользователь/чат отсутствует на сервере!')
    elif pickle.loads(data)["response"] == 409:
        print('уже имеется подключение с указанным логином!')
    elif pickle.loads(data)["response"] == 410:
        print('адресат существует, но недоступен (offline)!')
    elif pickle.loads(data)["response"] == 500:
        print('Ошибка сервера')
    else:
        print('Неизвестный ответ!!!')
    return data

def socket_work(s):
    msg = presence_msg()
    s.send(pickle.dumps(msg))
    data = server_msg(s)
    print('Сообщение от сервера: ', pickle.loads(data), ', длиной ', len(data))

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)