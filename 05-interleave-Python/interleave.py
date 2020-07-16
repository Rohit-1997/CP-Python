# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	result = ""
	first = 0
	second = 0
	size_one = len(s1)
	size_two = len(s2)

	while first < size_one and second < size_two:
		result += s1[first]
		first += 1
		result += s2[second]
		second += 1
	
	while first < size_one:
		result += s1[first]
		first += 1

	while second < size_two:
		result += s2[second]
		second += 1
	return result

print(fun_interleave('pto', 'yhn'))