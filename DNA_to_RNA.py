with open('rosalind_rna.txt', 'r') as data_file:
	data = data_file.read()
	ans = ''
	for letter in data:
		if letter == 'T':
			ans += 'U'
		else:
			ans += letter
		#print(letter)

	print(ans)