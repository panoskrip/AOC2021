f = open("input.txt", "r")

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
s = 0
incomplete = []

for line in f:
	prev = s
	stack = []
	line = line.strip()
	for c in line:
		if (c not in points):
			stack.append(c)
			continue

		if (c == ')'):
			if (stack[-1] == '('):
				stack.pop()
			else:
				s += points[c]
				break

		if (c == ']'):
			if (stack[-1] == '['):
				stack.pop()
			else:
				s += points[c]
				break

		if (c == '}'):
			if (stack[-1] == '{'):
				stack.pop()
			else:
				s += points[c]
				break

		if (c == '>'):
			if (stack[-1] == '<'):
				stack.pop()
			else:
				s += points[c]
				break

	if (prev == s):
		incomplete.append(line)

points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
arr = []
for line in incomplete:
	sum = 0
	stack = []
	for c in line:
		if (c not in points):
			stack.append(c)
			continue

		if (c == ')'):
			if (stack[-1] == '('):
				stack.pop()
			
		if (c == ']'):
			if (stack[-1] == '['):
				stack.pop()
			

		if (c == '}'):
			if (stack[-1] == '{'):
				stack.pop()
			
		if (c == '>'):
			if (stack[-1] == '<'):
				stack.pop()
				
	stack.reverse()
	
	for c in stack:
		sum = sum*5 + points2[c]

	arr.append(sum)
		
arr.sort()
length = len(arr)
pointer = length // 2
print(arr[pointer])