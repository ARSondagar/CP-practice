def med(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ret_value = arr[int((len(arr)-1)/2)]
    else:
        ret_value = 0.5*(arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])
    return ret_value


N = int(input().strip())

digit = [int(i) for i in input().strip().split(' ')]
freq = [int(j) for j in input().strip().split(' ')]
x_arr = list()
for m in range(N):
    x_arr += [digit[m]] * freq[m]
Q2 = med(x_arr)

l_arr = [i for i in x_arr if i < Q2]
u_arr = [i for i in x_arr if i > Q2]

Q1 = med(l_arr)
Q3 = med(u_arr)

print(int(Q3 - Q1))
