import pickle

FILE = "FILENAME.bin" # бинарный файл
FILEvivod = "text.txt" # выводимый файл

def viv(text): #функция вывода
    f = open(FILEvivod, 'w')
    f.write(text)
    f.close()

def priem():
    with open(FILE, "rb") as file: #открытие файла
        len = pickle.load(file)
        bykvi = pickle.load(file)
        otrezok = pickle.load(file)
        code = pickle.load(file)
    ll = 0
    for i in otrezok: #я не знаю почему он сам не хочет искать количество, возможных значений
        ll+=1
    vivod = ''
    #print(string)
    for h in code: #берем каждый код
        for i in range(11): #в нем хорошо раскодируются 11 символов
            for j in range(ll):
                if h < otrezok[j]:
                    if j == 0:
                        RangeL = 0
                    else:
                        RangeL = otrezok[j-1]
                    RangeR = otrezok[j]
                    vivod += bykvi[j]
                    break

            h=(h-RangeL)/(RangeR-RangeL) #пересчет отрезка

    return vivod[:len-1]

def main():
    text = priem()
    print(text)
    viv(text)
main()
