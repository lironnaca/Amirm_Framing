if __name__ == '__main__':
    f = open("finalPos.txt", "r")
    a = f.read().split("\n")
    b = []
    for index, sen in enumerate(a):
        if index == len(a) - 1:
            break
        if index == 0:
            continue
        elif 49 <= ord(sen[0]) <= 57:
            b.append(sen[3:])
        elif sen[0] == '-':
            b.append(sen[2:])
        else:
            b.append(sen)
    f.close()
    f = open("finalPosPreProcc.txt", "a")
    for sen in b:
        f.write(sen + "\n")
