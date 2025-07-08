import pandas as pd

# # 🔁 Yahan apni Excel file ka exact naam likhiye
# filename = "basic excel course.xlsx"

# try:
#     # Excel file read karna
#     df = pd.read_excel(filename)
    
#     print(f"📊 Reading from: {filename}\n")
#     print("📈 First 5 rows:")
#     print(df.head())

# except FileNotFoundError:
#     print(f"❌ File '{filename}' not found. Please check the name.")
# except Exception as e:
#     print(f"❌ Error occurred: {e}")

import pandas as pd

filename = "basic_excel_course.xlsx"

# Read all sheets as dictionary
all_sheets = pd.read_excel(filename, sheet_name=None)

# Print all sheet names and their data
for sheet_name, data in all_sheets.items():
    print(f"📄 Sheet: {sheet_name}")
    print(data)
    print("-" * 40)
