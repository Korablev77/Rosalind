try:
	with open('rosalind_hamm.txt', 'r') as data_file:
		mutations = 0
		str1 = data_file.readline()
		str2 = data_file.readline()
		for let1, let2 in zip(str1, str2):
			if let1 != let2:
				mutations += 1
		print(mutations)
except IOError as e:
	print('cant open file %s'% e.strerror)

print(list(zip(str1, str2)))