##https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX
##Shifted Array Search
##A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
##
##Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn’t fully reversed).
##
##Explain your solution and analyze its time and space complexities.
##input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
##                                                 # outcome of shifting
##                                                 # [2, 4, 5, 9, 12, 17]
##                                                 # three times to the left
##
##output: 3 # since it’s the index of 2 in arr

def shifted_arr_search(shiftArr, num):
    if shiftArr[0] == num:
      return 0
    minNumIndex = findMinNumIndex(shiftArr)
    if minNumIndex == 0:
      return binary_search(shiftArr,num)    
    elif shiftArr[0] < num:
        return binary_search(shiftArr[:minNumIndex],num)
    else:
        return binary_search(shiftArr[minNumIndex:],num)+minNumIndex
    
def findMinNumIndex(shiftArr):
    start = 0
    end = len(shiftArr)-1
    while start <= end:
        mid = (start+end)//2
        if shiftArr[mid]<shiftArr[mid-1] or mid ==0:
            return mid
        elif shiftArr[mid] > shiftArr[0]:
            start = mid+1
        else:
            end = mid-1


def binary_search(arr, num):
    start=0
    end = len(arr)-1
    while start<= end:
        mid = (start+end)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid-1
        else:
            start = mid+1
    return -1
  
arr = [1,2]
print(binary_search(arr,2))
print(shifted_arr_search(arr,2))
