-- Data_Import

USE dell_project;

SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA LOCAL INFILE 'C:/Users/Shraddha Mhapralkar/Downloads/Dell_Project/cleaned_dell_sales.csv'
INTO TABLE dell_sales
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

SHOW VARIABLES LIKE 'local_infile';
SELECT *
FROM Dell_sales
LIMIT 10;