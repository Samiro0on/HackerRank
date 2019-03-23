# samiro0on         # mahmoudsamir109@gmail.com             # 23/03/2019

def reverseChars(inputStr):
    inputList = inputStr.split(" ")
    # print(inputStr)
    outputStr = []
    for items in inputList:
        outputList = []
        for ch in items:
            outputList.append(ch)
        outputList.reverse()
        outputStr.append("".join(outputList))

    outputStr = " ".join(outputStr)
    return outputStr

def mySwapCase(inputStr):
    inputStr = list(inputStr)
    i = 0
    for char in inputStr:
        if char.islower():
            inputStr[i] = char.upper()
        else:
            inputStr[i] = char.lower()
        i+=1
    return ''.join(inputStr)

def stringValidation(inputStr):
    # has any alphanumeric characters
    print(any(char.isalnum() for char in inputStr))
    # has any alphabetical characters
    print(any(char.isalpha() for char in inputStr))
    # has any digits
    print(any(char.isdigit() for char in inputStr))
    # has any lowercase characters
    print(any(char.islower() for char in inputStr))
    # has any uppercase characters
    print(any(char.isupper() for char in inputStr))

def countSubstring(inputString, substring):
    counter = 0
    for index in range(len(inputString) - len(substring) + 1):
        # step = index + len(substring)
        if substring == inputString[index:index + len(substring)]:
            counter += 1

    return counter

import textwrap
def myWrap(line, width):
    paragraph = textwrap.fill(line, width)

    return paragraph


if __name__ == '__main__':

    str1 = input("please enter a sentence ... ")
    out1 = reverseChars(str1)
    print(out1)
    #######################################################
    # if you wanna swap cases using the built in function
    out2 = out1.swapcase()
    print(out2)
    ########################################################
    # if you wanna swap cases using my implementation
    out3 = mySwapCase(out1)
    print(out3)
    ########################################################
    stringValidation(out1)
    ########################################################
    string = input("please enter your string ... ")
    # .strip()        # if you want to remove the white spaces from the line 
    sub_string = input("you wanna search for ... ")
    # .strip()       # # if you want to remove the white spaces from the line 

    counter = countSubstring(string, sub_string)
    print("that sub string occur ", counter, " times")

    
