# -*- coding: utf-8 -*-
def main():
    import subprocess

    args1 = ['ping', 'yandex.ru']
    args2 = ['ping', 'youtube.com']

    subprocess_ping1 = subprocess.Popen(args1, stdout=subprocess.PIPE)
    for line in subprocess_ping1.stdout:
        l = line.decode('cp866')
        print(l, type(l))

    subprocess_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)
    for line in subprocess_ping2.stdout:
        l = line.decode('cp866')
        print(l, type(l))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
