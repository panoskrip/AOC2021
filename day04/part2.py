def bingoCheck(board):
    for i in range(len(board)):
        cH = 0
        cV = 0
        for j in range(len(board[i])):
            if(board[i][j] == 'X'):
                cH += 1
            if(board[j][i] == 'X'):
                cV += 1
        if (cH == 5 or cV == 5):
            return True
    return False



f = open("input.txt", "r")

draw = f.readline().strip().split(',')

arr = []
box = []

for line in f:   
    line = line.strip()
    if (line):
        split = line.split(' ')
        split = [item for item in split if item != '']
        box.append(split)
    else:
        if (len(box) != 0):
            arr.append(box)
            box = []



c = 0
flag = False
for n in draw:
    c += 1
    if(not flag):
        for i in range(len(arr)):
            if(not flag):
                for j in range(len(arr[i])):
                    if(not flag):
                        try:
                            for k in range(len(arr[i][j])):
                                if (arr[i][j][k] == n):
                                    arr[i][j][k] = 'X'
                        except:
                            break
                        if (c >=5):
                            if(bingoCheck(arr[i])):
                                
                                arr[i] = 'X'
                                if(len(list(filter(('X').__ne__, arr))) == 1):
                                    key = n
                                    flag = True                                    
                                    break


arr = list(filter(('X').__ne__, arr))                              

drawIndex = draw.index(key)

#print(arr)

flag = False
for n in range(drawIndex, len(draw)): 
    if(not flag):
        for ii in range(len(arr[0])):
            if(not flag):
                for jj in range(len(arr[0][ii])):
                    if(arr[0][ii][jj] == draw[n]):
                        arr[0][ii][jj] = 'X'
                
                if(bingoCheck(arr[0])):
                    sum = 0
                    for row in arr[0]:
                        for no in row:
                            if (no != 'X'):
                                sum += int(no)
                    print(sum * int(draw[n]))
                    flag = True
                    break

