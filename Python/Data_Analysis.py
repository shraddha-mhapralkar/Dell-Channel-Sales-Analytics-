import pandas as pd

df = pd.read_excel("Dell_Channel_Sales_Messy_2000Rows.xlsx")
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
