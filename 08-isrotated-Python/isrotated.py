# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	size = len(str1)
	list_data = ['']*size

	for i in range(size):
		index = (i + 1) % size
		list_data[index] = str1[i]

	rotated_string = "".join(list_data)
	return rotated_string == str2


print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA"))