# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	if len(p1) >= len(p2):
		p1_size = len(p1)
		p2_size = len(p2)
	else:
		p1_size = len(p2)
		p2_size = len(p1)

	result = [0] * (p1_size + p2_size - 1)

	for i in range(p1_size):
		for j in range(p2_size):
			result[i+j] += p1[i] + p2[j]
	return result





