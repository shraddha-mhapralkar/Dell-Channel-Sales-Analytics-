-- Database setup

CREATE DATABASE dell_project;
USE dell_project;

CREATE TABLE Dell_sales (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Region VARCHAR(50),
    City VARCHAR(50),
    Industry VARCHAR(50),
    Segment VARCHAR(50),
    Customer_Name VARCHAR(100),
    Salesperson VARCHAR(100),
    Product_Category VARCHAR(100),
    Product_Family VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(10 , 2 ),
    Discount DECIMAL(5 , 2 ),
    Revenue DECIMAL(10 , 2 ),
    Opportunity_Status VARCHAR(20),
    Payment_Term VARCHAR(20),
    Delivery_Days INT,
    Warranty_Years INT,
    Partner_Name VARCHAR(20),
    Manager VARCHAR(20),
    Customer_Rating INT,
    Support_Tickets INT
)



