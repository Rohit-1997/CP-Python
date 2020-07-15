# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	number = str(abs(n))
	for i in range(0, len(number) - 1):
		if number[i] == number[i + 1]:
			return True
	return False