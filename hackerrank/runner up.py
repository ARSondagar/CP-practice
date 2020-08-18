if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arr1 = list(dict.fromkeys(arr))
    print(arr1[-2])
