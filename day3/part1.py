f = open("input.txt", "r")


li = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0]
for line in f:
	i = 0
	line = line.strip()
	for bit in line:
		if (bit == '0'):
			li[i] += 1
		else:
			li[i+1] += 1
		i += 2

g = ""

for i in range(len(li)):	
	try:
		if (i % 2 == 0):
			if li[i] > li[i+1]:
				g += '0'
			else:
				g += '1'
			print(i)
		
	except:
		break

print(g)
gli = [char for char in g]
print(gli)

e = ""
for bit in gli:
	if (bit == '0'):
		e += '1'
	else:
		e += '0'

gInt = int(g, 2)
eInt = int(e, 2)
print(gInt * eInt)
