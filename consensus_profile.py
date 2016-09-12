import re

try:
	with open('rosalind_cons.txt', 'r') as data_file:
		data = data_file.read()
	
		data_str = re.sub('\n', '', data)
		strings = re.split('>Rosalind_\d+', data_str)	
		strings.remove('')	
		
		#print(data_list)
		lenght = len(strings[0])


		profile = {'A': [0]*lenght, 'T': [0]*lenght, 'C':[0]*lenght, 'G':[0]*lenght}

		for str_ in strings:
			i = 0
			for letter in str_:
				profile[letter][i] += 1
				i +=1
		consens = ''

		for i in range(lenght):
			maxL = 'A'
			for letter in profile:
				if profile[letter][i] >  profile[maxL][i]:
					maxL = letter
			consens += maxL				

		print(consens)
		for letter in profile:
			print(letter,':', *profile[letter], sep = ' ')
		
		#print(strings)

except IOError as e:
	print('fail failed %s' %e.strerror)
