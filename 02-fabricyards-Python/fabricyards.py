# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!
import math

def fun_fabricyards(inches):
	# your code goes here
	if inches == 0:
		return 0
	res = inches / 36
	return int(math.ceil(res))

def fun_fabricexcess(inches):
	# your code goes here
	if inches == 0:
		return 0
	res = fun_fabricyards(inches)
	return (36*res) - inches

print(fun_fabricexcess(0))
print(fun_fabricexcess(1))
print(fun_fabricexcess(35))
print(fun_fabricexcess(36))
print(fun_fabricexcess(37))
print(fun_fabricexcess(38))
print(fun_fabricexcess(72))
print(fun_fabricexcess(73))


