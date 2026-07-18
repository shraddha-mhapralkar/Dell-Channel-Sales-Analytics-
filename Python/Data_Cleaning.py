import pandas as pd

df = pd.read_excel("Dell_Channel_Sales_Messy_2000Rows.xlsx")
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