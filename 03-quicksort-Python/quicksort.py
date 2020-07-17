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
	return p_index



def quicksort_helper(array,low,high):
	if low < high:
		pivot_index = partition(array,low,high)
		quicksort_helper(array,low,pivot_index-1)
		quicksort_helper(array,high,pivot_index+1)


def quicksort(array):
	if array == []:
		return []
	quicksort_helper(array,0,len(array)-1)
	return array
	