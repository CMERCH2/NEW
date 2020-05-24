import pickle
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decode(chislo, lib):
    j = 0
    vivod =''
    for i in range(1, len(chislo)):

        try:
            b = lib[chislo[j:i]]

        except KeyError:
            #print(chislo[j:i])
            o = 1
        else:
            #print(lib[chislo[j:i]])
            vivod += lib[chislo[j:i]]
            j = i
    #print(chislo[j:i])
    return(vivod)
def priem():
    with open('FILENAME.bin', "rb") as file:
        lene = pickle.load(file)
        code = pickle.load(file)
        text = pickle.load(file)
    #print(code, text)
    count = len(code)
    lib = {}
    bytelist = []
    opps = ''
    j = code[0]
    flag = 0

    for i in range(1, count):

        if code[i] not in '01':
            if code[i+1] not in "01":
                flag = 1
                continue
            lib[opps] = j
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

    lib[opps] = j
    #print(lib)
    vivod = ''
    bstring = ''
    for byte in text:
        bytelist.append(byte)
        byte = str(byte)
        bstring += text_to_bits(byte)

    #normaltext = bytes.fromhex(hex(int(text, 2))[2:]).decode(encoding="ascii")
    #print(len(text))
    m = int.from_bytes(text, byteorder ='big')
    print(lib)
    chislo = ''
    while m:
        chislo = str(m%2) + chislo
        m //= 2
    #print(len(chislo))
    chislo = "0"*(lene-len(chislo)) + chislo
    text = decode(chislo, lib)
    return text

        #print(chislo[j:i])
def viv(text):
    f = open('text.txt', 'w')
    f.write(text)
    f.close()

    #print(vivod)
def main():
    text = priem()
    print(text)
    viv(text)




if __name__ == "__main__":
    main()
