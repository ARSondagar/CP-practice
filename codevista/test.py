inp = input()
testCase = int(inp)
while testCase > 0:
    noInp = input()
    n = int(noInp)
    # for i in range(n):
    rankInp = input()
    rankOfEmp = rankInp.split()
    # rankOfEmp.sort()
    max = len(rankOfEmp)

    giftOfEmp = [1 for i in range(max)]
    rankOfEmp.insert(0,0)
    rankOfEmp.append(0)
    giftOfEmp.insert(0, 0)
    giftOfEmp.append(0)
    # print(rankOfEmp)
    # print(giftOfEmp)
    for i in range(1, len(rankOfEmp)-1):
        # print( int(rankOfEmp[i]) , int(rankOfEmp[i-1]))
        if int(rankOfEmp[i]) > int(rankOfEmp[i-1]):
            # print(giftOfEmp[i] , giftOfEmp[i-1])
            if(giftOfEmp[i] <= giftOfEmp[i-1]):
                giftOfEmp[i] += 1
                max += 1
                # print(giftOfEmp,"0")
                # print("1")
                if (giftOfEmp[i] == giftOfEmp[i - 1]):
                    # print(giftOfEmp[i] , giftOfEmp[i - 1])
                    # print(int(rankOfEmp[i]) , int(rankOfEmp[i - 1]))
                    if (int(rankOfEmp[i]) > int(rankOfEmp[i - 1])):
                        giftOfEmp[i] += 1
                        max += 1
                        # print(giftOfEmp, "2")

        if int(rankOfEmp[i]) > int(rankOfEmp[i + 1]):
            # print(giftOfEmp[i] , giftOfEmp[i + 1])
            if (giftOfEmp[i] <= giftOfEmp[i + 1]):
                giftOfEmp[i] += 1
                max += 1
                # print(giftOfEmp, "1")
                # print("2")

    print(max)
    testCase -= 1
