import pandas as pd
import numpy as np

table=pd.read_csv("/Users/domgielar/Desktop/KenyaCase/WELFARECSV/Welfare.csv")


Years=["2011 [YR2011]","2014 [YR2014]","2017 [YR2017]","2021 [YR2021]","2024 [YR2024]"]

table = table[["Country Name", "Series Name"]+Years].copy()


table[Years] = table[Years].apply(pd.to_numeric, errors="coerce")
table.columns = ["Country","Indicator","2011","2014","2017","2021","2024"]




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

Rwanda = table[table["Country"]=="Rwanda"].copy()
Rwanda = Rwanda.drop(columns=["Country"])
Rwanda = Rwanda.set_index("Indicator")

Ghana = table[table["Country"]=="Ghana"].copy()
Ghana = Ghana.drop(columns=["Country"])
Ghana = Ghana.set_index("Indicator")

uganda.to_csv("Uganda_Welfare.csv")
kenya.to_csv("Kenya_Welfare.csv")
Tanzania.to_csv("Tanzania_Welfare.csv")
Rwanda.to_csv("Rwanda_Welfare.csv")
Ghana.to_csv("Ghana_Welfare.csv")
print(kenya)
