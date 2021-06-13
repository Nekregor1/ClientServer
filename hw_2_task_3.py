"""
Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
    
    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
    второму — целое число, третьему — вложенный словарь, где значение каждого ключа — 
    это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);

    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
    При этом обеспечить стилизацию файла с помощью параметра default_flow_style, 
    а также установить возможность работы с юникодом: allow_unicode = True;

    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

"""
import yaml

def main():
    dictYaml = {
        "first_key": [1,2,3],
        "second_key": 42,
        "third_key": {
            "1€": "123",
            "2©": "456"
        }
    }
    
    write_order_to_yaml(dictYaml)

    with open('data_write.yaml') as f_n:
        f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)
    print(f_n_content)

def write_order_to_yaml(dictYaml):
    with open('data_write.yaml', 'w') as f_n:
        yaml.dump(dictYaml, f_n, default_flow_style=False, allow_unicode = True, encoding='utf-8')
    f_n.close()

    



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)