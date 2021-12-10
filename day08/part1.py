f = open("input.txt", "r")
arr = []

for line in f:
	before, after = line.strip().split(' | ')
	arr += after.split(' ')

c = 0
for digit in arr:
	if (len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
		c += 1

print(c)
