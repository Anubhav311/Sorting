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
def binary_search(arr, target):
  
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


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  average = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if arr[average] == target:
    print('if: ', low, high, average)
    return average
  elif arr[average] > target:
    print('elif: ', low, high, average)
    return binary_search_recursive(arr, target, low = low, high = average)
  else:
    print('else: ', low, high, average)
    return binary_search_recursive(arr, target, low = average, high = high)

