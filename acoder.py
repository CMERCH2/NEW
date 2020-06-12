import pickle

FILE = "document1.txt" #название документа который надо закодировать

def open_file(): #открытие файла
    try:
        file = open(FILE)
        full = file.read()
    finally:
        return full
        file.close()

def probability(text, SetListString):#вычисление вероятности встречи симбола в тексте
    lenstr = len(text)
    return [text.count(i) / lenstr for i in SetListString]

def nahojdenie_otrezka(count):  #включаем наши симболы в один отрезок
    otrezok = []
    otrezok.append(count[0])
    for i in range(1, len(count)):
        otrezok.append(otrezok[i-1]+count[i])
    otrezok[len(count)-1] = 1
    return otrezok

def codir(string, otrezok, bykvi):
    ind = bykvi.index(string[0])#####кодируем выбранный отрезок

    granici = [0, 0] #границы закодированного отрезка
    if ind == 0:
        granici[0] = 0
    else:
        granici[0] = otrezok[ind-1]
    granici[1] = otrezok[ind]

    for i in range(1, len(string)):# расчет нового отрезка
        leftOLD = granici[0]
        rightOLD = granici[1]

        ind = bykvi.index(string[i])
        if ind == 0:
            RangeL = 0
        else:
            RangeL = otrezok[ind-1]
        RangeR = otrezok[ind]
        granici[0] = leftOLD+(rightOLD-leftOLD)*RangeL
        granici[1] = leftOLD+(rightOLD-leftOLD)*RangeR

    return granici[0]

def otpravka(len, bykvi, otrezok, code):# отправка в файл
    with open('FILENAME.bin', "wb") as file:
        pickle.dump(len, file)# сколько символов было
        pickle.dump(bykvi, file)# какие символы были
        pickle.dump(otrezok, file) #сколько их было
        pickle.dump(code, file) #сами коды


def main():
    string = open_file() #открываем файл
    lene = len(string) #сколько символов всего
    SetListString = set(list(string)) #какие символы в тексте
    #print(list(string))
    vozmojn = probability(string, SetListString) #вычисление вероятности встречи симбола в тексте
    bykvi = [i for i in SetListString]
    otrezok = nahojdenie_otrezka(vozmojn)
    code = []
    j = 0 #так как в конце каждой раскодируемой строки вызодит всякая фигня
    i = 0 #я перекодирую последние 2 симбола
    str = string[:13]
    while str:
        j+=2
        i+=1
        code.append(codir(str, otrezok, bykvi)) #добавление кода в семейство кодов
        str = string[i*13-j:(i+1)*13-j]

    otpravka(lene, bykvi, otrezok, code)
    #print(vozmojn, set(list(string)))


main()
