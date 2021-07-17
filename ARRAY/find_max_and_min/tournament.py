def getminmax(low, high, arr):
	arr_max = arr[low]
	arr_min = arr[low]

	# if there is only one element
	if low == high:
		arr_max = arr[low]
		arr_min = arr[low]

		return (arr_max, arr_min)

	# if there are two elements
	elif high == low+1:
		if arr[low]> arr[high]:
			arr_max = arr[low]
			arr_min = arr[high]

		else:
			arr_max = arr[high]
			arr_min = arr[low]

		return (arr_max, arr_min)

	else:
		# if there are more than two elements 
		mid = int((low+high)/2)
		arr_max1, arr_min1 = getminmax(low,mid, arr)
		arr_max2, arr_min2 = getminmax(mid+1, high, arr)


	return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

arr = [20, 1,25, 67,34,56,7,8,88,330,100, 340]
high = len(arr)-1

low= 0 

print(getminmax(low, high, arr))



