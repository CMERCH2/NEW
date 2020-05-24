import pickle
import binascii
"""
def text_to_bits(text, encoding='latin-1', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='latin-1', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors)"""

def open_file():
    try:
        file = open("test.txt")
        full = file.read()
        return full
    finally:
        file.close()

def addsymbol(str, number):
    vivod = ''
    b = 0
    if str in '01':
        #print('fd')
        if str == '1':
            #print('fd')
            vivod = 'cc' + number
            return vivod
        return ('ll' + number)

    elif len(str) == 1:
        return (str+number)
    else:

        for i in range(len(str)):

            if str[i] not in "01":
                #print(str[i])
                if str[i+1] not in "01":
                    continue
                vivod += str[b:i+1] + number
                b = i+1
        vivod += str[b:]
        return vivod

def counter(text1):
    text = text1
    """slovar = [0]*256
    for i in range(10,256):
        bits = ''
        b = i
        #print(i)
        for j in range(8):
            bits = str(b%2) + bits
            b //= 2
        #print(bits)
        symbol = text_from_bits(bits)
        #print(symbol)
        gg = text.count(symbol)
        #print(gg)
        slovar[i] = gg
    slovar[0] = 0
    print(slovar)"""
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
        ind = count.index(min(count))
        slovar.append(bykvi[ind])#распределение по числу
        count2.append(count[ind])
        count.pop(ind)
        bykvi.pop(ind)

    kount = len(count2)
    #print(symbols2)
    for i in range(kount-1):
        slovar[1] = addsymbol(slovar[0], '0') + addsymbol(slovar[1], '1')
        #print(symbols2[1])
        slovar = slovar[1:]
        count2[1] = count2[0] + count2[1]
        del count2[0]


        count = count2
        symbols = slovar
        count2 = []
        slovar = []
        for i in range(len(count)):
            a = min(count)
            z = count.index(a)
            count2.append(a)
            slovar.append(symbols[z])
            del count[z]
            symbols = symbols[:z] + symbols[z+1:]
        #print(symbols2, count2)
    #print(symbols, count)
    #print(symbols2, count2)
    symm = slovar[0]
    #print(slovar)
    return symm

"""def tree(slovar):
    def addsymbol(str, number):
        vivod = ''
        b = 0
        if str in '01':
            #print('fd')
            if str == '1':
                #print('fd')
                vivod = 'cc' + number
                return vivod
            return ('ll' + number)

        elif len(str) == 1:
            return (str+number)
        else:

            for i in range(len(str)):

                if str[i] not in "01":
                    #print(str[i])
                    if str[i+1] not in "01":
                        continue
                    vivod += str[b:i+1] + number
                    b = i+1
            vivod += str[b:]
            return vivod
    lib = {}
    for i in range(len(slovar)-1):
        slovar[1] = addsymbol(slovar[0], '0') + addsymbol(slovar[1], '1')
        slovar.pop(0)


    #print(slovar)

    symbols = []
    symbols2 = []
    count = []
    count2 = []
    for i in range(256):
        if slovar[i]!=0:
            bits = ''
            b = i
            #print(i)
            for j in range(8):
                bits = str(b%2) + bits
                b //= 2
            #print(bits)
            symbol = text_from_bits(bits)
            #print(symbol)
            symbols.append(symbol)

            count.append(slovar[i])
    print(symbols)
    for i in range(len(count)):
        a = min(count)
        z = count.index(a)
        count2.append(a)
        symbols2.append(symbols[z])
        del count[z]
        symbols = symbols[:z] + symbols[z+1:]

    kount = len(count2)
    #print(symbols2)
    for i in range(kount-1):
        symbols2[1] = addsymbol(symbols2[0], '0') + addsymbol(symbols2[1], '1')
        #print(symbols2[1])
        symbols2 = symbols2[1:]
        count2[1] = count2[0] + count2[1]
        del count2[0]


        count = count2
        symbols = symbols2
        count2 = []
        symbols2 = []
        for i in range(len(count)):
            a = min(count)
            z = count.index(a)
            count2.append(a)
            symbols2.append(symbols[z])
            del count[z]
            symbols = symbols[:z] + symbols[z+1:]
        #print(symbols2, count2)
    #print(symbols, count)
    #print(symbols2, count2)
    symm = symbols2[0]
    return slovar
"""
def codir(code, text):
    count = len(code)
    lib = {}
    opps = ''
    j = code[0]
    flag = 0
    print(j)
    for i in range(1, count):

        if code[i] not in '01':
            if code[i+1] not in "01":
                flag = 1
                continue
            lib[j] = opps
            opps = ''
            if flag == 1:
                if (code[i]+code[i-1])=='ll':
                    j = '0'
                    flag = 0
                    continue
                else:
                    j = '1'
                    flag = 0
                    continue
            j = code[i]
            continue
        opps += code[i]

    lib[j] = opps
    #print(lib)
    vivod = ''
    for i in text:
        vivod += lib[i]
    #print(vivod)
    return vivod

def otpravka(code, text):
    print(text)
    lene = len(text)
    n = int(text, 2)
    n = n.to_bytes((n.bit_length() + 7) // 8, 'big')
    with open('FILENAME.bin', "wb") as file:
        pickle.dump(lene, file)
        pickle.dump(code, file)
        pickle.dump(n, file)

def main():
    text = open_file()
    slovar = counter(text)
    #print(slovar)
    #code = tree(slovar)
    end = codir(slovar, text)
    otpravka(slovar, end)




if __name__ == "__main__":
    main()
