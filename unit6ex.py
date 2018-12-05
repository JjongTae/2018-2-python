import pandas as pd
l =pd.read_csv("lynx.csv")
l["year"] = round(l.year/10)*10
print(l["year"])

sum_l= l["year"].groupby("year").sum()
sum_l.head