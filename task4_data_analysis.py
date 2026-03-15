import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("Customers.csv", encoding="latin1")
products = pd.read_csv("Products.csv", encoding="latin1")
sales = pd.read_csv("Sales.csv", encoding="latin1")
stores = pd.read_csv("Stores.csv", encoding="latin1")

# Check data structure
print("Customers dataset:-")
print(customers.head())
print("---------------------------------------------------------------------------------------------------------")
print("Products dataset:-")
print(products.head())
print("---------------------------------------------------------------------------------------------------------")
print("Sales dataset:-")
print(sales.head())
print("------------------------------------------------------------------------------------------------------------")
print("Stores dataset:-")
print(stores.head())
print()

# Check dataset size (row,columns)
print("Customers dataset size is ", customers.shape)
print("Products dataset size is ", products.shape)
print("Sales dataset size is", sales.shape)
print("Stores dataset size is ", stores.shape)
print()

# check column names and data types of each dataset
print(customers.info())
print("---------------------------------------------------------------------------------------------------------")
print(products.info())
print("---------------------------------------------------------------------------------------------------------")
print(sales.info())
print("---------------------------------------------------------------------------------------------------------")
print(stores.info())

''' 

Customers dataset contains 15266 customer records with  information such as gender, city, country, and birthday.

Products dataset contains 2517 products with details like product name, brand, color, cost, price, and product category

Sales dataset contains 62884 transaction records linking customers, products, and stores, along with order dates and quantity sold.

Stores dataset contains 67 store location with country, state, store size, and store opening date information. 

These datasets belong to the Global Electronics Retailer dataset and contain information about customers, products, sales transactions, and store locations'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Check missing values
print("Missing values in customers dataset is \n", customers.isnull().sum())
print("Missing values in products dataset is \n", products.isnull().sum())
print("Missing values in sales dataset is \n", sales.isnull().sum())
print("Missing values in stores dataset is\n", stores.isnull().sum())

'''
Customers dataset has 10 missing values in the State Code  column while all other columns are complete

Products dataset has no missing values, indicating the product information is fully available.

Sales dataset has a large number of missing values (49,719) in the Delivery Date column

Stores dataset has only 1 missing value in the Square Meters column, while the rest of the store information is complete.
'''

#--------------------------------------------------------------------------------------------------------------------
# basic business  insights

# calculate total quantity of products sold
total_quantity = sales["Quantity"].sum()
print("Total products sold:-", total_quantity)
print('-------------------------------------------')
# count customers in each country
customers_by_country = customers["Country"].value_counts()
print("Customers by country:- \n", customers_by_country)
print('-------------------------------------------')
# count stores in each country
stores_by_country = stores["Country"].value_counts()
print("Stores by country:- \n", stores_by_country)

'''
Total products sold in the  whole dataset are 197757 units.

Most customers are from the United States, followed by the United Kingdom and Canada

The majority of stores are located in the United States, with fewer stores spread across Europe and Australia
'''

print("----------------------------------------------------------------------------------------------------------------------")
# Sales by Product Category
# merge sales and products
sales_products = sales.merge(products, on="ProductKey")
# total quantity sold by category
category_sales = sales_products.groupby("Category")["Quantity"].sum().sort_values(ascending=False)

print("Sales by product category:-->\n", category_sales)


'''insight:- The analysis shows that the Computers and cellphones categories has the highest sales compared to other product categories.

action:-This indicates more customer demand for computer products and cell phones, suggesting the business should focus more inventory, marketing, and product expansion in this category.'''
print("---------------------------------------------------------------------------------------------------------------------------------\n")
# Top 5 profitable products
# clean cost and price
products["Unit Cost USD"] = products["Unit Cost USD"].str.replace("$","").str.replace(",","").astype(float)
products["Unit Price USD"] = products["Unit Price USD"].str.replace("$","").str.replace(",","").astype(float)
# merge sales and products
sales_products = sales.merge(products, on="ProductKey")
# profit per row by multiply quantity
sales_products["profit"] = (sales_products["Unit Price USD"] - sales_products["Unit Cost USD"]) * sales_products["Quantity"]
# total profit per product
profit_by_product = sales_products.groupby("Product Name")["profit"].sum().sort_values(ascending=False).head(5)
print("Top profitable products:---\n", profit_by_product)

"""
The product "WWI Desktop PC2.33 X2330 Black" generated the highest total profit, followed by "Adventure Works Desktop PC2.33 XD233 Silver".

These products generate significantly higher profit compared to other products, indicating strong sales performance and higher contribution to overall business profitability."""

print("-------------------------------------------------------------------------------------------------------------------------\n")
#  Top 5 least profitable products
least_profit_products = sales_products.groupby("Product Name")["profit"].sum().sort_values(ascending=True).head(5)

print("Least profitable products:-->\n", least_profit_products)

'''Insight :-The products "SV USB Data Cable E600 Silver" and "SV USB Sync Charge Cable E700 Silver" generated the lowest total profit among all products.

Action:- These products contribute very little to overall business profitability, so the company may consider improving pricing, increasing sales volume, or optimizing production costs.'''


print("--------------------------------------------------------------------------------------------------\n")
# most profitable country and least profitable country
# merge sales table with store for country name 
sales_products_country = sales_products.merge(stores, on="StoreKey")
# total profit by country
profit_by_country = sales_products_country.groupby("Country")["profit"].sum().sort_values(ascending=False)
# most profitable country
most_profitable_country = profit_by_country.head(1)
# least profitable country
least_profitable_country = profit_by_country.tail(1)
print("Most profitable country:-\n", most_profitable_country)
print("\nLeast profitable country:-", least_profitable_country)

'''insight:- The United States generated the highest total profit, while France generated the lowest profit among all countries.

action:- This suggests the business should continue strengthening its presence and marketing strategies in the United States, 
while improving sales performance and market strategies in France to increase profitability.'''

