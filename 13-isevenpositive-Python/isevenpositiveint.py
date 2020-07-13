# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	if x is None:
		return False
	try:
		if int(x) == x and x%2 == 0 and x >= 0:
			return True
		else:
			return False
	except:
		return False


print(isevenpositiveint(1))
print(isevenpositiveint(-1))
print(isevenpositiveint(-2))
print(isevenpositiveint(-3))
print(isevenpositiveint(2))
print(isevenpositiveint(3))
print(isevenpositiveint(1.0))
print(isevenpositiveint(None))
print(isevenpositiveint((12)))
print(isevenpositiveint([12]))
print(isevenpositiveint(123456))
