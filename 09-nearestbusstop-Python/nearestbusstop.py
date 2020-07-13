# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.

import math


def fun_nearestbusstop(street):
	prev_street = int(math.floor(street/8) * 8)
	next_street = prev_street + 8
	first_stop = street - prev_street
	next_stop = next_street - street

	print(prev_street, next_street)
	print(first_stop, next_stop)

	if first_stop <= next_stop:
		return prev_street
	else:
		return next_street

print(fun_nearestbusstop(12))
# print(fun_nearestbusstop(8))
# print(fun_nearestbusstop(13))
# print(fun_nearestbusstop(0))
# print(fun_nearestbusstop(5))
# print(fun_nearestbusstop(16))
# print(fun_nearestbusstop(4))