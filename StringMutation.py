
def mutateString(inputString, index, char):
    # inputString = inputString[:index] + char + inputString[index+1:]

    stringList = list(inputString)
    stringList[index] = char
    inputString = ''.join(stringList)

    return inputString


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutateString(s, int(i), c)
    print(s_new)