# samiro0on             # mahmoudsamir109@gmail.com         # 25/03/2019

def GCD(firstNumber, secondNumber):

    if secondNumber == 0:
        return firstNumber

    return GCD(secondNumber, firstNumber % secondNumber)

def LCM(firstNumber, secondNumber):
    return firstNumber * secondNumber // GCD(firstNumber, secondNumber)

def FabSeq(number):
    if (number < 1):
        return number

    first, second = 0, 1
    for _ in range(number - 1):
        first, second = second, first + second

    return second

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(GCD(a, b))

#28851538 1183019 = 17657

    print(LCM(a,b))

#28851538 1183019 = 1933053046

    print(FabSeq(11))

# FabSeq(11) = 89