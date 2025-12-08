import pandas as pd
import numpy as np

table=pd.read_csv("WorldBankFirms.csv")


Years=["2007 [YR2007]","2013 [YR2013]","2018 [YR2018]"]

table = table[["Country Name", "Series Name"]+Years].copy()



table[Years] = table[Years].apply(pd.to_numeric, errors="coerce")
table.columns = ["Country","Indicator","2007","2013","2018"]

#rounding everything to 2 decimals
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

kenya = table[table["Country"]=="Kenya"].copy()
kenya = kenya.drop(columns=["Country"])
kenya = kenya.set_index("Indicator")




uganda = table[table["Country"]=="Uganda"].copy()
uganda = uganda.drop(columns=["Country"])
uganda = uganda.set_index("Indicator")

Tanzania = table[table["Country"]=="Tanzania"].copy()
Tanzania = Tanzania.drop(columns=["Country"])
Tanzania = Tanzania.set_index("Indicator")


uganda.to_csv("Uganda_Firms.csv")
kenya.to_csv("Kenya_Firms.csv")
Tanzania.to_csv("Tanzania_Firms.csv")

print(kenya)