def main():
    s1 = 'разработка'
    s2 = 'сокет'
    s3 = 'декоратор'

    print(s1, type(s1))
    print(s2, type(s2))
    print(s3, type(s3))

    s1b = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
    s2b = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
    s3b = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

    print(s1b, type(s1b))
    print(s2b, type(s2b))
    print(s3b, type(s3b))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)