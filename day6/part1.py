f = open("input.txt", "r")

arr = list(map(int, f.readline().split(',')))
eights = []


day = 0
while (day < 80):
    length = len(arr)
    for i in range(length):
        if (arr[i] > 0):
            arr[i] -= 1
        else:
            arr[i] = 6
            arr.append(8)
    
    day += 1


print(len(arr))