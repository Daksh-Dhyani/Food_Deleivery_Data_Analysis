# 🍔 Food Delivery Data Analysis

A Python-based **Data Science Mini Project** that analyzes food delivery data to understand **orders, restaurant performance, customer ratings, order amounts, and delivery trends**.

This project uses **Pandas, NumPy, Matplotlib, and Seaborn** to clean, analyze, and visualize the dataset.

---

## 📌 Project Overview

Food delivery platforms generate large amounts of data related to customer orders, restaurants, ratings, food categories, order values, and delivery times.

This project analyzes a sample food delivery dataset to identify useful patterns and answer questions such as:

- Which restaurant receives the most orders?
- Which food category is most popular?
- What is the average order amount?
- What is the average customer rating?
- What is the average delivery time?
- Which restaurant has the highest average rating?
- Is there a relationship between delivery time and customer rating?

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze food delivery order data.
2. Perform data cleaning using Pandas.
3. Calculate statistical measures using NumPy and Pandas.
4. Analyze restaurant and food-category performance.
5. Study customer ratings and delivery times.
6. Find the correlation between rating and delivery time.
7. Create meaningful data visualizations.
8. Generate useful findings from the dataset.

---

## 🗂️ Dataset Description

The project uses a sample dataset containing **15 food delivery orders**.

| Column | Description | Data Type |
|---|---|---|
| `Order_ID` | Unique order number | Integer |
| `Restaurant` | Restaurant name | Object |
| `Food_Category` | Type of food ordered | Object |
| `Order_Amount` | Total order amount | Integer |
| `Rating` | Customer rating | Float |
| `Delivery_Time` | Delivery time in minutes | Integer |

### Example Data

| Order_ID | Restaurant | Food_Category | Order_Amount | Rating | Delivery_Time |
|---:|---|---|---:|---:|---:|
| 1 | Pizza Hub | Pizza | 450 | 4.5 | 30 |
| 2 | Burger Point | Burger | 300 | 4.0 | 25 |
| 3 | Food Palace | Indian | 550 | 4.2 | 40 |
| 4 | Pizza Hub | Pizza | 700 | 4.8 | 35 |
| 5 | Biryani House | Biryani | 400 | 4.1 | 45 |

---

## 🛠️ Technologies Used

- 🐍 **Python**
- 🐼 **Pandas**
- 🔢 **NumPy**
- 📊 **Matplotlib**
- 📈 **Seaborn**
- 💻 **Jupyter Notebook / VS Code**

---

## 🧹 Data Cleaning

Pandas is used to perform basic data cleaning:

- Check missing values
- Check duplicate records
- Check data types
- Remove duplicate records
- Validate ratings
- Check valid order amounts
- Check valid delivery times

Example:

```python
# Check missing values
print(df.isnull().sum())

# Check duplicate records
print(df.duplicated().sum())

# Check data types
print(df.dtypes)

# Remove duplicates
df = df.drop_duplicates()

# Validate data
df = df[(df["Rating"] >= 0) & (df["Rating"] <= 5)]
df = df[df["Order_Amount"] > 0]
df = df[df["Delivery_Time"] > 0]
```

---

## 📊 Data Analysis

### Statistical Analysis

The project calculates:

- Mean
- Median
- Standard deviation
- Minimum value
- Maximum value
- Total sales
- Average rating
- Average delivery time

Example:

```python
import numpy as np

mean_order = np.mean(df["Order_Amount"])
median_order = np.median(df["Order_Amount"])
std_order = np.std(df["Order_Amount"])

print("Mean:", mean_order)
print("Median:", median_order)
print("Standard Deviation:", std_order)
```

---

## 🍽️ Restaurant Analysis

Restaurant-wise analysis is performed using `groupby()`.

```python
restaurant_summary = df.groupby("Restaurant").agg(
    Orders=("Order_ID", "count"),
    Average_Rating=("Rating", "mean"),
    Total_Sales=("Order_Amount", "sum")
)

print(restaurant_summary)
```

