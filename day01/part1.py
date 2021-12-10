f = open("input.txt", "r")

depths = []
for line in f:
    depths.append(int(line.strip()))

no = 0
for i in range(1, len(depths)):
    if(depths[i] > depths[i-1]):
        no += 1

print(no)

# One liner attempt
print(sum(depths[i+1] > depths[i] for i in range(len(depths)-1)))