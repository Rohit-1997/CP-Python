# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math

def isperfectsquare(n):
	try:
		if n < 0 or int(n) != n:
			return False
		res = math.sqrt(n)
		print("The actual result: ", res)
		return int(res) != res
	except:
		return False

print(isperfectsquare(625))
	