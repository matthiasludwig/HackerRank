#!/bin/python3

if __name__ == '__main__':
	n = int(input())
	b = "{0:b}".format(n)

	counter = 0
	max_count = 0
	found = False

	for i in range(len(b)):
		if b[i] == '1':
			counter += 1
			found = True
			if counter > max_count:
				max_count = counter
		else:
			found = False
			counter = 0

	print(max_count)