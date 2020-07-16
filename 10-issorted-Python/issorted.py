# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	asc_falg = False
	desc_flag = False

	for i in range(len(a) - 1):
		if a[i] > a[i+1]:
			asc_falg = True
			break
	
	if asc_falg:
		return False

	if not asc_falg:
		return True

	for i in range(len(a) - 1):
		if a[i] < a[i+1]:
			desc_flag = True
			break
	if desc_flag:
		return False
	return True

print(issorted([5,4,3,2,1]))