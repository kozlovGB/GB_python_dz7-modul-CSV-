import csv
def read_file(path):
    list=[]
    with open(path,encoding='UTF8') as f:
        reader = csv.DictReader(f,delimiter=' ')
        for row in reader:
            list.append(row)
    return list