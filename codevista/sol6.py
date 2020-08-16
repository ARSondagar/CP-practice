total_fighter = int(input())
coins_input = input()
value_coins = coins_input.split()
sum = 0
for i in range(total_fighter):
    if len(value_coins) > 2:
            value_coins.sort()
            sum += int(value_coins[-1])*int(value_coins[-2]) + int(value_coins[-3])
            value_coins.remove(value_coins[-2])
    elif len(value_coins) == 2:
            value_coins.sort()
            sum += int(value_coins[0])*int(value_coins[1])
            value_coins.remove(value_coins[0])
    else:
            sum += int(value_coins[0])
print(sum)

