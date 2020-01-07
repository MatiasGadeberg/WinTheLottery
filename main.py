from itertools import combinations
import pandas as pd

combs = list(combinations(range(1,30),6))

#n = 10**6
#comblist = [combs[i * n:(i + 1) * n] for i in range((len(combs) + n - 1) // n )]

df = pd.DataFrame(combs)

# pd.DataFrame.from_records(comb, columns=["N1", "N2", "N3", "N4", "N5", "N6"])

df["sum"] = df.sum(axis=1)

sumCount = df["sum"].value_counts()
sumCount.columns = "count"
total = pd.merge(df, sumCount, left_on="sum", right_index=True)
total = total.drop("sum_x", axis=1)
total.columns = ["sum", "N1", "N2", "N3", "N4", "N5", "N6", "SumCount"] 
total = total[["N1", "N2", "N3", "N4", "N5", "N6", "sum", "SumCount"]]
total["sumProd"] = total["sum"] * total["SumCount"]
total["numProd"] = total["N1"] * total["N2"] * total["N3"] * total["N4"] * total["N5"] * total["N6"]
result = total[total["sumProd"] == total["numProd"]]
print(result)