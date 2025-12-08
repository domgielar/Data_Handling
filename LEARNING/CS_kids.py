import pandas as pd

x = {"Student":["David", "Samuel", "Terry", "Evan"],
    "Age": [27,24,22,32], 
    "Country": ["UK", "Canada", "China", "USA"],
    "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"],
    "Marks": [85,72,89,76]
}


df = pd.DataFrame(x)

marks = df[["Marks"]]
print(marks)

cc = df[["Country","Course"]]
print(cc)

df2 = df
df2 = df2.set_index("Student")
#print(df2.head())

print(df2.loc["David", "Age"])

print(df2.loc["David", "Marks"])

print(df2.loc["David":"Terry", "Course": "Marks"])