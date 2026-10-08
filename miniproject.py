# ============================================================
# CASE STUDY: FOOD DELIVERY DATA ANALYSIS
# ============================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CREATE DATASET
# ------------------------------------------------------------

data = {
    "Order_ID": range(1, 16),

    "Restaurant": [
        "Pizza Hub", "Burger Point", "Food Palace", "Pizza Hub",
        "Biryani House", "Burger Point", "Food Palace", "Pizza Hub",
        "Biryani House", "Burger Point", "Food Palace", "Pizza Hub",
        "Biryani House", "Burger Point", "Food Palace"
    ],

    "Food_Category": [
        "Pizza", "Burger", "Indian", "Pizza",
        "Biryani", "Burger", "Indian", "Pizza",
        "Biryani", "Burger", "Indian", "Pizza",
        "Biryani", "Burger", "Indian"
    ],

    "Order_Amount": [
        450, 300, 550, 700, 400,
        350, 600, 500, 450, 280,
        650, 750, 500, 320, 580
    ],

    "Rating": [
        4.5, 4.0, 4.2, 4.8, 4.1,
        3.8, 4.5, 4.7, 4.3, 3.9,
        4.6, 4.9, 4.4, 4.0, 4.5
    ],

    "Delivery_Time": [
        30, 25, 40, 35, 45,
        28, 38, 32, 42, 27,
        35, 30, 40, 25, 36
    ]
}

df = pd.DataFrame(data)


# ------------------------------------------------------------
# 2. DISPLAY DATASET
# ------------------------------------------------------------

print("\n========== FOOD DELIVERY DATASET ==========")
print(df)


# ------------------------------------------------------------
# 3. BASIC INFORMATION
# ------------------------------------------------------------

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ------------------------------------------------------------
# 4. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ------------------------------------------------------------
# 5. CHECK DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 6. NUMPY CALCULATIONS
# ------------------------------------------------------------

average_order = np.mean(df["Order_Amount"])
average_rating = np.mean(df["Rating"])
average_delivery = np.mean(df["Delivery_Time"])

highest_order = np.max(df["Order_Amount"])
lowest_order = np.min(df["Order_Amount"])

print("\n========== NUMPY ANALYSIS ==========")
print("Average Order Amount:", round(average_order, 2))
print("Average Rating:", round(average_rating, 2))
print("Average Delivery Time:", round(average_delivery, 2), "minutes")
print("Highest Order Amount:", highest_order)
print("Lowest Order Amount:", lowest_order)


# ------------------------------------------------------------
# 7. RESTAURANT-WISE ANALYSIS
# ------------------------------------------------------------

restaurant_orders = df["Restaurant"].value_counts()

print("\n========== ORDERS BY RESTAURANT ==========")
print(restaurant_orders)


# Average rating of each restaurant
restaurant_rating = df.groupby("Restaurant")["Rating"].mean()

print("\n========== AVERAGE RATING BY RESTAURANT ==========")
print(restaurant_rating.round(2))


# Average order amount by restaurant
restaurant_amount = df.groupby("Restaurant")["Order_Amount"].mean()

print("\n========== AVERAGE ORDER AMOUNT ==========")
print(restaurant_amount.round(2))


# ------------------------------------------------------------
# 8. CATEGORY-WISE ANALYSIS
# ------------------------------------------------------------

category_orders = df["Food_Category"].value_counts()

print("\n========== ORDERS BY FOOD CATEGORY ==========")
print(category_orders)


category_amount = df.groupby("Food_Category")["Order_Amount"].sum()

print("\n========== SALES BY FOOD CATEGORY ==========")
print(category_amount)


# ------------------------------------------------------------
# 9. DELIVERY TREND
# ------------------------------------------------------------

print("\n========== DELIVERY TIME ANALYSIS ==========")

fastest_delivery = df.loc[df["Delivery_Time"].idxmin()]
slowest_delivery = df.loc[df["Delivery_Time"].idxmax()]

print("Fastest Delivery:")
print(fastest_delivery)

print("\nSlowest Delivery:")
print(slowest_delivery)


# ------------------------------------------------------------
# 10. BEST RATED RESTAURANT
# ------------------------------------------------------------

best_restaurant = restaurant_rating.idxmax()
best_rating = restaurant_rating.max()

print("\n========== BEST RESTAURANT ==========")
print("Restaurant:", best_restaurant)
print("Average Rating:", round(best_rating, 2))


# ------------------------------------------------------------
# 11. TOTAL SALES
# ------------------------------------------------------------

total_sales = np.sum(df["Order_Amount"])

print("\n========== TOTAL SALES ==========")
print("Total Sales: ₹", total_sales)


# ------------------------------------------------------------
# 12. VISUALIZATION 1 - ORDERS BY RESTAURANT
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

restaurant_orders.plot(
    kind="bar",
    title="Number of Orders by Restaurant"
)

plt.xlabel("Restaurant")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 13. VISUALIZATION 2 - RESTAURANT RATINGS
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

restaurant_rating.plot(
    kind="bar",
    title="Average Rating by Restaurant"
)

plt.xlabel("Restaurant")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14. VISUALIZATION 3 - FOOD CATEGORY ORDERS
# ------------------------------------------------------------

plt.figure(figsize=(7, 5))

category_orders.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Orders by Food Category"
)

plt.ylabel("")
plt.show()


# ------------------------------------------------------------
# 15. VISUALIZATION 4 - DELIVERY TIME
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Order_ID"],
    df["Delivery_Time"],
    marker="o"
)

plt.title("Delivery Time Trend")
plt.xlabel("Order ID")
plt.ylabel("Delivery Time (Minutes)")
plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 16. VISUALIZATION 5 - ORDER AMOUNT
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    df["Order_ID"],
    df["Order_Amount"]
)

plt.title("Order Amount by Order ID")
plt.xlabel("Order ID")
plt.ylabel("Order Amount (₹)")
plt.show()


# ------------------------------------------------------------
# 17. CORRELATION
# ------------------------------------------------------------

correlation = df["Rating"].corr(df["Delivery_Time"])

print("\n========== CORRELATION ANALYSIS ==========")
print(
    "Correlation between Rating and Delivery Time:",
    round(correlation, 2)
)


# ------------------------------------------------------------
# 18. FINAL FINDINGS
# ------------------------------------------------------------

print("\n========== FINAL FINDINGS ==========")

print("1. Total number of orders:", len(df))
print("2. Total sales: ₹", total_sales)
print("3. Average rating:", round(average_rating, 2))
print("4. Average delivery time:",
      round(average_delivery, 2), "minutes")
print("5. Best rated restaurant:", best_restaurant)
print("6. Most ordered food category:",
      category_orders.idxmax())
print("7. Highest order amount: ₹", highest_order)
print("8. Lowest order amount: ₹", lowest_order)

print("\n========== PROJECT COMPLETED ==========")