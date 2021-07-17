## Using Simple linear Search:
1. will create two pairs :
        min and max
  -- no of element is one
    set max  = arr[0]
    set min = arr [0]
  -- no ofelements in array are greater than 1 :
    comapare the vaules and set min and max
  -- initialize loop from (2, n)
    check arr[i] > max
      max == arr[i]
    else arr[i]<min
      min == arr[i]
 -- eturn min max

  end of program
                  
                 
        
 ## Using Tournament method :
	Pair maxmin(array , arra_size):
		if arr_size = 1
			return element as both min and max
		elif arr_size = 2
			compare min and max 
			return min and max
		else arr_size > 2:
			recur for max and min of the left half
			recur for max and min of the right half
			one comparision determine true max of the two candidates
			one comparision determine true min for the two candidates
			return min max  
  
## Using comparision method :
###.  n = len(arr)
###. array has even no of elements
####	arr[0]>arr[1]
      set max = arr[0]
      set min = arr[1]
#### else set max = arr[1]
      set min = arr[0]
    set i = 2
###	ifarr has odd no of elements
    set max = arr[0]
    set min = arr [ 0]
    set i = 1
### ina loop pick elements  in pair and compare the pairs with max and min
      if arr[i] < arr[i+1]
        max = max(max , arr[i+1])
        min = min (min , arr[i])
      else
        max = max(max, arr[i])
        min = min(min, arr[i+1])
      return max min
