# 🍏 AppleStore Analysis
<div align="center">
  <img src="https://raw.githubusercontent.com/Syed-Moinuddin2025/sql-learning-journey/main/images/image56.png" alt="SQL Learning Banner" width="800" height="auto">
</div>
A data analytics project based on sales, product, and warranty data of Apple Stores across multiple countries. This project performs exploratory data analysis (EDA), derives business insights, and answers key performance questions using Python and pandas.

---

## 📁 Project Structure

```plaintext
01_Apple_Store_Analytics_Project/
├── AppleStore_Analysis.ipynb          # Main analysis notebook
├── cleaned_apple_store_data.csv       # Final merged dataset
├── apple_store_questions.md           # Business questions list
├── products.csv
├── sales.csv
├── stores.csv
├── warranty.csv
└── category.csv
```

---

## 📊 Dataset Overview

This project uses 5 CSV files:

- `products.csv` → Product ID, name, category, price, launch date
- `sales.csv` → Sales transaction ID, date, product\_id, quantity, store\_id
- `stores.csv` → Store details including city, country
- `warranty.csv` → Repair/claim details linked to sales
- `category.csv` → Product category mapping

All are merged into one `cleaned_apple_store_data.csv` for easy analysis.

---

## ✅ Key Business Questions Answered

### Sales Analysis

- What is the total revenue generated?
- Which product/category/store/city generates the most sales?
- What is the average sale value per store?

### Product Insights

- Top selling products
- Average price by category
- Return/repair patterns from warranty data

### Store Performance

- Store count by city & country
- Country-wise performance
- Trends over time

### Warranty Analysis

- Claim rates
- Most frequently claimed products
- Repair status breakdown

---

## 📌 Tools Used

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook (`.ipynb`)
- CSV files as input source

---

## 📈 Output Samples

- Bar chart of revenue by category
- Store-wise sales ranking
- Repair claim pie chart
- Monthly sales trends

---

## 🚀 Getting Started

1. Clone the repo or download project folder
2. Open `AppleStore_Analysis.ipynb` in Jupyter or VS Code
3. Run all cells to view EDA and insights

---

## 🧠 Author

**Syed Moinuddin**\
GitHub: [Syed-Moinuddin2025](https://github.com/Syed-Moinuddin2025)

---

> 📌 *This project is part of the SQL + Python Learning Journey.*
