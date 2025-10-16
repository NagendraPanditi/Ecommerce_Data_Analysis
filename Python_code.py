import pandas as pd 
df = pd.read_csv('Ecommerce_DS.csv')
print("Data Loaded Successfully")
print(f"Rows:{df.shape[0]}, Colums:{df.shape[1]}")
print("\n Preview of Dataset")
print(df.head())

#remove decimals to all numaruic columns
df['Discount Amount (INR)'] = df['Discount Amount (INR)'].astype(int)
df['Gross Amount(Before Discount)'] = df['Gross Amount(Before Discount)'].astype(int)
df['Net Amount(After Discount)'] = df['Net Amount(After Discount)'].astype(int)

# Converting the 'purchese Date' column to datetime format
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], format="%d-%m-%Y %H:%M")  

#add new column Discount_Percent
df['Discount_Percentage'] = (df['Discount Amount (INR)'] / df['Gross Amount(Before Discount)']) * 100
df['Discount_Percentage'] = df['Discount_Percentage'].astype(int)

#add new column month and year from purcchese date
df['Month'] = df['Purchase Date'].dt.month_name()
df['Year'] = df['Purchase Date'].dt.year

print("\n new columns added successfully")

#statement to fake Transaction ID
df['Transaction ID'] = ['TID' + str(i).zfill(5) for i in range(1, len(df) + 1)]
print("\n Transaction ID added successfully")

#check for duplicate transaction ID
duplicate_count = df.duplicated(subset=['Transaction ID']).sum()
print(f"\n Number of duplicate Transaction IDs: {duplicate_count}")

#check data types of each column
print("\n Data Types of each column:")
print(df.dtypes)

#check for missing values
missing_values = df.isnull().sum()
print("\n Missing Values in each column:")
print(missing_values)

#check for datatypes and struture
print(df.info())
print("\n Updated Data Info")
new_data = df.head()
print(new_data)

df.to_csv('Ecommerce_Dataset.csv', index=False)


