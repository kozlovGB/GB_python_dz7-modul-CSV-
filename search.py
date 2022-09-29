import csv
def select_search(Name,path='dict.csv'):#функция выводит интересующий нас критерий из интересующего словаря
    with open(path,encoding='UTF8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            print(row[Name])