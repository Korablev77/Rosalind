with open('rosalind_dna.txt', 'r') as data_file:
	read_data = data_file.read()
	data_ans = {'A':0, 'C':0, 'T':0, 'G':0}
	for letter in read_data:
		#print(letter)
		if letter  in ['A','C','T','G']: 
			data_ans[letter] += 1

#how to print in the correct order?
for let,value in data_ans.items():
	print(let,value)