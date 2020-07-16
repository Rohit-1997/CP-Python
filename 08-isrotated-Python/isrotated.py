# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

from collections import defaultdict

def isrotated(str1, str2):
	dict_data = defaultdict(str)
	size = len(str1)
	size_two = len(str2)
	# building the dictionary
	for i in range(size):
		dict_data[str1[i]] = str1[(i+1)%size]

	print(dict_data)

	for i in range(size_two):
		if str2[(i+1)%size_two] != dict_data[str2[i]]:
			return False
	return True




print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA"))