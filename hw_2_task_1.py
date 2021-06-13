"""
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. Для этого:
    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
    их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью 
    регулярных выражений извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка
    — например, os_prod_list, os_name_list, os_code_list, os_type_list. 
    В этой же функции создать главный список для хранения данных отчета — например, main_data 
    — и поместить в него названия столбцов отчета в виде списка: 
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
    В этой функции реализовать получение данных через вызов функции get_data(), 
    а также сохранение подготовленных данных в соответствующий CSV-файл;

    Проверить работу программы через вызов функции write_to_csv().
"""

import re
import csv
from pathlib import Path

COUNTFILE = 3

def main():
    file_csv = 'data_csv'
    write_to_csv(file_csv)

def get_data():
    osProdList = []
    osNameList = []
    osCodeList = []
    osTypeList = []
    mainData = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    myself = Path(__file__).resolve()
    sourse = myself.parents[0]
    for count in range(COUNTFILE):
        fileName = 'info_' + str(count+1) + '.txt'
        sourseFile = sourse / fileName
        with open(sourseFile, 'r') as f:
            for line in f:
                if 'Изготовитель ОС:' in line:
                    temp = re.split(':\s+', line)
                    osProdList.append(re.sub("\n",'', temp[1]))
                if 'Название ОС' in line:
                    temp = re.split(':\s+', line)
                    osNameList.append(re.sub("\n",'', temp[1]))
                if 'Код продукта' in line:
                    temp = re.split(':\s+', line)
                    osCodeList.append(re.sub("\n",'', temp[1]))
                if 'Тип системы' in line:
                    temp = re.split(':\s+', line)
                    osTypeList.append(re.sub("\n",'', temp[1]))
        f.close()
    for count in range(len(osProdList)):
        mainData.append([])
        mainData[count+1].append(osProdList[count])
        mainData[count+1].append(osNameList[count])
        mainData[count+1].append(osCodeList[count])
        mainData[count+1].append(osTypeList[count])

    with open('main_data.txt', 'w+') as f:
        for count in range(len(osProdList)+1):
            for item in mainData[count]:
                f.write(item + ' !!!!! ')
            f.write('\n')

    return mainData

def write_to_csv(file_csv):
    file_csv +='.csv'
    print(file_csv)
    mainData = get_data()

    with open(file_csv, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in mainData:
            f_n_writer.writerow(row)
    with open(file_csv) as f_n:
        print(f_n.read())

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)