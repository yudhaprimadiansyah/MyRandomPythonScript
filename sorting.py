data = [4,5,6,1,2,3,11,12,14,13,11]

sort = []

for i in data:
	for a in data:
		if i > a:
			sort.append(i)
		else:
			continue

print sort
