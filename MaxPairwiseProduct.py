
def max_pairwise_product(numbers):
    numbers.sort(reverse=True)

    if numbers[0] == numbers[1]:
        numbers.pop(1)

    return numbers[0] * numbers[1]



if __name__ == '__main__':
    inputN = int(input("please enter total number of input ... "))
    inputNumbers = [int(x) for x in input("please enter your numbers separated by space ... ").split()]
    print("max pairwise product is .... ", max_pairwise_product(inputNumbers))
