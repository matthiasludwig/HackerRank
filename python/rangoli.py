def print_rangoli(size):
	# your code goes here
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	left = alphabet[:size]
	right = list(reversed(left))

	print(left)
	print(right)

	for i in range(n):
		# for j in range(1, n):
		# 	muster = (".|." * i)
		# 	print(muster.center(M, '-'))
		#
		# print("WELCOME".center(M, '-'))
		#
		# for i in range(2, N, 2):
		# 	muster = (".|." * (N - i))
		# 	print(muster.center(M, '-'))


n = int(input())
print_rangoli(n)