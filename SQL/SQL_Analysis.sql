USE dell_project;

-- SQL Analysis
-- Total Revenue Generated 
select * from Dell_sales;
select sum(Revenue) as Total_Revenue
from Dell_sales;

-- Revenue by Segment
select Segment, sum(Revenue) as Total_Revenue_by_Segment
from Dell_sales
group by Segment
order by Total_Revenue_by_Segment desc;

-- Revenue by Product_category
select Product, sum(Revenue) as Total_Revenue_by_Product
from Dell_sales
group by Product
order by Total_Revenue_by_Product desc;

-- Revenue by Region
select Region, sum(Revenue) as Total_Revenue_by_Region
from Dell_sales
group by Region
order by Total_Revenue_by_Region desc;

-- Top 10 customer
select Customer_Name, Sum(Revenue) as Total_Revenue
from Dell_sales
group by Customer_Name
order by Total_Revenue desc
limit 10;

#Top salesperson
Select Salesperson, Sum(Revenue) as Total_Revenue
from Dell_sales  
group by Salesperson
Order by Total_Revenue desc;

/* avg discount on products
Select Product_Category, avg(Discount_%) as Avg_Discount
from Dell_sales  
group by Product_Category
Order by Avg_Discount desc;
*/

-- Which month generated highest revenue
select monthname(Order_Date) as Month, sum(Revenue) as Total_Revenue
from Dell_sales
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY MONTH(Order_Date);

-- revenue by industry
select Industry, sum(Revenue) as Total_Revenue
from Dell_sales
group by Industry
order by Total_Revenue desc;

-- Avg revenue
Select AVG(Revenue) AS Average_Deal_Size
FROM dell_sales;

-- won/lost opportunity
SELECT Opportunity_Status, COUNT(*) AS Total_Deals
FROM dell_sales
GROUP BY Opportunity_Status;

-- Highest discount order
/*select Order_ID, Order_Date, Customer_Name,	Salesperson, Product_Category, Max('Discount_%') as max_discount
from Dell_sales
limit 1;*/

-- Average Delivery Days by Region
select Region, avg(Delivery_Days) as avg_delivery_days
from Dell_sales
Group by Region;

#which product family make high revenue
SELECT Product_Family, SUM(Revenue) AS Revenue
FROM dell_sales
GROUP BY Product_Family
ORDER BY Revenue DESC;

-- which manager persform well
select Manager, Sum(Revenue) as Total_Revenue
from Dell_sales
group by Manager
Order by Total_Revenue desc;


