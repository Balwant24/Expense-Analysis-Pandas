import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")
print(df)

# Display basic information about the DataFrame
df.info()

# Checking for missing values
print(df.isnull().sum())

#Cleaning data: Filling missing values with the mean of the column
df["Amount"].fillna(0, inplace=True)
print(df.isnull().mean())
print("\nAfter filling missing values:")
print(df)

#removing duplicates
df = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df)

# Total expenses
total_expenses = df["Amount"].sum()
print(f"\nTotal Expenses: {total_expenses}")

#Average expense
average_expense = df["Amount"].mean()
print(f"Average Expense: {average_expense}")

# Maximum expense
max_expense = df["Amount"].max()
print(f"Maximum Expense: {max_expense}")

# Minimum expense
min_expense = df["Amount"].min()    
print(f"Minimum Expense: {min_expense}")

# Expenses by Category
expenses_by_category = df.groupby("Category")["Amount"].sum()
print("\nExpenses by Category:")
print(expenses_by_category)

#plotting expenses by category
plt.figure
expenses_by_category.plot(kind='bar', title='Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Total Amount')
plt.show()

#Highest expense category
highest_spending_category = df.groupby("Category")["Amount"].sum().idxmax()
print(highest_spending_category)

#Payment Method Analysis
payment_mode_expense = df.groupby("Payment_Mode")["Amount"].sum()
print("\nExpenses by Payment Mode:")
print(payment_mode_expense)

#plotting expenses by payment mode
plt.figure()
payment_mode_expense.plot(kind='bar', title='Expenses by Payment Mode')
plt.xlabel('Payment_Mode')
plt.ylabel('Total Amount')
plt.show()

# Exporting the cleaned and analyzed data to a new CSV file
df.to_csv("Analyzed_Expenses.csv")

   
