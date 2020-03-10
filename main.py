""" 
This code is created to solved the puzzle in Geocache GC1R50B - Winning the Lottery (https://www.geocaching.com/geocache/GC1R50B)

The puzzle:
You have just invented a device which allows you to retrieve pieces of information from the future. Howver, it is still a beta version, 
so you can only use it to get information about a week ahead of time, and only a few small bits of information per week.
Since you always wanted to be rich, you instruct the device to get you the lottery numbers for the next drawing of the 6/49 lottery. 
Unfortunately 6 numbers at the same time is too much information for the machine, and it just spits out an error.
Being a smart cookie, you try and ask the device for the sum of the 6 lottery numbers. 
The machine starts rattling, and voila - spits out a piece of paper with a number on it. 
Looking at the number, you start to realize your mistake: There's got to be thousands of possible number combinations that yield this particular sum!
Luckily the machine is also quite smart and feels your despair. It starts working again and spits out some more information: 
It tells you that if you figure out exactly how many possible number combinations there are (from 6 out of 49 numbers) to yield this particular sum, 
and then multiply this number with the sum on the paper, it will yield a new number of around one million, 
and you will also get the same number if you multiply all 6 lottery numbers with each other.

After that, the machine went silent.

Now you need to figure out those 6 numbers! Rest assured that this is enough information to find a single set of 6 winning numbers for the lottery.
"""

from itertools import combinations
import pandas as pd
import time

#Assign variables for testing parameters
lowNum = 1
highNum = 49
binSize = 6

#Use combinations to give all combinations of binSize numbers from a pool of highNum numbers (6 from 49 in GC) - 13.983.816 different combinations
#Returned as iterator
print("Creating combinations")
combs = list(combinations(range(lowNum,highNum+1),binSize))
print("Combinations done")

#Define lowest and highest possible sum for counting later
lowsum = sum(range(lowNum,lowNum+6))
highsum = sum(range(highNum-binSize+1,highNum+1))

#Create list of possible sums
sumRange = list(range(lowsum,highsum+1))
values = [0] * len(sumRange)

#Using list comprehension to speed up performance and avoid filling memory with a giant DataFrame
print("Beginning calculations")

#For each combination calculate the sum
t0 = time.time()
numSum = [(a+b+c+d+e+f) for a,b,c,d,e,f in combs]
t1 = time.time()

print("Time used for numSum: {}".format(t1-t0))

#Count the number of times each sum appears
t0 = time.time()
sumCount = [numSum.count(num) for num in sumRange]
t1 = time.time()

print("Time used for count: {}".format(t1-t0))

#Create the product of the sums and their count
t0 = time.time()
sumProd = [a*b for a,b in zip(sumRange, sumCount)]
t1 = time.time()

print("Time used for sumProd: {}".format(t1-t0))

#number around ~1.000.000 (From puzzle description) create range to filter the result to a more managable size
lowLim = 990000
upLim = 1100000

#create a list of combinations for which the product is between lowLim and upLim
t0 = time.time()
winPool = [comb for comb in combs if lowLim < comb[0]*comb[1]*comb[2]*comb[3]*comb[4]*comb[5] < upLim]
t1 = time.time()

print("Time used for indexing: {}".format(t1-t0))

#Calculate the product of the 6 numbers in each possible winning combination
t0 = time.time()
winProd = [(a*b*c*d*e*f) for a,b,c,d,e,f in winPool]
t1 = time.time()

print("Time used for numProd: {}".format(t1-t0))

#Calculate the sum of each winning combination
winSum = [(a+b+c+d+e+f) for a,b,c,d,e,f in winPool]

#Use the sumProd list to get the product of sum and count for each winning combination 
#winSum contains sums, sumRange contains all possible sums sumRange.index(i) returns the index of the particular sum
#Since sumProd and sumRange are equally long we can use the index to get the corresponding sum count product from sumProd
winSumProd = [sumProd[sumRange.index(i)] for i in winSum]

#Convert to Dataframes now that the solutionspace has been reduced to make merging and filtering easier
t0 = time.time()
dfWinSumProd = pd.DataFrame(winSumProd, columns = ["sumProd"])
dfWinProd = pd.DataFrame(winProd, columns = ["prod"])
dfWinSum = pd.DataFrame(winSumProd, columns = ["sum"])
dfWinPool = pd.DataFrame(winPool, columns = ["N1", "N2", "N3", "N4", "N5", "N6"])
t1 = time.time()

#Merge the three relevant pieces of information together
total = pd.merge(dfWinPool, dfWinProd, left_index=True, right_index=True)
total = pd.merge(total, dfWinSum, left_index=True, right_index=True)
total = pd.merge(total, dfWinSumProd, left_index=True, right_index=True)

print("Time used for Dataframe: {}".format(t1-t0))

#Filter the winpool to the instances where the product of the numbers and the sumProd are equal
result = total[total["sumProd"] == total["prod"]]

#Used for the Geocache to get coordinates
A, B, C, D, E, F = list(result.iloc[0, :6])

#Finally print result
print("The winning numbers are: {}, {}, {}, {}, {} and {}".format(A, B, C, D, E, F))

N = (C*F) + B + 10
W = (D*F) - (A*B) + 1 + 15

print("Coordinates are N43 28.{}, W80 32.{}".format(N, W))

print(total[total["prod"]==1029952])
for summation, count in zip(sumRange,sumCount):
    print([summation, count])