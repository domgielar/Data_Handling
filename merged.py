import pandas as pd 
 
gdp=pd.read_csv("GDP.csv")
findex=pd.read_csv("MobileMoney.csv")

years=["2011 [YR2011]","2014 [YR2014]","2017 [YR2017]","2021 [YR2021]"]

gdp_new = gdp.melt(id_vars=["Country Name"], value_vars=["2011 [YR2011]", "2014 [YR2014]", "2017 [YR2017]", "2021 [YR2021]", "2024 [YR2024]"],var_name="Year", value_name="GDP_growth")
gdp_new["Year"] = gdp_new["Year"].str.slice(0,3).astype(int)

findex_new = findex.melt(id_vars=["Country Name"],value_vars=["2011 [YR2011]", "2014 [YR2014]", "2017 [YR2017]", "2021 [YR2021]", "2024 [YR2024]"],var_name="Year", value_name="MobileMoney")
findex_new["Year"] = findex_new["Year"].str.slice(0,3).astype(int)


master=pd.merge(
    gdp_new,
    findex_new,
    on=["Country Name", "Year"],
    how="inner"
)