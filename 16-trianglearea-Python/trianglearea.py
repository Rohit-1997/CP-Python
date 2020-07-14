# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def isValid(s1,s2,s3):
	sides = [s1,s2,s3]
	logest = sides.pop(sides.index(max(sides)))
	return sum(sides) > longest



def trianglearea(s1, s2, s3):
	# your code goes here
	valid = isValid(s1,s2,s3)
	if not valid:
		return 0
	s = (s1 + s2 + s3) / 2
	area = math.sqrt(s * ((s-s1)*(s-s2)*(s-s3)))
	return area

