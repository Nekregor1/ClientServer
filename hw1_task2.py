
def main():
    sb1 = bytes('class', 'utf-8')
    sb2 = bytes('function', 'utf-8')
    sb3 = bytes('method', 'utf-8')

    print(sb1, len(sb1))
    print(sb2, len(sb2))
    print(sb3, len(sb3))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)