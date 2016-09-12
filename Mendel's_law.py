def prob(n = 0,m = 0,k = 0):
	total = n + m + k
	return (n/total)*((n-1)/(total-1)) + 2*(n/total)*(m/(total-1))*(1/2) + (m/total)*((m-1)/(total-1))*(1/4)


if __name__ == '__main__':
	print(1-prob(25,22,29))