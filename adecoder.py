import pickle

FILE = "FILENAME.bin" # бинарный файл
FILEvivod = "text.txt" # выводимый файл

def viv(text): #функция вывода
    f = open(FILEvivod, 'w')
    f.write(text)
    f.close()

def priem():
    with open(FILE, "rb") as file: #открытие файла
        lene = pickle.load(file)
        bykvi = pickle.load(file)
        otrezok = pickle.load(file)
        code = pickle.load(file)
    m = int.from_bytes(code, byteorder ='big')
    chislo = ''
    print(bykvi, otrezok)
    while m:
        chislo = str(m%2) + chislo
        m //= 2
    #print(len(chislo))
    a = (lene-len(chislo))
    chislo = "0"*(a) + chislo
    #print(chislo)
    ll = 0
    for i in otrezok: #я не знаю почему он сам не хочет искать количество, возможных значений
        ll+=1
    vivod = ''
    #print(string)
    #print(chislo)
    value = chislo[:16]
    print(value)
    value = int(value, 2)
    print(value)
    chislo = chislo[16:]
    left = 0
    right = 65535
    delitel = otrezok[-1]
    First_qtr = (right+1)//4
    Half = First_qtr*2
    Third_qtr = First_qtr*3
    a = input()
    while chislo:
        leftold = left
        rightold = right
        freq = ((value - left +1)*delitel-1)//(right - left +1)
        j = 1
        while otrezok[j]<=freq:
            j+=1
        c = bykvi[j]
        print(c)
        left = leftold + otrezok[j]*(rightold - leftold + 1)//delitel
        right = leftold + otrezok[j+1]*(rightold - leftold + 1)//delitel -1
        while True:
            if right <Half:
                f = 1
            elif left>=Half:
                left -= Half
                right -= Half
                value -=Half
            elif (left >= First_qtr) and (right < Third_qtr):
                left -= First_qtr
                right -= First_qtr
                value -= First_qtr
            else:
                break
            left*=2
            right*=2 + 1
            value+=value + int(chislo[0])
            print(value, '\n')
            chislo = chislo[1:]
        vivod+=c
    return vivod

def main():
    text = priem()
    print(text)
    viv(text)
main()
