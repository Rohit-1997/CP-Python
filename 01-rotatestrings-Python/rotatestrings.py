# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def fun_rotatestrings(s, n):
	if n == 0:
		return s
	size = len(s)
	aux_x = ['']*size
	print(aux_x)

	if abs(n) == n:
		print("In here")
		for i in range(size):
			index = (i-n) % size
			print(index)
			aux_x[index] = s[i]
		print(aux_x)
		return "".join(aux_x)
	else:
		for i in range(size):
			index = (i+abs(n)) % size
			print(index)
			aux_x[index] = s[i]
		return "".join(aux_x)

print(fun_rotatestrings('abcd', -1))


