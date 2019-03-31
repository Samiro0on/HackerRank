# Advertisement Revenue # hackerrank
# samiro0on   # mahmoudsamir109@gmail.com       # 28/03/2019


import numpy


def max_dot_product(a, b):
    c = b[::-1]
    res = 0
    for i in range(len(a)):
        res += a[i] * c[i]
    # res = numpy.dot(a, c)
    return res


if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # data = list(map(int, input.split()))
    # n = data[0]
    # a = data[1:(n + 1)]
    # b = data[(n + 1):]

    print(max_dot_product(a, b))

