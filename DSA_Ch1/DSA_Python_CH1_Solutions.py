# R-1.1
def is_multiple(n, m):
	''' Validates if first argument is a multiple of second argument'''
	return m%n == 0

# R-1.2
def is_even(k):
	''' Validates if argument is even without the use of multiplication, modulo, or division operators'''
	return str(k)[-1] in ('2','4','6','8','0')
# R-1.3
def minmax(data):
	for i in data:
		for j in range(0,len(data)-1):
			if data[j] >= data[j+1]:
				key = data[j]
				data[j] = data[j+1]
				data[j+1] = key
	return (data[0],data[-1])
# R-1.4
def squaressum(n):
	sqsum=0
	for i in range(1,n):
		sqrd = i/(i**(1/2))
		if i%sqrd==0:
			sqsum += i
	return sqsum
# R-1.5
def squareSum(n):

	return sum(i*i for i in range(1,n))
# R-1.6	
def sumOdd(n):
	total = 0
	for i in range(1,n):
		if i%2>0:
			total += i*i
	return total
# R-1.7 
def sumOdd(n):
	
	return sum((i*i for i in range(1,n,2)))
# R-1.9
def problem_R_1_9():

	return list(range(50,81,10))
# R-1.10
def problem_R_1_10():

	return list(range(8,-9,-2))
# R-1.11
def problem_R_1_11():

	return list(2**i for i in range(0,9))
# R-1.12
def problem_R_1_12():
	import random
	choices=['a','b','c','d','e']
	choice=random.randrange(0,5)
	return choices[choice]
# C-1.13
def reverseOrder(n):
	if type(n) is list:
		for i in range(0,len(n)//2):
			n[i], n[-(i+1)] = n[-(i+1)], n[i]
		return n
	else:
		return "The argument is not of type LIST"
# C-1.14
def findOddPairs(n):
	oddList = []
	oddPairs = []
	if type(n) in (list, tuple):
		try:
			for i in n:
				if i%2>0:
					oddList.append(i)
			for i in range(0,len(oddList)):
				for j in range(i+1,len(oddList)):
					oddPairs.append((oddList[i],oddList[j]))
			return oddPairs
		except:
			return "The elements of the sequence must all be integers."
# C-1.15
def is_set(n):
	# Using built-in methods
	# return n.sort() == list(set(n)).sort()

	# Using my creativity
	mySet = []
	for item in n:
		if item in mySet:
			return False
		else:
			mySet.append(item)
	return True
# C-1.16, C-1.17
def scale(data, factor):
	# This function can only accept mutable data types
	# since the operation multiplies the referenced value.
	for j in data:
		j *= factor
	return data
#C-1.18
def multiplyIndex(n):
	return [i*(i+1) for i in range(n)]
#C-1.19
def alphabet():
	from string import ascii_lowercase as alphabet
	return [letter for letter in alphabet]



def main():
	print(alphabet())


if __name__ == '__main__':
	main()




















