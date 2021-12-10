f = open("input.txt", "r")

directions = {"forward":0, "down":0, "up":0}

for line in f:
    line = line.strip()
    direction, number = line.split(' ')
    number = int(number)
    directions[direction] += number
    
horizontal = directions["forward"]
depth = directions["down"] - directions["up"]

print (horizontal*depth)