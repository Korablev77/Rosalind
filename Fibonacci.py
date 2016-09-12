n = 34
k = 4

def k_fibonacci(n, k):
	if n == 1 or n == 2:
		return 1
	return k_fibonacci(n-1, k) + k*k_fibonacci(n-2,k)

print(k_fibonacci(n,k))