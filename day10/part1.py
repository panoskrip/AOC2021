f = open("input.txt", "r")

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
s = 0
for line in f:
	stack = []
	line = line.strip()
	for c in line:
		#print(stack)
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

print(s)