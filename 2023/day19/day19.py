import re
import math

with open('day19.txt', 'r') as file:
	lines = [l.strip()  for l in file.readlines()]

parts_map = ['x', 'm', 'a', 's']

rules = {}
parts = []
r = True
for l in lines:
	if l == '':
		r = False
		continue
	if r:
		rp = l.replace("}", "").split("{")
		rules[rp[0]] = rp[1]
	else:
		p = re.findall(r"\d+", l)
		n = re.findall(r"([xmas])+", l)
		assert(n == ['x', 'm', 'a', 's'])
		parts.append(p)
		assert len(p) == 4

def classify_part(part, rule, rule_segment):
	
	if rule == 'A':
		return True
	elif rule == 'R':
		return False
	else:
		rule_content_full = rules[rule]

	rule_segments = rule_content_full.split(",")
	rule_str = rule_segments[rule_segment]
	if ':' in rule_str:
		rule_parts_re = re.compile(r"([a-z]+)([<>]{1})(\d+):([a-z|AR]+)")
		rule_parts_match = rule_parts_re.match(rule_str)
		rule_parts = rule_parts_match.groups()
		
		if eval(part[parts_map.index(rule_parts[0])] + rule_parts[1] + rule_parts[2]):
			return classify_part(part, rule_parts[3], 0)
		else:
			return classify_part(part, rule, rule_segment+1)
	else:
		return classify_part(part, rule_str, 0)

def split_ranges(part_ranges, category_id, comparator, value):
	ret = {True: [[] for i in range(4)], False: [[] for i in range(4)]}
	for range_category_id, ranges in enumerate(part_ranges):
		if range_category_id == category_id:
			# split here
			for r in ranges:
				if r[0]<=value<=r[1]:
					if comparator == '<':
						ret[True][range_category_id].append((r[0], value-1))
						ret[False][range_category_id].append((value, r[1]))
					else:
						ret[False][range_category_id].append((r[0], value))
						ret[True][range_category_id].append((value+1, r[1]))

				elif value>r[1]:
					if comparator == '<':
						ret[True][range_category_id].append((r[0], r[1]))
					else:
						ret[False][range_category_id].append((r[0], r[1]))

				elif value<r[0]:
					if comparator == '<':
						ret[False][range_category_id].append((r[0], r[1]))
					else:
						ret[True][range_category_id].append((r[0], r[1]))
		else:
			# don't split - categories not in rule are added to both True and False
			ret[True][range_category_id] += ranges
			ret[False][range_category_id] += ranges
	return ret[True], ret[False]

def classify_range(part_ranges, rule, rule_segment):
	ret = 0
	
	if rule == 'A':
		tmp = []
		for ranges in part_ranges:
			for r in ranges:
				tmp.append(r[1]-r[0]+1)
		return math.prod(tmp)
	elif rule == 'R':
		return 0
	else:
		rule_content_full = rules[rule]

	rule_segments = rule_content_full.split(",")	
	rule_str = rule_segments[rule_segment]
	if ':' in rule_str:
		rule_parts_re = re.compile(r"([a-z]+)([<>]{1})(\d+):([a-z|AR]+)")
		rule_parts_match = rule_parts_re.match(rule_str)
		rule_parts = rule_parts_match.groups()
		category_id = parts_map.index(rule_parts[0])
		comparator = rule_parts[1]
		value = rule_parts[2]
		if_true = rule_parts[3]

		# split range on parts that satisfy the condition i.e True and ones that don't i.e. False
		part_ranges_true, part_ranges_false = split_ranges(part_ranges, category_id, comparator, int(value))

		# send True range to the defined step
		ret += classify_range(part_ranges_true, if_true, 0)
		
		# send False range to next rule segment in chain
		ret += classify_range(part_ranges_false, rule, rule_segment+1)
	else:
		# send range to "otherwise" rule
		ret += classify_range(part_ranges, rule_str, 0)
	return ret

# 1
ret = 0
for part in parts: 
	if classify_part(part, 'in', 0):
		ret += sum(list(map(int, part)))
print(ret)

# 2
print( classify_range([[(1,4000)],[(1,4000)],[(1,4000)],[(1,4000)]], 'in', 0 ) )