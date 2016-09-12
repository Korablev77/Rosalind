try:
	with open('rosalind_revc.txt', 'r') as data_file, open('answer.txt', 'w') as f:
		data = data_file.read()

		ans = ''
		reverse_order  = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
		for letter in data:
			if letter in ['A', 'C', 'T', 'G']:
				ans += reverse_order[letter]

		ans = ans[::-1] 
		f.write(ans)
except IOError as e:
	print('file failed: %s' % e.strerror)





#print(ans+'\n')
#print(''.join(reversed(ans)))
