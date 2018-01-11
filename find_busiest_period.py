#https://www.pramp.com/challenge/2WBx3Axln1t7JQ2jQq96
'''
Busiest Time in The Mall
The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.
'''
def find_busiest_period(data):
  maxTimeStamp = data[0][0]
  sumPeople = 0
  maxPeople = 0
  length = len(data)

  for i in range(0, len(data)-1):
    if data[i][2] == 0:
      sumPeople = sumPeople - data[i][1]
    elif data[i][2] == 1:
      sumPeople = sumPeople + data[i][1]
    if maxPeople < sumPeople and (i == length -1 or data[i][0] != data[i+1][0]):
      maxPeople = sumPeople
      maxTimeStamp = data[i][0]
  if data[len(data)-1][2] == 0:
    sumPeople = sumPeople - data[len(data)-1][1]
  elif data[len(data)-1][2] ==1:
    sumPeople = sumPeople + data[len(data)-1][1]
  if maxPeople < sumPeople:
    maxTimeStamp = data[len(data)-1][0]
    
      
  return maxTimeStamp

def find_busiest_period_v2(data):
  maxTimeStamp = data[0][0]
  sumPeople = 0
  maxPeople = 0
  length = len(data)

  for i in range(0, length):
    if data[i][2] == 0:
      sumPeople = sumPeople - data[i][1]
    elif data[i][2] == 1:
      sumPeople = sumPeople + data[i][1]
    if maxPeople < sumPeople and (i == length -1 or data[i][0] != data[i+1][0]):
      maxPeople = sumPeople
      maxTimeStamp = data[i][0]        
  return maxTimeStamp
  

"""
let me know if you have questions
still there?
yes, I'm reading the problem.
okay
so the arr is:
['Current people','people increase','people decrese']?
no
['timestamp(sec or something)', 'num of people', 'entering or leaving the mall (1 for enter 0 for leaving)']
so for 1st one at time 14877...425 14 people entered, and at the same time 4 people left and also same time 2 people left
OK
data is sorted so all of the same time stamp would be grouped next to each other
OK

so right now its comparing currPeople to maxPeople every timestamp 
you want to only compare when it's end of a timestamp because that represents the total people for that time stamp 
I got it
so that's why I said reduce the iteration since you would look at i + 1
inside the for loop 
when i = n -1, it should not go into max comparison
"""
