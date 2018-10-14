#!/usr/bin/env python3
import time


class Random(object):
	"""
	Simplified Java SE 6 random number generator.
	Adapted from https://github.com/MostAwesomeDude/java-random
	"""

	def __init__(self, seed=None):
		if seed is None:
			seed = int(time.time() * 1000)
		self.seed = seed

	@property
	def seed(self):
		return self._seed

	@seed.setter
	def seed(self, seed):
		self._seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1)

	def next(self, bits):
		"""
		Generate next random number.
		Method returns an int that is `bits` bits long.
		Each bit is nearly equally likely to be 0 or 1.
		"""

		if bits < 1:
			bits = 1
		elif bits > 32:
			bits = 32

		self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) - 1)
		retval = self._seed >> (48 - bits)

		if retval & (1 << 31):
			retval -= (1 << 32)

		return retval

	def nextInt(self, n=None):
		"""
		Return random int in [0, `n`).
		If `n` is not supplied, random 32-bit int will be returned
		"""
		if n is None:
			return self.next(32)

		if n <= 0:
			raise valueError("Argument must be positive!")

		if not (n & (n - 1)):
			return (n * self.next(31)) >> 31

		bits = self.next(31)
		val = bits % n
		while (bits - val + n - 1) < 0:
			bits = self.next(31)
			val = bits % n

		return val


# To create a test list
# test = Random(5)
# test_list = [test.nextInt(1000) for i in range(10)]
# print(test_list)

rand_num = list(map(int, input().split(' ')))

PRNG_found = False
seed_test = int(time.time() * 1000)

while not PRNG_found:
	PRNG_temp = Random(seed_test)
	numbers_correct = 0

	for i in range(0, 10):
		temp = PRNG_temp.nextInt(1000)
		if temp == rand_num[i]:
			numbers_correct += 1
		else:
			seed_test -= 1
			break

	if numbers_correct == 10:
		PRNG_found = True
		break

print("Seed is ", seed_test)