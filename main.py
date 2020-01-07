from itertools import combinations
import pandas as pd

print("Creating combinations")
combs = list(combinations(range(1,50),6))
print("Combinations done")
n = 10**6
comblist = [combs[i * n:(i + 1) * n] for i in range((len(combs) + n - 1) // n )]

print("Creating dataframe")
df1 = pd.DataFrame
df2 = pd.DataFrame
df3 = pd.DataFrame
df4 = pd.DataFrame

while comblist:
    df = pd.DataFrame()
    count = 0
    for comb in comblist:
        if df.size > 10**7:
            break
        df = pd.concat([df, pd.DataFrame(comb)], ignore_index=True)
        count += 1
    comblist = comblist[count:]
    if df1.empty:
        df1 = df.copy()
        print("Dataframe 1 copied")
    elif df2.empty:
        df2 = df.copy()
        print("Dataframe 2 copied")
    elif df3.empty:
        df3 = df.copy()
        print("Dataframe 3 copied")
    elif df4.empty:
        df4 = df.copy()
        print("Dataframe 4 copied")
    print(len(comblist))
    

# pd.DataFrame.from_records(comb, columns=["N1", "N2", "N3", "N4", "N5", "N6"])

df1["sum"] = df1.sum(axis=1)

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