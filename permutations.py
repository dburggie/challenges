

# enumerate all 9 digit numbers with each digit 1 to 9 exactly once
# 123456789
# 123456798
# ...
# 987654312
# 987654321

def getDigitPermutations():
	print "calculating permutations on 9 digits..."
	digits = []
	A = range(1,10)
	for a in A:
		B = A[:]
		B.remove(a)
		for b in B:
			C = B[:]
			C.remove(b)
			for c in C:
				D = C[:]
				D.remove(c)
				for d in D:
					E = D[:]
					E.remove(d)
					for e in E:
						F = E[:]
						F.remove(e)
						for f in F:
							G = F[:]
							G.remove(f)
							for g in G:
								H = G[:]
								H.remove(g)
								value = a * 10 ** 8
								value += b * 10 ** 7
								value += c * 10 ** 6
								value += d * 10 ** 5
								value += e * 10 ** 4
								value += f * 10 ** 3
								value += g * 10 ** 2
								digits.append(value + H[0] * 10 + H[1])
								digits.append(value + H[1] * 10 + H[0])
	print "all permutations found"
	return digits

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
		43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
		103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
		173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
		241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
		317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
		401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
		479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
		571, 577, 587, 593, 599, 601, 607]

def getHighestPrimeFactor(n):
	highest = 2
	for p in primes:
		if n % p == 0:
			highest = p
	if n > highest:
		highest = max(highest, getHighestPrimeFactor(n / highest))
	return highest


def getFactors(n, factors):
	if n == 1:
		return factors
	for p in primes:
		if n % p == 0:
			factors.append(p)
			return getFactors(n / p, factors)
	factors.append(n)
	return factors





perms = getDigitPermutations()

numbers = []
factorizations = []
lowest = 10 ** 10

print ""
print "finding lowest largest prime factor among permutations..."

for n in perms:
	factors = getFactors(n, [])
	largest = factors[-1]
	if largest == lowest:
		numbers.append(n)
		factorizations.append(factors)
	elif largest < lowest:
		lowest = largest
		factorizations = [factors]
		numbers = [n]
		
print "lowest largest factor was", lowest

print "this factor was found in the following number(s)"
for i in range(len(numbers)):
	print "    ", numbers[i], "with factors",
	for n in factorizations[i]:
		print n,
	print




