# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")
from collections import defaultdict

def leastfrequentletters(s):
	if s == "":
		return ""
	dict_data = defaultdict(int)		# to store the count

	for ele in s:
		if ((ele >= 'a' and ele <= 'z') or (ele >= 'A' and ele <= 'Z')):
			element = ele.lower()
			# print("The element: ", element)
			dict_data[element] += 1
		
	print('The dict data: ', dict_data)
	if len(dict_data) == 0:
		return ""
	min_value = min(dict_data.values())
	result = []
	for key in dict_data:
		if key != '':
			if dict_data[key] == min_value:
				result.append(key)

	result.sort()
	return "".join(result)

print(leastfrequentletters("aDq efQ? FB'daf!!!"))


