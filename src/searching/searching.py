# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  if len(arr) == 0:
    return -1

  for i in range(len(arr)):
    if arr[i] == target:
      return  i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = arr.index(arr[j])

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


def binary_search(arr, target):

  selection_sort(arr)

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  targetFound = False
  
  while not targetFound:
    average = round((low + high) / 2)
    if arr[average] == target:
      targetFound = True
      return average
    elif arr[average] > target:
      high = average
    else:
      low = average

  return -1 # not found

# binary_search([5,8,9,-9,1,2,0], 6)

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
