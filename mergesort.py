import math
import datetime

def mergeSort(arr):
	n = len(arr)
	if (n == 2):
		if arr[0] > arr[1]:
			arr[0], arr[1] = arr[1], arr[0]
		return arr
	
	if n == 1:
		return arr

	if (n % 2) == 0:
		group1 = mergeSort(arr[:int(n/2)])
		group2 = mergeSort(arr[int(n/2):])
	else:
		arrendondar = math.ceil(n/2)
		group1 = mergeSort(arr[:int(n/2)])
		group2 = mergeSort(arr[int(arrendondar)-1:])

	count = 0
	while len(group1+group2) > 0:
		if len(group1) == 0:
			arr = arr[:count]
			arr = arr+group2
			group2.clear()
			continue
		
		if len(group2) == 0:
			arr = arr[:count]
			arr = arr+group1
			group1.clear()
			continue

		if group1[0] >= group2[0]:
			arr[count] = group2[0]
			del(group2[0])
		else:
			arr[count] = group1[0]
			del(group1[0])
		count = count + 1
	return arr

print(mergeSort([6,5,5,3,1,8,5,7,2,4,1,4,6,3,6,2,1423,3,52,5,2,13,24,46,224,244,123,98]))