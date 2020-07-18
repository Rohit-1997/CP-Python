# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	low = 0
	high = x

	while low <= high:
		mid = (low + high) / 2
		print("Te mid: ", mid)
		if (mid**2) > x:
			high = mid
		elif (mid**2) < x:
			low = mid
		elif abs((mid**2) - x) <= epsilon:
			print("In here")
			return mid
	return -1

print(findzerowithbisection(81,0.01))

			

