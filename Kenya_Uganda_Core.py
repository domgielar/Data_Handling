import pandas as pd

table=pd.read_csv("WorldBankGDP.csv")

Years=["2011 [YR2011]","2014 [YR2014]","2017 [YR2017]","2021 [YR2021]","2024 [YR2024]"]

table = table[["Country Name", "Series Name"]+Years].copy()

table.columns = ["Country","Indicator","2011","2014","2017","2021","2024"]


kenya = table[table["Country"]=="Kenya"].copy()
kenya = kenya.set_index("Indicator")

print(kenya)