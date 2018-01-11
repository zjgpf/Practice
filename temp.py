def insertion_sort(arr):
    for i in range(0,len(arr)-1):
        j = i+1
        temp = arr[j]
        while temp < arr[j-1] and j>0:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr

def root(x, n):
  lowerBound = 0
  upperBound = x
  approxRoot = x/2
  
  while approxRoot - lowerBound >= 0.001:
    if approxRoot**n > x:
      upperBount = approxRoot
    elif approxRoot**n < x:
      lowerBound = approxRoot
    else:
      break
    approxRoot = (lowerBound+upperBound)/2
  return approxRoot

print(root(9,2))
