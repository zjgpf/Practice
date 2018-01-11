#https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5LM1

# reverses the order of the first k elements in the array arr.
def flip(arr, k):
    start = 0
    end = k-1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start+1
        end = end-1
    return arr

def findMaxIndex(arr,k):
    maxValue = arr[0]
    maxIndex = 0
    for i in range(1,k):
        if maxValue < arr[i]:
            maxValue = arr[i]
            maxIndex = i
    return maxIndex
    
def pancakeSort(arr):
    length = len(arr)
    m = length
    for i in range(0, length):
        maxIndex = findMaxIndex(arr,m)
        temp = arr[0]
        arr[0] = arr[maxIndex]
        arr[maxIndex] = temp
        flip(arr,m)
        m = m-1
    return arr

arr = [1, 5, 4, 3, 2]
l = pancakeSort(arr)
print(l)

