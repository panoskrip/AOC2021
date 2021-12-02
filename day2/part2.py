f = open("input.txt", "r")

horizontal = 0
depth = 0
aim = 0
for line in f:
    line = line.strip()
    direction, number = line.split(' ')
    number = int(number)
    
    if(direction == "forward"):
        horizontal += number
        depth += number*aim
    elif(direction == "down"):
        aim += number
    else:
        aim -= number
    
print(horizontal*depth)