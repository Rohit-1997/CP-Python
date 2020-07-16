# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	counter = 0
	size_one = len(s1)
	size_two = len(s2)
	result = ""
	
	while counter < size_one:
		if s1[counter] == s2[0]:
			end_index = counter + size_two
			if s1[counter:end_index] == s2:
				result += s3
				counter = end_index
			else:
				result += s1[counter]
				counter += 1
		else:
			result += s1[counter]
			counter += 1
	
	return result

print(fun_replace("helloworld123", "world", "345"))



