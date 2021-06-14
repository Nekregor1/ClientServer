"""Реализовать простое клиент-серверное взаимодействие по протоколу 
JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции.

    Функции сервера:
        принимает сообщение клиента;
        формирует ответ клиенту;
        отправляет ответ клиенту;
        имеет параметры командной строки:
            -p <port> — TCP-порт для работы (по умолчанию использует 7777);
            -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)."""

from socket import *
import time
import pickle
import argparse
# import sys



def main():

    parser = argparse.ArgumentParser(description='Server')
    parser.add_argument('-a', '--addr', default='localhost')
    parser.add_argument('-p', '--port', default=7777, type=int)
    
    socket_serv = socket_open(parser.parse_args().addr, parser.parse_args().port)

    socket_work(socket_serv)




def socket_open(addr='localhost', port=7777):

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 8887))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    print('server socket open')
    return s

def socket_close(s):
    s.close()
    print('client socket close')

def client_msg(client):
    data = client.recv(1024)
    return data

def server_msg(client_data):
    print('Полученное сообщение от пользователья ', pickle.loads(client_data))
    if pickle.loads(client_data)["action"] == "presence":
        return {
            "response": 200,
            "time": time.time(),
            "alert": "Good job!"
        }

def socket_work(s):
    while True:
        client, addr = s.accept()
        client_data = client_msg(client)
        response = server_msg(client_data)
        client.send(pickle.dumps(response))

        socket_close(client)

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)
