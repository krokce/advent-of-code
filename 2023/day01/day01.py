with open('day01.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

# 1
res = 0
for l in lines:
	numbers = ''
	for char in l:
		if char.isdigit():
			numbers += char
	res += int(numbers[0] + numbers[-1])
print(res)

# 2
res = 0
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for l in lines:
	numbers = ''
	for char_position, char in enumerate(l):
		if char.isdigit():
			numbers += char
		for word_position, word in enumerate(words):
			if word == l[char_position:char_position + len(word)]:
				numbers += str(word_position + 1)
	res += int(numbers[0] + numbers[-1])
print(res)
