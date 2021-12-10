f = open("input.txt", "r")

arr = [[0 for i in range(1000)] for j in range(1000)]

for line in f:
    line = line.strip()
    x1, rest, y2 = line.split(',')
    y1, x2 = rest.split('->')
    x1 = int(x1.strip())
    x2 = int(x2.strip())
    y1 = int(y1.strip())
    y2 = int(y2.strip())
    
    if (x1 == x2):
        length = abs(y2-y1) + 1
        for i in range(length):
            if(y1 >= y2):
                arr[y1-i][x1] += 1
            else:
                arr[y2-i][x1] += 1

    elif (y1 == y2):
        length = abs(x2-x1) + 1
        for i in range(length):
            if(x1 >= x2):
                arr[y1][x1-i] += 1
            else:               
                arr[y1][x2-i] += 1
        
    else:
        length = abs(x2-x1) + 1
        for i in range(length):
            if (x1 >= x2):
                if (y1 >= y2):
                    pointX = x1 - i
                    pointY = y1 - i
                    arr[pointY][pointX] += 1
                else:
                    pointX = x1 - i
                    pointY = y1 + i
                    arr[pointY][pointX] += 1
            else:
                if (y1 >= y2):
                    pointX = x1 + i
                    pointY = y1 - i
                    arr[pointY][pointX] += 1
                else:
                    pointX = x1 + i 
                    pointY = y1 + i
                    arr[pointY][pointX] += 1
        
s = 0  
for line in arr:
    for point in line:
        if (point >= 2):
            s += 1

print(s) 