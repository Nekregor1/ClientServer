"""
Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
    Создать функцию write_order_to_json(), в которую передается 5 параметров 
    — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). 
    Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
    При записи данных указать величину отступа в 4 пробельных символа;

    Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

"""

import json

def main():
    write_order_to_json('мочалка', 5, 100, 'Вова', '2021_06_13')

    with open('order_in_json.json', encoding="utf-8") as f_n:
        print(f_n.read())

def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('order_in_json.json', 'w', encoding="utf-8") as f_n:
        json.dump(dict_to_json, f_n, indent=4, ensure_ascii=False)
    
    

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)
