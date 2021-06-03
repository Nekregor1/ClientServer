def main():
    s1 = 'разработка'
    s2 = 'администрирование'
    s3 = 'protocol'
    s4 = 'standart'

    bs1 = s1.encode('utf-8')
    bs2 = s2.encode('utf-8')
    bs3 = s3.encode('utf-8')
    bs4 = s4.encode('utf-8')


    print(s1, bs1, bs1.decode('utf-8'))
    print(s2, bs2, bs2.decode('utf-8'))
    print(s3, bs3, bs3.decode('utf-8'))
    print(s4, bs4, bs4.decode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)