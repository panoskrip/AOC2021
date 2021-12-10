f = open("input.txt", "r")

arr = list(map(int, f.readline().split(',')))

count = [0] * 9
for i in arr:
    count[i] += 1

for day in range(256):
    n0 = count.pop(0)
    count[6] += n0
    count.append(n0)

print(sum(count))