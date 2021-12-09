f = open("input.txt", "r")

arr = []
for line in f:
    line = line.strip()
    tempArr = []
    for char in line:
        tempArr.append(int(char))
    arr.append(tempArr)

riskLevel = 0
for i in range(len(arr)):

    for j in range(len(arr[i])):
        point = arr[i][j]
        if  (i == 0):
            up = 999
        else:
            up = arr[i-1][j]
        
        if (j == len(arr[i])-1):
            right = 999
        else:
            right = arr[i][j+1]

        if (i == len(arr)-1):
            down = 999
        else:
            down = arr[i+1][j]

        if (j == 0):
            left = 999
        else:
            left = arr[i][j-1]

        if (point < up and point < right and point < down and point < left):
            riskLevel += point+1

        
print(riskLevel)