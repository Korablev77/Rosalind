import re
#import inspect

def find_pattern(main_str, sub_str):
	start = 0
	while True:
		start = main_str.find(sub_str, start+1)
		if start > 0:
			print(start+1)
		else: return

def find_substr(t, s):
	return [m.start() for m in re.finditer('(?=%s)' %s, t)]


try:
	with open('rosalind_subs.txt', 'r') as data_file:
		#data = data_file.read()
		#main_str = 'CACTTGCATCCACTTGCACCACTTGCGCACTTGCCGCACTTGCCGTGTTATTACCCACTTGCTTCTTAAGAGCACTTGCCACTTGCGACACTTGCGCACACTTGCAAGTACTCCCACCACTTGCACTCACTTGCCACTTGCTGACACTTGCTTATCACTTGCTCACTTGCTTTCACTTGCCCGCACTTGCTTAGCACTTGCCACTTGCCCACTTGCCGCACTTGCCACTTGCCCACTTGCGGGCACTTGCCAGCACTTGCTCACTTGCTAAACTTGTTACACTTGCCACTTGCCCACTTGCGGTCACTTGCCGCAGCACTTGCACGGTGGATCACTTGCGTCCACTTGCGGATCACTTGCCACTTGCCAAAAATTCACTTGCCTGGACTCTCACTTGCCACTTGCGGCACACTTGCGCACTTGCTAGGACACTTGCCTGCACTTGCTTCGCCTTTTCACTTGCGTTGTCACTTGCTCACTTGCGCACTTGCCACTTGCCACTTGCAACCCACTTGCTCACTTGCTATCACTTGCTTTAGAAATTGACACTTGCAAAACACTTGCCACTTGCTGATCACTTGCCACTTGCCTGCACTTGCCTCCACTTGCGTTTCACTTGCCACTTGCTGACCACTTGCGGTGCACTTGCTAACACTTGCCGAGATATGCTCACTTGCGTGGACATCACTTGCAGCACTTGCCACTTGCGACTAGCAACACTTGCACACTTGCCACTTGCCACTTGCCAGGCACTTGCGGAACACTTGCCCACTTGCGCACTTGCAAAAGCACTTGCGCCTATGAGGACACTTGCAGAAACTTCCCACTTGCCACACTTGCTGCACTTGCCACTTGCTTCACTTGCACACTTGCTCACTTGCCCCACTTGCGGTCACTTGCACGCCGACACTTGCACACTTGCCCCACTTGC'
		#sub_str  = 'CACTTGCCA'

		#print(main_str, sub_str)

		#matches = re.finditer(sub_str, main_str, overlapped = True)
		#print(mathces)


		#find_pattern(main_str, sub_str)

		s1,s2 = data_file.read().split()

		locs = find_substr(s1,s2)
		print(locs)

		#for i in range(len(main_str)):
		#	if main_str[i:].startswith(sub_str):
		#		print(i+1)


		#pattern = re.compile(sub_str)
		#for m in pattern.finditer(main_str):
		#	print(m.start(), m.group())

		#print(inspect.getsourcelines(re.finditer))

		#for match in re.finditer(sub_str, main_str):
		#	print(match.span())

except IOError as e:
	print('fail failed %s' %e.strerror)