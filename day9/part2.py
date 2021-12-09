f = open("test.txt", "r")

arr = []
for line in f:
	line = line.strip()
	temparr = []
	for c in line:
		temparr.append(int(c))
	arr.append(temparr)

s = 0
points = []
for i in range(len(arr)):

	for j in range(len(arr[i])):
		point = arr[i][j]
		if (i != 0):
			up = arr[i-1][j]
		else:
			up = 999
		
		if (j != len(arr[i])-1):
			right = arr[i][j+1]
		else:
			right = 999

		if (i != len(arr)-1):
			down = arr[i+1][j]
		else:
			down = 999

		if (j != 0):
			left = arr[i][j-1]
		else:
			left = 999

		if (point < up and point < right and point < down and point < left):
			s += point+1
			points.append([i,j])

#print(s)

# PART 2
def checkPoint(arr, i, j, s):
	point = arr[i][j]
	if (i != 0):
		up = arr[i-1][j]
		ij = [i,j]
		if (up - point == 1 and up != 9):
			s += 1
			print(i, j)
			print('Went up')
			return checkPoint(arr, i-1, j, s)
	else:
		up = 999
	
	if (j != len(arr[i])-1):
		right = arr[i][j+1]
		if (right - point == 1 and right != 9):
			s += 1
			print(i, j)
			print('Went right')
			return checkPoint(arr, i, j+1, s)
	else:
		right = 999

	if (i != len(arr)-1):
		down = arr[i+1][j]
		if (down - point == 1 and down != 9):
			s += 1
			print(i, j)
			print('Went down')
			return checkPoint(arr, i+1, j, s)
	else:
		down = 999

	if (j != 0):
		left = arr[i][j-1]
		if (left - point == 1 and left != 9):
			s += 1
			print(i, j)
			print('Went left')
			return checkPoint(arr, i, j-1, s)
        	
            
	else:
		left = 999

	return s


s = 0
k=0
for ij in points:
	if (k==1):
		i = ij[0]
		j = ij[1]
		print('next')
		print(checkPoint(arr, i, j, s)+1)
		break
	k += 1
    
	
