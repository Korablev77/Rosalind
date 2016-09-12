import re

def isFloat(num):
	return float(num)

try:
	with open('mass table.txt','r') as mass, open('rosalind_prtm.txt', 'r') as data_file:
		table = mass.read()
		t = re.findall(r'\S+', table)
		#print(t)

		#for i in range(len(t)):
			#t[i] = float(t[i])
		masses = dict(zip(t[::2], map(float,t[1::2])))
		#masses = [(x,y) for x in t[::2] for y in t[1::2]]

		#for i in masses:
		#masses[i] = float(masses[i])
		data = data_file.read()
		total_mass = 0
		for letter in data:
			total_mass += masses[letter]
		#print(masses)
		print(total_mass)

except IOError as e:
	print('fail failed %s' %e.strerror)