import re

try:
	with open('codon table.txt', 'r') as table, open ('rosalind_prot.txt') as data_file:
		codon_table = table.read()
		res = re.findall(r'\w+', codon_table)
		d = dict(zip(res[::2], res[1::2]))
		#c = dict(res[i:i+2] for i in range(0, len(res), 2))
		data = data_file.read()
		word = ''
		protein = ''
		for letter in data:
			if len(word) == 3:
				protein += d[word]
				word = ''
			word += letter
		print(protein)

except IOError as e:
	print('fail failed %s' %e.strerror)


