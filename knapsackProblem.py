

if __name__ == "__main__":
    n, capacity = map(int, input().split())
    data = []

    for _ in range(n):
        data.append(list(map(int, input().split())))
    print(n, capacity, " data .. ", data)

    # for rec in data:
    #     if rec

    # treasure , weight
    candidate = []
    for record in data:
        if record[1] <= capacity:
            # max1 = 0
            # max2 = record[1]
            candidate.append(record)
    # print(candidate)

    if len(candidate) == 0:
        hugeOutput = max(data)
        factor = capacity / hugeOutput[1]
        total = hugeOutput[0] * factor
        print(total)

    else:
        newCandidate = []
        for record in candidate:
            temp = record[1]
            for i in range(len(candidate)-1):
                if (temp + candidate[i][1]) <= capacity | temp == capacity:
                    # newCandidate.append(record)
                    newCandidate.append(candidate[i])
        # print(newCandidate)

        for i in range(len(newCandidate)-1):
            if newCandidate[0] == newCandidate[i+1]:
                newCandidate.pop(0)

        # print(newCandidate)

        total = 0
        for records in newCandidate:
            total = total + records[0]

        print(total)

    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # opt_value = get_optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))
