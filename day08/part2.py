f = open("input.txt", "r")
d = {2: [1], 3: [7], 4: [4], 5: [2,3,5], 6: [0,6,9], 7: [8]}

total = 0
for line in f:
	before, after = line.strip().split(' | ')
	noticed = before.split(' ')
	output = after.split(' ')
	digit = [''] * 7
	digit2 = [''] * 7
	
	noticed.sort(key=len)
	
	for n in noticed:
		arr = [char for char in n]
		couldBe = d[len(arr)]
		for i in couldBe:
			if (i == 1):
				digit[5] += n
				digit[6] += n
			elif (i == 2):
				digit[0] += n
				digit[6] += n
				digit[2] += n
				digit[3] += n
				digit[4] += n
			elif (i == 3):
				digit[0] += n
				digit[6] += n
				digit[2] += n
				digit[5] += n
				digit[4] += n
			elif (i == 4):
				digit[1] += n
				digit[2] += n
				digit[5] += n
				digit[6] += n
			elif (i == 5):
				digit[0] += n
				digit[1] += n
				digit[2] += n
				digit[5] += n
				digit[4] += n
			elif (i == 6):
				digit[0] += n
				digit[1] += n
				digit[2] += n
				digit[3] += n
				digit[5] += n
				digit[4] += n
			elif (i == 7):
				digit[0] += n
				digit[5] += n
				digit[6] += n
			elif (i == 8):
				digit[0] += n
				digit[1] += n
				digit[2] += n
				digit[3] += n
				digit[5] += n
				digit[4] += n
				digit[6] += n
			elif (i == 9):
				digit[0] += n
				digit[1] += n
				digit[2] += n
				digit[5] += n
				digit[4] += n
				digit[6] += n
			else:
				digit[0] += n
				digit[1] += n
				digit[3] += n
				digit[5] += n
				digit[4] += n
				digit[6] += n
		
	arrOfDict = []
	diS = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
	for j in range(len(digit)):
		di = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
		for char in digit[j]:
			di[char] += 1
			diS[char] += 1
			
		arrOfDict.append(di)

	liOfMax = []
	liOfChar = []
	for key in diS:
		liOfMax.append(diS[key])
		liOfChar.append(key)
	
	sortedChar = [x for _,x in sorted(zip(liOfMax,liOfChar), reverse = True)]

	lll = []
	for element in sortedChar:
		maxN = 0
		dictPos = -1
		for ii in range(len(arrOfDict)):
			tempDi = arrOfDict[ii]
			
			if(tempDi[element] > maxN):
				maxN = tempDi[element]
				dictPos = ii

		for el in arrOfDict[dictPos]:
			arrOfDict[dictPos][el] = -1	
		lll.append(dictPos)
	
	for ii in range(len(lll)):
		digit2[lll[ii]] = sortedChar[ii]

	segmentDict = {0: digit2[0], 1: digit2[1], 2: digit2[2], 3: digit2[3], 4: digit2[4], 5: digit2[5], 6: digit2[6],}
	
	mapper = {
		0: digit2[0]+digit2[1]+digit2[3]+digit2[4]+digit2[5]+digit2[6],
		1: digit2[5]+digit2[6],
		2: digit2[0]+digit2[2]+digit2[3]+digit2[4]+digit2[6],
		3: digit2[0]+digit2[2]+digit2[4]+digit2[5]+digit2[6],
		4: digit2[1]+digit2[2]+digit2[5]+digit2[6],
		5: digit2[0]+digit2[1]+digit2[2]+digit2[4]+digit2[5],
		6: digit2[0]+digit2[1]+digit2[2]+digit2[3]+digit2[4]+digit2[5],
		7: digit2[0]+digit2[5]+digit2[6],
		8: digit2[0]+digit2[1]+digit2[2]+digit2[3]+digit2[4]+digit2[5]+digit2[6],
		9: digit2[0]+digit2[1]+digit2[2]+digit2[4]+digit2[5]+digit2[6],
	}

	for i in range(len(output)):
		tempSLi = sorted(output[i])
		s = "".join(tempSLi)
		output[i] = s

	for i in range(10):
		tempSLi = sorted(mapper[i])
		s = "".join(tempSLi)
		mapper[i] = s

	value = ""
	for n in output:
		for i in range(10):
			if (n == mapper[i]):
				value += str(i)

	total += int(value)

print(total)
