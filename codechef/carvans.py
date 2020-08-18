def max_speed(input_list):
    count = 0
    max = input_list[0]
    for j in input_list:
        if j <= max:
            count += 1
            max = j
    print(count)


if __name__ == "__main__":
    test_case = int(input())
    for i in range(test_case):
        car_num = int(input())
        car_max_speed = [int(i) for i in input().split()]
        max_speed(car_max_speed)

