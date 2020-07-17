"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array,low,high):
	pivot = array[high]
	p_index = low

	for i in range(low,high):
		if array[i] <= pivot:
			temp = array[p_index]
			array[p_index] = array[i]
			array[i] = temp
			p_index += 1
	print('The array after partition: ', array)

	# swapping the last element
	temp = array[p_index]
	array[p_index] = pivot
	array[high] = temp
	return p_index


def quicksort_helper(array,low,high):
	if low < high:
		pivot_index = partition(array,low,high)
		print(pivot_index)
		quicksort_helper(array,low,pivot_index-1)
		quicksort_helper(array,high,pivot_index+1)


def quicksort(array):
	if array == []:
		return []
	quicksort_helper(array,0,len(array)-1)
	return array

print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
	