#  input

# test_case = int(input())
all_emolpyee = [[1, 2], [1, 2, 1, 5, 2]]
# for i in range(test_case):+
#     num_employee = int(input())
#     arr = [int(i) for i in input().split()]
#     all_emolpyee.append(arr)
# print(test_case)
# print(num_employee)
# print(all_emolpyee)

#  logic
for j in all_emolpyee:
    sum = 0
    temp_list = []
    for m in range(len(j)):
        temp_list.append(m)
    for n in range(len(temp_list)):
        if n == 0:
            if temp_list[n] > temp_list[n+1]:
                sum += 2
            else:
                sum += 1
            print(sum)
        elif n == len(temp_list):
            if temp_list[n] > temp_list[n-1]:
                sum +=  2
            else:
                sum += 1
            print(sum)
        else:
            if temp_list[n] > temp_list[n-1] or temp_list[n] > temp_list[n-1]:
                sum += 2
            else:
                sum += 1
            print(sum)
    print(sum)
    for k in range(len(temp_list)):
        temp_list.remove(k)




