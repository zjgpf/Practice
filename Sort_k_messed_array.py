#https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnBZ
def sort_k_messed_array_v1(arr, k):
    l = []
    for i in range(0,len(arr)-k):
        minNum = arr[0]
        minNumIndex = 0
        for j in range(0, k+1):
          if minNum > arr[j]:
            minNum = arr[j]
            minNumIndex = j
        arr.pop(minNumIndex)
        l.append(minNum)
    for i in range(0, k):
        for j in range(i+1,k):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    for i in range(0,k):
        l.append(arr[i])
    return l

def sort_k_messed_array_v2(arr, k):
    length = len(arr)
    for start in range(0,length-k):
        minNum = arr[start]
        minNumIndex = start
        #find min Num and index
        for j in range(start, start+k+1):
          if minNum > arr[j]:
            minNum = arr[j]
            minNumIndex = j
        #change the first index aganist min Index
        arr[minNumIndex]= arr[start]
        arr[start] = minNum
    print(arr)
    for i in range(length-k, length):
        for j in range(i+1,length):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def sort_k_messed_array_v3(arr, k):
    length = len(arr)
    for i in range(1,length):
        a = arr[i]
        j = i-1
        while a<arr[j] and j>=0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = a
    return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
print(arr)
l = sort_k_messed_array_v3(arr, 2)
print(l)
