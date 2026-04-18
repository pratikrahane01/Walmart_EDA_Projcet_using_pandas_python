import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Walmart.csv")
print(df.head())

print(df.shape)

print(df.isnull().sum())

print(df.info())
print(df.describe())

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Extract year, month and week
#These help analyze monthly and yearly sales trends

df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["week"]=df["Date"].dt.isocalendar().week
df["weekday"]=df["Date"].dt.weekday

print(df.head())

#total sales
total_sales=df["Weekly_Sales"].sum()
print(f"Total sales: {total_sales}")

#Average Weekly Sales
Avg_weekly_sales=df["Weekly_Sales"].mean()
Avg_weekly_sales=round(Avg_weekly_sales,2)

print(f"Avg weekly sales: {Avg_weekly_sales}")

#Maximum Weekly Sales

max_weekly_sales=df["Weekly_Sales"].max()
max_weekly_sales=round(max_weekly_sales,2)

print(f"Max weekly sales: {max_weekly_sales}")



#Minimum Weekly Sales

min_weekly_sales=df["Weekly_Sales"].min()
min_weekly_sales=round(min_weekly_sales,2)

print(f"Min weekly sales: {min_weekly_sales}")

print(df.columns)

#top 5 performing stores and bottom 5 performing stores

top5=df.nlargest(5,"Store")
bottom5=df.nsmallest(5,"Store")

print(f"top 5 performing stores: {top5}")
print(f"bottom 5 performing stores: {bottom5}")

#avg weekly sales per store

Avg_weekly_sales_per_store=df.groupby("Store")["Weekly_Sales"].mean().round(2)
print(f"avg weekly sales per store: {Avg_weekly_sales_per_store}")


#Holiday Impact Analysis
holiday_impact_sales=df.groupby("Holiday_Flag")["Weekly_Sales"].mean().round(2)
print(f"holiday_impact_sales: {holiday_impact_sales}") #i.e 0= Normal week , 1= Holiday week
print("here clearly visible on holiday weeks there are more sales as compared to normal one")


#Monthly Sales Trend

monthly_sales=df.groupby("Month")["Weekly_Sales"].sum().round(2)
print(f"monthly_sales: {monthly_sales}")

#Highest sales month
highest_monthly_sales=monthly_sales.max()
highest_monthly_sales=round(highest_monthly_sales,5)
print(f"higest_monthly_sales: {highest_monthly_sales}")


#Lowest sales month
lowest_monthly_sales=monthly_sales.min()
lowest_monthly_sales=round(lowest_monthly_sales,5)
print(f"higest_monthly_sales: {lowest_monthly_sales}")


#Weekly Sales Trend

#Group sales by Week number.

sales_weekly_by_weekno=df.groupby("week")["Weekly_Sales"].sum().round(2)
print(f"Group sales by Week number: {sales_weekly_by_weekno}")

#Analyze weekly sales performance.

higest_weekly_sales=sales_weekly_by_weekno.max()
print(f"higest_weekly_sales: {higest_weekly_sales}")

lowest_weekly_sales=sales_weekly_by_weekno.min()
print(f"lowest_weekly_sales: {lowest_weekly_sales}")

#Temperature Impact on Sales

# Range of correlation values:
# +1 → strong positive relationship
# 0  → no relationship
# -1 → strong negative relationship

temp_sales_corr=df["Temperature"].corr(df["Weekly_Sales"])
print(f"temp_sales_corr: {temp_sales_corr}")

#As temperature increases, sales slightly decrease

plt.scatter(df["Temperature"], df["Weekly_Sales"],marker="*",color="purple")
plt.grid(color="gray",linestyle=":")
plt.xlabel("Temperature")
plt.ylabel("Weekly Sales")
plt.title("Temperature vs Weekly Sales")
plt.legend(loc="upper left")
plt.show()

#Fuel Price Impact

Fuel_Price_Impact=df["Fuel_Price"].corr(df["Weekly_Sales"])
print(f"Fuel_Price_Impact: {Fuel_Price_Impact}")

#when fuel prices increases the weekly sales increases


plt.scatter(df["Fuel_Price"], df["Weekly_Sales"],marker="^",color="green")
plt.grid(color="gray",linestyle=":")
plt.xlabel("fuel prices")
plt.ylabel("Weekly Sales")
plt.title("Temperature vs Weekly Sales")
plt.legend(loc="upper left")
plt.show()

#CPI Impact

CPI_Impact=df["CPI"].corr(df["Weekly_Sales"])
print(f"CPI impact: {CPI_Impact}")

#as CPI increases weekly sales slightly decreases

plt.scatter(df["CPI"], df["Weekly_Sales"],marker="d",color="red")
plt.grid(color="gray",linestyle=":")
plt.xlabel("CPI")
plt.ylabel("Weekly Sales")
plt.title("Temperature vs Weekly Sales")
plt.legend(loc="upper left")
plt.show()

#Unemployment Impact

unemployment_Impact=df["Unemployment"].corr(df["Weekly_Sales"])
print(f"unemployment impact: {unemployment_Impact}")


#as unployment increases weekly sales decreses

plt.scatter(df["Unemployment"], df["Weekly_Sales"],marker="<",color="skyblue")
plt.grid(color="gray",linestyle=":")
plt.xlabel("Unemployment")
plt.ylabel("Weekly Sales")
plt.title("Temperature vs Weekly Sales")
plt.legend(loc="upper left")
plt.show()

#Correlation Analysis
corr_matrix=df.corr()
print(corr_matrix)


# correlation with  Weekly_Sales

# Temperature
#As temperature increases, sales slightly decrease

# Fuel_Price
#when fuel prices increases the weekly sales increases

# CPI
#as CPI increases weekly sales slightly decreases

# Unemployment
#as unployment increases weekly sales decreses

