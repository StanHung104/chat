

with open('line_r3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		s = line.strip().split(' ')
		time = s[0][:5]
		name = s[0][5:]
		print(time, name)