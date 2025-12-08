import pandas as pd
import numpy as np

table=pd.read_csv("WorldBankGDP.csv")


Years=["2011 [YR2011]","2014 [YR2014]","2017 [YR2017]","2021 [YR2021]","2024 [YR2024]"]

table = table[["Country Name", "Series Name"]+Years].copy()


table[Years] = table[Years].apply(pd.to_numeric, errors="coerce")
table.columns = ["Country","Indicator","2011","2014","2017","2021","2024"]

#rounding every row except GDP CONSTANT
i=1
table.loc[table.index!= i,["2011","2014","2017","2021","2024"]]=table.loc[table.index!= i,["2011","2014","2017","2021","2024"]].round(2)



pd.set_option('display.float_format', lambda x: f'{x:.2f}')

kenya = table[table["Country"]=="Kenya"].copy()
kenya = kenya.drop(columns=["Country"])
kenya = kenya.set_index("Indicator")




uganda = table[table["Country"]=="Uganda"].copy()
uganda = uganda.drop(columns=["Country"])
uganda = uganda.set_index("Indicator")


uganda.to_csv("Uganda_Core.csv")
kenya.to_csv("Kenya_Core.csv")

print(kenya)
