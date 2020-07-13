# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	list_data = []
	num = hand
	
	while num != 0:
		list_data.append(num%10)
		num = num//10
	return tuple(list_data)

print(123)
print(214)
print(422)
print(400)
print(101)