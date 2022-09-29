from read import *


def pull_line(key,value,path='text.csv'):
    data=read_file(path)
    try:
        return [line for line in data if line[key]==value]
    except:
        print['No key']


def dict_search(Name,key,value,path='text.csv'):
    data=pull_line(key,value,path)
    print(data)
    with open(Name, 'w',encoding='UTF8') as f:
        writer = csv.DictWriter(f,  fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)

