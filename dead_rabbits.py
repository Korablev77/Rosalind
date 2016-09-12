def dead_fib(n, m):
	fib_list = [0, 1, 1]
	for i in range(3,n+1):
		if i - m <=	 0:
			fib_list.append(fib_list[i-1] + fib_list[i-2])
		else:
			fib_list.append(fib_list[i-1] + fib_list[i-2] - fib_list[i-m-1])
	print(fib_list)
	return fib_list[n]


if __name__ == '__main__':
	print(dead_fib(25, 31))
