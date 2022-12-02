with open('day01.txt', 'r') as file:
	elves = [sum([int(weight) for weight in elf.split("\n") if len(weight)>0]) for elf in file.read().split("\n\n")]

#1
print(sorted(elves)[-1])

#2
print(sum(sorted(elves)[-3:]))
