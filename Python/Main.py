import pandas as pd

df = pd.read_excel("Dell_Channel_Sales_Messy_2000Rows.xlsx")

#understand dataset
#1st 5 rows of dataset
print(df.head())
#last 5 rows of dataset
print(df.tail())
#structure od the dataset which inc column name, data types, not null count
df.info()
#statistics summary
print(df.describe())
#show all column names
print(df.columns)

#data cleaning
#missing values
print(df.isnull().sum())
#duplicate rows
print(df.duplicated().sum())
#remove whitespaces in all dataset
#for col in df.select_dtypes(include='object').columns:
   # df[col] = df[col].str.strip()
df["Segment"] = df["Segment"].str.strip()
#1st letter uppercase
df["Product_Category"] = df["Product_Category"].str.title()
#fill null value in city column
df["City"] = df["City"].fillna("Unknown")
#fill null value in customer rating with median
df["Customer_Rating"] = df["Customer_Rating"].fillna(
    df["Customer_Rating"].median())
#fill null value in support ticket with 0
df["Support_Tickets"] = df["Support_Tickets"].fillna(0)
#fill null value in Discount with 0
df["Discount_%"] = df["Discount_%"].fillna(0)
#fill null value in Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)
#fill null value in Revenue with calculated value
df["Revenue"] = (
    df["Quantity"] *
    df["Unit_Price"] *
    (1 - df["Discount_%"] / 100)
)
print(df.isnull().sum())
#save cleaned data
df.to_excel("Cleaned_Dell_Data.xlsx", index=False)
#total revenue
print("How much total business generated")
Total_Revenue = df["Revenue"].sum()
print(Total_Revenue)
#total revenue by segment
print("Total Revenue by segment")
Revenue_by_segment = (df.groupby("Segment")["Revenue"].sum().sort_values(ascending=False))
print(Revenue_by_segment)
#revenue by product
print("Total Revenue by product")
Revenue_by_product = (df.groupby("Product_Category")["Revenue"].sum().sort_values(ascending=False))
print(Revenue_by_product)
#revenue by region
print("Total Revenue by region")
Revenue_by_region = (df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))
print(Revenue_by_region)
#top 10 customer
top_customer = (df.groupby("Customer_Name")["Revenue"].sum().sort_values(ascending = False).head(10))
print(top_customer)
#top sales person
top_salesperson = (df.groupby("Salesperson")
                   ["Revenue"].sum().
                   sort_values(ascending = False).
                   head(10))
print(top_salesperson)
#which deal received higest discount
#print(df["Discount_%"].max())
highest_discount = (df.sort_values("Discount_%", ascending =False).head(10))
print(highest_discount)
#8th question#average order value
avg_deal_value = (df["Revenue"].mean())
print(avg_deal_value)
#monthly revenue
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
monthly_revenue = df.groupby(df["Order_Date"].dt.month)["Revenue"].sum()
print(monthly_revenue)
#revenue by industry
revenue_by_industry = df.groupby("Industry")["Revenue"].sum().sort_values(ascending=False)
print(revenue_by_industry)

df.to_csv("cleaned_dell_sales.csv", index=False)

