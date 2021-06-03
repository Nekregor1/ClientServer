def main():
    with open('test_file.txt', 'w+') as f:
        f.write('сетевое программирование\n')
        f.write('сокет\n')
        f.write('декоратор\n')
    
    f.close()

    # with open('test_file.txt', 'r', encoding='utf-8') as f:
    with open('test_file.txt', 'r', encoding='cp1251') as f:
        for line in f:
            print(line)
    f.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
