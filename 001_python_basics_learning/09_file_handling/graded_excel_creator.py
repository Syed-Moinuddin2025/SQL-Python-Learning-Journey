import pandas as pd

# Step 1: DataFrame create karna
data = {
    "Roll no": [101, 102, 103, 104],
    "Name": ["Moin", "Ahmed", "Zara", "Tariq"],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)

# Step 2: Grade column add karna
def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    else:
        return 'C'

df["Grade"] = df["Marks"].apply(assign_grade)

# Step 3: Excel file save with grade
df.to_excel("graded_data.xlsx", index=False)
print("✅ Graded Excel file created successfully.")

# Excel file read karna
df = pd.read_excel("graded_data.xlsx")   # Excel file must be in same folder
print(df.head())
