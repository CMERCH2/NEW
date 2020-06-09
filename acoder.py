FILE = "document1.txt"

class Segment:
    left = 0
    right = 0

class SegmentDecode(Segment):
    character = None

def open_file():
    try:
        file = open(FILE)
        full = file.read()
    finally:
        return full
        file.close()

def probability(text, SetListString):
    lenstr = len(text)
    return [text.count(i) / lenstr for i in SetListString]

def codir(count, bykvi):
    otrezok = []
    otrezok.append(count[0])
    for i in range(1, len(count)):
        otrezok.append(otrezok[i-1]+count[i])
    print(count, otrezok)







def main():
    string = "hello world"
    SetListString = set(list(string))
    #print(list(string))
    vozmojn = probability(string, SetListString)
    codir(vozmojn, SetListString)


    #print(vozmojn, set(list(string)))


main()
