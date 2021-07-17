class pair:
	def __init__(self):
		self.min = 0
		self.max = 0 

def getminmax(arr: list , n :int):
	minmax = pair()

	#if there is inly one element in the array
	if n == 1:
		minmax.max = arr[0]
		minmax.min = arr[0]

		return minmax

	#if there are more than one element set min max

	if arr[0]> arr[1]:

		minmax.max = arr[0]

		minmax.min = arr[1]

	else:
		minmax.max = arr[1]
		minmax.min = arr[0]

	for i in range(2, n):
		if arr[i] > minmax.max:
			minmax.max = arr[i]

		elif arr[i] < minmax.min:
			minmax.min = arr[i]

	return minmax
arr = [20, 1,25, 67,34,56,7,8,88,330,100]
arr_size = len(arr)
minmax = getminmax(arr,arr_size)

print(minmax.max, minmax.min)
