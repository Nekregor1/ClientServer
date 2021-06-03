def main():
    
    b1 = b'attribute'
    #b2 = b'класс'
    #b3 = b'функция'
    b4 = b'type'

    b2 = bytes('класс', 'utf-8')
    b3 = bytes('функция', 'utf-8')

    print(b1)
    print(b2)
    print(b3)
    print(b4)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)