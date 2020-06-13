import pickle

FILE = "test.txt" #название документа который надо закодировать


def open_file(): #открытие файла
    try:
        file = open(FILE)
        full = file.read()
    finally:
        return full
        file.close()

def probability(text1):#вычисление вероятности встречи симбола в тексте
    lene = len(text1)
    text = text1
    slovar = []
    bykvi = []
    count2=[]
    count = []
    while text:
        bykvi.append(text[0])
        count.append(text.count(text[0]))#цикл по нахождению символов
        text = text.replace(text[0],"")
    print(count, bykvi)



    while count:
        ind = count.index(max(count))
        slovar.append(bykvi[ind])#распределение по числу
        count2.append(count[ind])
        count.pop(ind)
        bykvi.pop(ind)

    #print(count2)

    otrezok = nahojdenie_otrezka(count2)
    #print(otrezok)
    code = codir(text1, otrezok, slovar)
    #otpravka(lene, slovar, otrezok, code)
    return count2

def nahojdenie_otrezka(count):  #включаем наши симболы в один отрезок
    otrezok = [0]
    print(count)
    for i in range(len(count)):
        otrezok.append(otrezok[i]+count[i])

    return otrezok
def BitsPlusFollow(bit):
    global viv
    global bits_to_follow
    viv += str(bit)
    while bits_to_follow > 0:
        bits_to_follow-=1
        if bit:
            viv+='0'
        else:
            viv+='1'

def codir(string, otrezok, bykvi):
    left = 0
    global viv
    global bits_to_follow
    viv = ''
    bits_to_follow = 0
    str= ''
    delitel = otrezok[-1]
    print(bykvi)

    right = 65535
    First_qtr = (right+1)//4
    Half = First_qtr*2
    Third_qtr = First_qtr*3


    for i in range(len(string)):# расчет нового отрезка
        c = string[i]

        ind = bykvi.index(c)
        leftold = left
        rightold = right
        #
        left = leftold + otrezok[ind]*(rightold - leftold + 1)//delitel
        right = leftold + otrezok[ind+1]*(rightold - leftold + 1)//delitel - 1
        print(left, right)
        while True:
            if right<Half:
                BitsPlusFollow(0)
                f = 1
            elif left >= Half:

                BitsPlusFollow(1)
                left -= Half
                right -= Half
            elif (left >= First_qtr) and (right < Third_qtr):
                bits_to_follow+=1
                left -= First_qtr
                right -= First_qtr
            else:
                break
            left+=left
            right+=right+1

    bits_to_follow+=1
    if left<First_qtr:
        BitsPlusFollow(0)
    else:
        BitsPlusFollow(1)
    print(viv)
    otpravka(bykvi, otrezok, viv)
    return 1

def otpravka(bykvi, otrezok, code):# отправка в файл
    lene = len(code)
    n = int(code, 2)
    n = n.to_bytes((n.bit_length() + 7) // 8, 'big')
    print(n)
    with open('FILENAME.bin', "wb") as file:
        pickle.dump(lene, file)# сколько символов было
        pickle.dump(bykvi, file)# какие символы были
        pickle.dump(otrezok, file) #сколько их было
        pickle.dump(n, file) #сами коды


def main():
    string = open_file() #открываем файл
    lene = len(string) #сколько символов всего

    #print(list(string))
    vozmojn = probability(string) #вычисление вероятности встречи симбола в тексте
    """bykvi = [i for i in SetListString]
    otrezok = nahojdenie_otrezka(vozmojn)
    code = (codir(string, otrezok, bykvi))

    otpravka(lene, bykvi, otrezok, code)"""
    #print(vozmojn, set(list(string)))"""


main()
