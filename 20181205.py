import pandas as pd

alco = pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])
alco["Total"] = alco.Wine + alco.Spirits + alco.Beer
alco.head()
print(alco.head())