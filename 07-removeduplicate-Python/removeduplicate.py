# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	list_data = []
	for char in text:
		if char not in list_data:
			list_data.append(char)
	print(list_data)
	return "".join(list_data)
	
# print(removeduplicate('HelloWorld'))
# print(removeduplicate('EEE'))
print(removeduplicate('a a'))
