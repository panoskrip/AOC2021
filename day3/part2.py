arr, dup = [], []

for line in open("input.txt", "r"):
    arr.append(line.strip())
    dup.append(line.strip())

j = 0
while(True):   
    s = int(sum([1 if i[j] == '1' else -1 for i in arr]))
    cbit = ('1' if s>=0 else '0')

    for i in range(len(arr)):
        byte = arr[i]
        if (byte[j] != cbit):
            arr[i] = 'XXXXXXXXXXXX'
        
    arr = list(filter(('XXXXXXXXXXXX').__ne__, arr))
    
    if(len(arr) == 1): break
    j += 1

o2 = int(arr[0], 2)

j = 0
while(True):
    s = int(sum([1 if i[j] == '1' else -1 for i in dup]))
    cbit = ('1' if s>=0 else '0')

    for i in range(len(dup)):
        byte = dup[i]
        if (byte[j] == cbit):
            dup[i] = 'XXXXXXXXXXXX'
        
    dup = list(filter(('XXXXXXXXXXXX').__ne__, dup))
    
    if(len(dup) == 1): break
    j += 1 

co2 = int(dup[0], 2)

print(o2*co2)