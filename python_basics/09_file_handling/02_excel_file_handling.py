import pandas as pd

data = {
     " Roll no ": [101,102,103,104],
    "Name": ["Moin", "Ahmed", "Zara", "Tariq"],
    "Marks": [85, 90, 95,88],
    
}
df = pd.DataFrame(data)

df.to_excel("data.xlsx", index=False)
print("Excel file created ✅")

import pandas as pd

# Excel file read karna
df = pd.read_excel("data.xlsx")   # Excel file must be in same folder
print(df.head())
