import pandas as pd
import matplotlib.pyplot as plt

kenya=pd.read_csv("Kenya_Core.csv",index_col=0)
uganda=pd.read_csv("Uganda_Core.csv",index_col=0)

#x-axis(years)
year = kenya.columns.astype(int)

plt.figure(figsize=(12,6))

#loop for each indicator

for indicator in kenya.index:
    if ("GDP (constant 2015 US$)" not in indicator) and("Domestic credit to private sector" not in indicator):
        plt.plot(
            year,
            kenya.loc[indicator],
            marker="o",
            label=indicator
        )

plt.title("Kenya - All Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Value")
plt.grid(True)
plt.legend()   # shows indicator labels
plt.tight_layout()
plt.show()