def find_grants_cap(grantsArray, newBudget):
  grantsArray.sort()
  length = len(grantsArray) # 2
  previousSum = 0
  for i in range(0, length): # i=0
    currentValue = grantsArray[i] #curr=2
    if i > 0:
      previousSum = previousSum+grantsArray[i-1]
    if currentValue*length + previousSum > newBudget: #2*2+2 > 3, true
      return 1.0*(newBudget-previousSum)/length # 3/2=1.5
    length = length-1


grantsArray = [2,100,50,120,1000]
print(find_grants_cap(grantsArray, 190))



