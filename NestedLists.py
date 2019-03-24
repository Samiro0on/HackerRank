# samiro0on         # mahmoudsamir109@gmail.com             # 24/03/2019
if __name__ == '__main__':
    list1 = []
    for _ in range(int(input("please enter total number of students ..... "))):
        name = input("std name is : ")
        score = float(input("score : "))
        list1.append([score, name])
    list1.sort()
    lowest = list1[0]
    # remove the lowest score
    while True:
        if (list1[0][0] == lowest[0]):
            list1.remove(list1[0])
        else:
            break

    second_lowest = list1[0]
    final_l = []
    for i in range(len(list1)):
        if (second_lowest[0] == list1[i][0]):
            final_l.append(list1[i][1])
            # sort the output alpha order
    final_l.sort()
    for i in range(len(final_l)):
        print(final_l[i])