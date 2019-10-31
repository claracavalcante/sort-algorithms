import math

def mergeSort(arr):
	array_len = len(arr)

	#Not using sort() method. I wanted to make the process clearer.
	if (array_len == 2):
		if arr[0] > arr[1]:
			arr[0], arr[1] = arr[1], arr[0]
		return arr
	
	if array_len == 1:
		return arr

	mid = array_len // 2
	left = mergeSort(arr[:mid])
	right = mergeSort(arr[mid:])

	count = 0
	while len(left+right) > 0:
		if len(left) == 0:
			arr = arr[:count]
			arr = arr+right
			right.clear()
			continue
		
		if len(right) == 0:
			arr = arr[:count]
			arr = arr+left
			left.clear()
			continue

		if left[0] >= right[0]:
			arr[count] = right[0]
			del(right[0])
		else:
			arr[count] = left[0]
			del(left[0])
		count = count + 1
	return arr

print(mergeSort([6,5,5,3,1,8,5,7,2,4,1,4,6,3,6,2,1423,3,52,5,2,13,24,46,224,244,123,98]))