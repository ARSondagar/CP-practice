num_of_train = int(input())
arrival = []
departure = []
for k in range(num_of_train):
    x = input()
    arrival.append(int(x.split()[0]))
    departure.append(int(x.split()[1])+int(x.split()[0]))

if len(arrival) != len(departure):
    print("plz..give right information")    # Sort both the lists.
arrival.sort()
departure.sort()

platform_required = 1  # Count of platforms required at the moment when comparing i^th arrival and j^th departure
max_platform_required = 1  # Keep track of the max value of platform_required

i = 1
j = 0
while i < len(arrival) and j < len(arrival):
    if arrival[i] <= departure[j]:
        platform_required += 1
        i += 1
        if platform_required > max_platform_required:
            max_platform_required = platform_required

    else:
        platform_required -= 1
        j += 1
print(max_platform_required)
