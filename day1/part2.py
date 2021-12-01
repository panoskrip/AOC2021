f = open("input.txt", "r")

depths = []
for line in f:
    depths.append(int(line.strip()))

no = 0
for i in range(1, len(depths)):
    try:
        if(depths[i]+depths[i+1]+depths[i+2] > depths[i-1]+depths[i]+depths[i+1]):
            no += 1
    except:
        print(no)
        break
