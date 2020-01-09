from itertools import combinations
import pandas as pd
import time

lowNum = 1
highNum = 30
binSize = 6

print("Creating combinations")
combs = list(combinations(range(lowNum,highNum+1),binSize))
print("Combinations done")

lowsum = sum(range(lowNum,lowNum+6))
highsum = sum(range(highNum-binSize+1,highNum+1))

sumRange = list(range(lowsum,highsum+1))
values = [0] * len(sumRange)

#sumCount = pd.DataFrame(values, index = sumRange, columns = ["count"])
#winPool = pd.DataFrame()

print("Beginning calculations")

t0 = time.time()
numSum = [(a+b+c+d+e+f) for a,b,c,d,e,f in combs]
t1 = time.time()

print("Time used for numSum: {}".format(t1-t0))

t0 = time.time()
sumCount = [numSum.count(num) for num in sumRange]
t1 = time.time()

print("Time used for count: {}".format(t1-t0))

t0 = time.time()
sumProd = [a*b for a,b in zip(sumRange, sumCount)]
t1 = time.time()

print("Time used for sumProd: {}".format(t1-t0))

lowLim = 600
upLim = 70000

t0 = time.time()
winPool = [comb for comb in combs if lowLim < comb[0]*comb[1]*comb[2]*comb[3]*comb[4]*comb[5] < upLim]
t1 = time.time()

print("Time used for indexing: {}".format(t1-t0))

t0 = time.time()
winProd = [(a*b*c*d*e*f) for a,b,c,d,e,f in winPool]
t1 = time.time()

print("Time used for numProd: {}".format(t1-t0))

winSum = [(a+b+c+d+e+f) for a,b,c,d,e,f in winPool]

winSumProd = [sumProd[sumRange.index(i)] for i in winSum]

""" print(len(winSumProd))
print(len(winProd)) """

wIndex = [winSumProd[winProd.index(i)] == winProd[winProd.index(i)] for i in winProd]
print(wIndex)
""" result = winPool[wIndex]
resultProd = winProd[wIndex]
resultSumProd = winSumProd[wIndex] """



""" print(winPool[:20])
print(winSumProd[:20])
print(winProd[:20])
print(result)
print(resultProd)
print(resultSumProd) """

""" for i, comb in enumerate(combs):
    sumCount.loc[sum(comb)] += 1
    #if lowLim < numProd[i] < upLim:
        #winPool = winPool.append(pd.DataFrame(comb).transpose())
    
    if i%10**4 == 0:
        print("{} % complete".format(round(i/tot*100,0)))
    #print("The sum of {}, {}, {}, {}, {} and {} is {}".format(comb[0],comb[1],comb[2],comb[3],comb[4],comb[5], sum(comb)))
 """

'''
winPool.columns = ["N1", "N2", "N3", "N4", "N5", "N6"]

winPool["sum"] = winPool.sum(axis=1)
total = pd.merge(winPool, sumCount, left_on="sum", right_index=True)
total["sumProd"] = total["sum"] * total["count"]
total["numProd"] = total["N1"] * total["N2"] * total["N3"] * total["N4"] * total["N5"] * total["N6"]
result = total[total["sumProd"] == total["numProd"]]
print(total)
print(result)


# pd.DataFrame.from_records(comb, columns=["N1", "N2", "N3", "N4", "N5", "N6"])



sumCount = df1["sum"].value_counts()
sumCount.columns = "count"
total = pd.merge(df1, sumCount, left_on="sum", right_index=True)
total = total.drop("sum_x", axis=1)
total.columns = ["sum", "N1", "N2", "N3", "N4", "N5", "N6", "SumCount"] 
total = total[["N1", "N2", "N3", "N4", "N5", "N6", "sum", "SumCount"]]
total["sumProd"] = total["sum"] * total["SumCount"]
total["numProd"] = total["N1"] * total["N2"] * total["N3"] * total["N4"] * total["N5"] * total["N6"]
#result = total[total["sumProd"] == total["numProd"]]
#print(result)
print(total.tail())
'''