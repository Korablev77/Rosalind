import re

def parse_line(line):
	str_id = 0


	return str_id


try:
	with open('rosalind_gc.txt', 'r') as data_file:
		data_id = 0
		max_rate = 0.001
		max_str  = ''
		GC = 0
		cur_str = ''
		numb_letter = 1

		for line in data_file:
			if line[0] == '>':
				rate = GC / numb_letter
				if rate > max_rate:
					max_str = cur_str
					max_rate = rate
					

				cur_str = line[1:]
				numb_letter = 0
				GC = 0
				continue
			for letter in line:
				if letter == '\n':
					continue
				numb_letter += 1
				if letter in ['G', 'C']:
					GC += 1
		rate = GC / numb_letter
		if rate > max_rate:
			max_str = cur_str
			max_rate = rate
		print(max_str, max_rate)



except IOError as expt:
	print('fail failed: %s' %expt.strerror)