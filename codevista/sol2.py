test_case = int(input())
input_list = []
for k in range(test_case):
    for l in range(100):
        command = input()
        if command == 'END':
            break
        else:
            input_list.append(command)

sm_num = {"SHOE": 0, "SHIRT": 0}
sm_price = {"SHOE": 0, "SHIRT": 0}
s_num = {"SHOE": 0, "SHIRT": 0}

for i in input_list:

    temp_list = i.split()
    if temp_list[1] == 'SM' and temp_list[2] == 'SET_COST':
        if temp_list[-2] == 'SHOE':
            sm_price["SHOE"] = int(temp_list[-1])
            print(sm_price["SHOE"])
        else:
            sm_price["SHIRT"] = int(temp_list[-1])
            print(sm_price["SHIRT"])
    elif temp_list[1] == "SM" and temp_list[2] == 'ADD':
        if temp_list[-2] == 'SHOE':
            sm_num["SHOE"] += int(temp_list[-1])
            print(sm_num["SHOE"])
        else:
            sm_num["SHIRT"] += int(temp_list[-1])
            print(sm_num["SHIRT"])
    elif temp_list[1] == "SM" and temp_list[2] == 'INCR':
        if temp_list[-2] == 'SHOE':
            sm_num["SHOE"] += int(temp_list[-1])
            print(int(temp_list[-1]))
        else:
            sm_num["SHIRT"] += int(temp_list[-1])
            print(int(temp_list[-1]))
    elif temp_list[1] == "SM" and temp_list[2] == 'DCR':
        if temp_list[-2] == 'SHOE':
            sm_num["SHOE"] -= int(temp_list[-1])
            print(int(temp_list[-1]))
        else:
            sm_num["SHIRT"] -= int(temp_list[-1])
            print(int(temp_list[-1]))
    elif temp_list[1] == "SM" and temp_list[2] == 'GET_QTY':
        if temp_list[-2] == 'SHOE':
            print(sm_num["SHOE"])
        else:
            print(sm_num["SHIRT"])
    elif temp_list[1] == "SM" and temp_list[2] == 'REMOVE':
        if temp_list[-1] == 'SHOE':
            sm_num["SHOE"] = 0
            print("1")
        else:
            sm_num["SHIRT"] = 0
            print("1")

    elif temp_list[1] == "S" and temp_list[2] == 'ADD':
        if temp_list[-2] == 'SHOE':
            s_num["SHOE"] += int(temp_list[-1])
            print(s_num["SHOE"])
        else:
            s_num["SHIRT"] += int(temp_list[-1])
            print(s_num["SHIRT"])
    elif temp_list[1] == "S" and temp_list[2] == 'INCR':
        if temp_list[-2] == 'SHOE':
            s_num["SHOE"] += int(temp_list[-1])
            print(int(temp_list[-1]))
        else:
            s_num["SHIRT"] += int(temp_list[-1])
            print(int(temp_list[-1]))
    elif temp_list[1] == "S" and temp_list[2] == 'DCR':
        if temp_list[-2] == 'SHOE':
            s_num["SHOE"] -= int(temp_list[-1])
            print(int(temp_list[-1]))
        else:
            s_num["SHIRT"] -= int(temp_list[-1])
            print(int(temp_list[-1]))
    elif temp_list[1] == "S" and temp_list[2] == 'REMOVE':
        if temp_list[-1] == 'SHOE':
            s_num["SHOE"] = 0
            print("1")
        else:
            shirt_list_s = 0
            print("1")
    elif temp_list[1] == "S" and temp_list[2] == 'GET_ORDER_AMOUNT':
        print((sm_price["SHOE"]*s_num["SHOE"])+(sm_price["SHIRT"]*s_num["SHIRT"]))
    else:
        print("-1")