This helps compare:

- Number of orders
- Average rating
- Total sales

---

## 🔎 Sorting & Filtering

High-value orders can be identified using filtering.

```python
# Sort orders by amount
df.sort_values("Order_Amount", ascending=False)

# Find orders above ₹500
high_value = df[df["Order_Amount"] > 500]

print(high_value)
```

---

## 🔗 Correlation Analysis

The project analyzes the relationship between **customer rating** and **delivery time**.

```python
correlation = df["Rating"].corr(df["Delivery_Time"])

print("Correlation:", correlation)
```

Correlation helps identify whether rating and delivery time have a positive, negative, or weak linear relationship.

> **Note:** Correlation does not prove causation.

---

# 📈 Data Visualization

## Matplotlib

The project uses Matplotlib to create:

### 1. Bar Chart
Shows the number of orders received by each restaurant.

### 2. Line Chart
Shows the delivery-time trend across orders.

### 3. Histogram
Shows the distribution of order amounts.

### 4. Pie Chart
Shows the percentage distribution of food categories.

### 5. Scatter Plot
Shows the relationship between customer rating and delivery time.

Example:

```python
plt.scatter(df["Delivery_Time"], df["Rating"])

plt.title("Rating vs Delivery Time")
plt.xlabel("Delivery Time")
plt.ylabel("Rating")

plt.show()
```

---

## Seaborn

Seaborn is used for additional statistical visualizations:

- Count Plot
- Pair Plot

Example:

```python
import seaborn as sns

sns.countplot(data=df, x="Food_Category")

plt.title("Orders by Food Category")
plt.show()
```

---

# 🔍 Key Findings

The analysis provides the following observations:

1. The dataset contains **15 food delivery orders**.
2. Different restaurants have different order frequencies.
3. Food category analysis helps identify the most popular food type.
4. The average order amount gives an idea of customer spending.
5. Customer ratings can be used to compare restaurant performance.
6. Delivery time varies between different orders.
7. Restaurant-wise grouping helps identify high-performing restaurants.
8. Correlation analysis shows the observed relationship between delivery time and customer ratings.

---

# 📌 Conclusion

The **Food Delivery Data Analysis** project demonstrates how Python can be used to analyze real-world business data.

Using **Pandas**, the dataset is cleaned, filtered, grouped, and analyzed. **NumPy** is used for numerical and statistical calculations, while **Matplotlib and Seaborn** are used to create meaningful visualizations.

The analysis provides insights into:

- 📦 Customer orders
- 🍽️ Restaurant performance
- ⭐ Customer ratings
- 💰 Order amounts
- 🚴 Delivery trends
- 🍕 Food-category preferences

This project demonstrates the basic **Data Science workflow:**

**Data → Cleaning → Analysis → Visualization → Findings → Conclusion**

---

## 📁 Project Structure

```text
Food-Delivery-Data-Analysis/
│
├── 📄 food_delivery_analysis.py
├── 📄 dataset.csv
├── 📄 README.md
├── 📄 Food_Delivery_Data_Analysis_Case_Study.docx
│
└── 📁 images/
    ├── orders_restaurant.png
    ├── delivery_trend.png
    ├── order_histogram.png
    ├── category_pie.png
    ├── rating_delivery_scatter.png
    ├── category_count.png
    └── pairplot.png
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Food-Delivery-Data-Analysis.git
```

### 2. Open the project folder

```bash
cd Food-Delivery-Data-Analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the Python file

```bash
python food_delivery_analysis.py
```

---

## 👨‍💻 Author

**Daksh Dhyani**

🎓 BCA Data Science  
🏫 Chandigarh University

---

## ⭐ Project Type

**Data Science Mini Project**

**Domain:** Food Delivery & Customer Analytics

**Main Tools:** Python | Pandas | NumPy | Matplotlib | Seaborn
