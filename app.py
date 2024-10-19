import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from an Excel file
dataset = pd.read_excel("Superstore_USA.xlsx")

# Display the first five rows of the dataset
# print(dataset.head())  # Uncomment to view the first five rows

# Check for missing values in each column
missing_values = dataset.isnull().sum()
# print(missing_values)  # Optional: Uncomment to print the missing values

# Fill missing values in the 'Product Base Margin' column with the mean of that column
dataset['Product Base Margin'].fillna(
    dataset['Product Base Margin'].mean(), inplace=True
)

# Count plot for 'Order Priority'
plt.figure(figsize=(8, 6))
sns.countplot(x='Order Priority', data=dataset)
plt.title('Count of Order Priority')
plt.xlabel('Order Priority')
plt.ylabel('Count')
plt.xticks(rotation=30, fontsize=7)  # Rotate x labels for better visibility, if needed
plt.savefig("Count_of_Order_Priority.jpg")
plt.show()

# Count occurrences of each 'Ship Mode' and create a pie chart
ship_mode_counts = dataset['Ship Mode'].value_counts()
x = ship_mode_counts.index  # Ship modes
y = ship_mode_counts.values  # Counts

plt.figure(figsize=(8, 6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=140)  # Add percentage labels
plt.title('Distribution of Ship Modes')  # Add a title
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle
plt.savefig("Distribution_of_Ship_Modes.jpg")
plt.show()

# Count plot for 'Ship Mode' with hue for 'Product Category'
plt.figure(figsize=(5, 4))
sns.countplot(x='Ship Mode', data=dataset, hue='Product Category')
plt.title('Count of Ship Modes by Product Category')
plt.xlabel('Ship Mode')
plt.ylabel('Count')
plt.savefig("Count_of_Ship_Modes_by_Product_Category.jpg")
plt.show()

# Count plot for 'Customer Segment'
plt.figure(figsize=(5, 4))
sns.countplot(x='Customer Segment', data=dataset)
plt.title('Count of Customer Segments')
plt.xlabel('Customer Segment')
plt.ylabel('Count')
plt.savefig("Count_of_Customer_Segments.jpg")
plt.show()

# Count plot for 'Product Category'
plt.figure(figsize=(5, 4))
sns.countplot(x='Product Category', data=dataset)
plt.title('Count of Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.savefig("Count_of_Product_Categories.jpg")
plt.show()

# Count plot for 'Product Category' with hue for 'Product Sub-Category'
plt.figure(figsize=(5, 4))
sns.countplot(x='Product Category', data=dataset, hue='Product Sub-Category')
plt.title('Count of Product Categories by Sub-Category')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.savefig("Count_of_Product_Categories_by_Sub_Category.jpg")
plt.show()

# Create a new column for 'Order year'
dataset['Order year'] = dataset['Order Date'].dt.year

# Count plot for 'Order year'
plt.figure(figsize=(5, 4))
sns.countplot(x='Order year', data=dataset)
plt.title('Count of Orders by Year')
plt.xlabel('Order Year')
plt.ylabel('Count')
plt.savefig("Count_of_Orders_by_Year.jpg")
plt.show()

# Bar plot for 'Product Category' and 'Profit'
plt.figure(figsize=(8, 6))
sns.barplot(x='Product Category', y='Profit', data=dataset, estimator='sum')
plt.title('Total Profit by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Profit')
plt.savefig("Total_Profit_by_Product_Category.jpg")
plt.show()

# Bar plot for 'Product Category' and 'Product Base Margin'
plt.figure(figsize=(8, 6))
sns.barplot(x='Product Category', y='Product Base Margin', data=dataset, estimator='sum')
plt.title('Total Product Base Margin by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Product Base Margin')
plt.savefig("Total_Product_Base_Margin_by_Product_Category.jpg")
plt.show()
