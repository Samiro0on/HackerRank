# samiro0on         # mahmoudsamir109@gmail.com             # 23/03/2019

import textwrap

def myWrap(line, width):
    paragraph = textwrap.fill(line, width)
    return paragraph


if __name__ == '__main__':

    givenLine, newWidth = input(), int(input())
    output = myWrap(givenLine, newWidth)
    print(output)
