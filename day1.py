
inFile = open('day1.txt', 'r')

total_fuel = 0
for line in inFile:
    line = int(line)
    fuel = line // 3 - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel // 3 -2

print(total_fuel)
