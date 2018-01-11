##https://www.pramp.com/challenge/yZm60L6d5juM7K38KYZ6
##Island Count
##Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.
##
##An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).
##
##Explain and code the most efficient solution possible and analyze its time and space complexities.
##def get_number_of_islands(binaryMatrix):
##  if binaryMatrix == None or binaryMatrix==[]:
##    return 0
##  row = len(binaryMatrix)
##  col = len(binaryMatrix[0])
##  isLandCount = 0
##  for i in range(0,row):
##    for j in range(0, col):
##      if binaryMatrix[i][j] == 1:
##        isLandCount = isLandCount + 1
##        markNeigborLand(binaryMatrix, i, j)
##  return isLandCount
##
##
##
##def markNeigborLand(binaryMatrix, i, j):
##  # boundary checks on i and j
##  if i < 0 or j < 0 or i>=len(binaryMatrix) or j>=len(binaryMatrix[0]):
##    return
##  if binaryMatrix[i][j] == 1:
##  # mark it
##    binaryMatrix[i][j] = 2
##    markNeigborLand(binaryMatrix, i-1, j)
##    markNeigborLand(binaryMatrix, i+1, j)
##    markNeigborLand(binaryMatrix, i, j-1)
##    markNeigborLand(binaryMatrix, i, j+1)


def get_number_of_islands(arr):
    if arr == None or arr == []:
        return 0
    row = len(arr)
    col = len(arr[0])
    islandCount = 0
    for i in range(0,row):
        for j in range(0,col):
            if arr[i][j] == 1:
                islandCount += 1
                markAdjacentIsland_v2(arr,i,j, row, col)
    return islandCount

def markAdjacentIsland(arr,i,j,row,col):
    if i < 0 or j<0 or i>=row or j>=col:
        return
    if arr[i][j] == 1:
        arr[i][j] = 2
        markAdjacentIsland(arr,i-1,j, row, col)
        markAdjacentIsland(arr,i+1,j, row, col)
        markAdjacentIsland(arr,i,j-1, row, col)
        markAdjacentIsland(arr,i,j+1, row, col)

def markAdjacentIsland_v2(arr, i,j, row, col):
    q = []
    q.append((i,j))
    while(len(q)>0):
        item = q.pop(0)
        x = item[0]
        y = item[1]
        if arr[x][y] == 1:
            arr[x][y] =2
            verifyAndPushToQueue(arr, q,x+1,y, row, col)
            verifyAndPushToQueue(arr, q,x-1,y, row, col)
            verifyAndPushToQueue(arr, q,x,y+1, row, col)
            verifyAndPushToQueue(arr, q,x,y-1, row, col)

def verifyAndPushToQueue(arr, q,x,y, row, col):
    if x < 0 or y<0 or x>=row or y>=col:
        return
    if arr[x][y] == 1:
        q.append((x,y))
            
