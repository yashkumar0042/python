
This tutorial assumes you have Python 3.x and `pandas` installed. If not, you can install `pandas` via:
```bash
pip install pandas
```

---

## 1. Importing pandas and Creating a Sample Dataset

First, you’ll need to import `pandas`. Here’s how you typically start:

```python
import pandas as pd
```

### 1.1. Creating a Simple DataFrame
Let’s create a small sample DataFrame. In real scenarios, you’ll be reading data from CSV, Excel, databases, etc. Here, we construct a DataFrame from a Python dictionary for illustration.

```python
import pandas as pd

# Sample employee dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Frida', 'George'],
    'Age': [24, 42, 18, 29, 35, 28, 41],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Chicago', 'New York'],
    'Salary': [70000, 90000, 45000, 81000, 62000, 52000, 92000],
    'Department': ['HR', 'Sales', 'IT', 'Finance', 'IT', 'HR', 'Sales']
}

df = pd.DataFrame(data)
print(df)
```

**Output might look like:**

```
       Name  Age         City  Salary Department
0     Alice   24     New York   70000         HR
1       Bob   42  Los Angeles   90000      Sales
2   Charlie   18      Chicago   45000         IT
3     Diana   29      Houston   81000    Finance
4     Ethan   35      Phoenix   62000         IT
5     Frida   28      Chicago   52000         HR
6    George   41     New York   92000      Sales
```

---

## 2. Reading and Writing Data

### 2.1. Reading from CSV
If you had a CSV file named `employees.csv`:
```python
df = pd.read_csv('employees.csv')
```

### 2.2. Writing to CSV
You can also export a DataFrame to CSV:
```python
df.to_csv('employees_output.csv', index=False)
```
(`index=False` to avoid writing the row numbers to the file.)

Similarly, you can use:
- `pd.read_excel('filename.xlsx')` / `df.to_excel('output.xlsx', index=False)`
- `pd.read_sql(query, connection)` to read from SQL databases (with the right drivers and connections).

---

## 3. Basic Data Inspection

Once you have a DataFrame, here are some common operations:

```python
# First few rows
print(df.head())    # By default, displays first 5 rows

# Last few rows
print(df.tail(3))   # Displays last 3 rows

# Shape of the DataFrame (rows, columns)
print(df.shape)

# Summary of columns, data types, and non-null counts
print(df.info())

# Basic statistics (mean, count, min, max, etc.) for numerical columns
print(df.describe())

# List columns
print(df.columns)
```

---

## 4. Indexing and Selecting Data

### 4.1. Selecting Columns
```python
# Select a single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Salary']])
```

### 4.2. Selecting Rows by Integer Position with `.iloc`
```python
# Single row by index
print(df.iloc[0])         # first row
print(df.iloc[-1])        # last row

# Multiple rows (first three)
print(df.iloc[0:3])
```

### 4.3. Selecting Rows by Labels with `.loc`
If you have a custom index (e.g., names or dates), you can use `.loc`:
```python
# Example: if "Name" was the index
df_indexed = df.set_index('Name')
print(df_indexed.loc['Alice'])
```

### 4.4. Boolean Indexing (Filtering Data)
```python
# Employees older than 30
older_than_30 = df[df['Age'] > 30]
print(older_than_30)

# Employees in IT department
it_dept = df[df['Department'] == 'IT']
print(it_dept)

# Multiple conditions (AND)
it_high_salary = df[(df['Department'] == 'IT') & (df['Salary'] > 50000)]
print(it_high_salary)

# Multiple conditions (OR)
ny_or_la = df[(df['City'] == 'New York') | (df['City'] == 'Los Angeles')]
print(ny_or_la)
```

---

## 5. Data Cleaning and Handling Missing Values

Let’s illustrate missing values. Suppose we have a dataset with some missing ages and salaries:

```python
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, None, 18, 29],
    'City': ['New York', None, 'Chicago', 'Houston'],
    'Salary': [70000, 90000, None, 81000]
}
df_na = pd.DataFrame(raw_data)

print(df_na)
```

### 5.1. Identifying Missing Data
```python
# Detect where values are NaN
print(df_na.isna())

# Count missing values per column
print(df_na.isna().sum())
```

### 5.2. Dropping Missing Values
```python
# Drop rows containing ANY missing values
df_na_dropped_any = df_na.dropna(how='any')

# Drop rows only if ALL values are missing
df_na_dropped_all = df_na.dropna(how='all')
```

### 5.3. Filling Missing Values
```python
# Fill with a specific value
df_na_filled = df_na.fillna({'Age': 0, 'City': 'Unknown', 'Salary': 0})

# Forward fill (fill NaN using last valid observation)
df_na_ffill = df_na.fillna(method='ffill')

# Backward fill
df_na_bfill = df_na.fillna(method='bfill')
```

---

## 6. Sorting, Renaming, and Changing Data

### 6.1. Sorting
```python
# Sort by a single column
df_sorted = df.sort_values(by='Salary', ascending=False)

# Sort by multiple columns
df_sorted_multi = df.sort_values(by=['Department', 'Age'], ascending=[True, False])
```

### 6.2. Renaming Columns
```python
df_renamed = df.rename(columns={'Name': 'EmployeeName', 'Salary': 'AnnualSalary'})
print(df_renamed.columns)
```

### 6.3. Adding or Modifying Columns
```python
# Add a new column that calculates some metric
df['SalaryUSD'] = df['Salary']  # example: assume Salary is already in USD

# We can also do calculations
df['SalaryInThousands'] = df['Salary'] / 1000
```

### 6.4. Dropping Columns
```python
df_dropped = df.drop(columns=['SalaryInThousands'])
```

---

## 7. Grouping and Aggregation

Grouping and aggregating are powerful for summarizing data. For instance, if we want to see average salary by department:

```python
dept_salary = df.groupby('Department')['Salary'].mean()
print(dept_salary)
```

We can also aggregate multiple statistics simultaneously:

```python
dept_stats = df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max'],
    'Age': 'mean'
})
print(dept_stats)
```

This will return a hierarchical column index, which can be flattened if desired:

```python
dept_stats.columns = ['_'.join(col) for col in dept_stats.columns]
print(dept_stats)
```

---

## 8. Merging and Joining DataFrames

Let’s create two DataFrames that share a key and merge them:

```python
employees = pd.DataFrame({
    'EmpID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['HR', 'Sales', 'IT', 'Finance']
})

salaries = pd.DataFrame({
    'EmpID': [1, 2, 3, 5],
    'Salary': [70000, 90000, 45000, 50000]
})

# Inner Join on EmpID
merged_inner = pd.merge(employees, salaries, on='EmpID', how='inner')
print(merged_inner)

# Left Join
merged_left = pd.merge(employees, salaries, on='EmpID', how='left')
print(merged_left)

# Right Join
merged_right = pd.merge(employees, salaries, on='EmpID', how='right')
print(merged_right)

# Outer Join
merged_outer = pd.merge(employees, salaries, on='EmpID', how='outer')
print(merged_outer)
```

---

## 9. Pivot Tables

Pivot tables let you reshape data:

```python
pivot = df.pivot_table(
    values='Salary', 
    index='Department', 
    columns='City', 
    aggfunc='mean'
)
print(pivot)
```

This shows the **average salary** for each **(Department, City)** combination.

---

## 10. Working with Dates and Times

If you have a column with dates, you can convert it to a datetime type:

```python
# Sample data with dates
data_dates = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'JoinDate': ['2021-01-15', '2020-12-01', '2021-03-10', '2022-07-20'],
    'Salary': [70000, 90000, 45000, 81000]
}
df_dates = pd.DataFrame(data_dates)

# Convert JoinDate to datetime
df_dates['JoinDate'] = pd.to_datetime(df_dates['JoinDate'])
print(df_dates.info())

# Extract year, month, day as separate columns
df_dates['JoinYear'] = df_dates['JoinDate'].dt.year
df_dates['JoinMonth'] = df_dates['JoinDate'].dt.month
df_dates['JoinDay'] = df_dates['JoinDate'].dt.day

print(df_dates)
```

---

## 11. Advanced: Applying Functions and Transformations

### 11.1. Using `.apply()`
```python
def categorize_age(age):
    if age < 25:
        return 'Young'
    elif age < 35:
        return 'Mid'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(categorize_age)
```

### 11.2. Vectorized String Operations
You can apply vectorized string methods on columns of type `object` (strings):

```python
# Make all names uppercase
df['Name'] = df['Name'].str.upper()

# Check if City contains "New"
df['IsNewCity'] = df['City'].str.contains('New')
```

### 11.3. Lambda Functions
```python
df['SalaryRange'] = df['Salary'].apply(lambda x: 'High' if x > 80000 else 'Low/Medium')
```

---

## 12. Visualization (Basic)

`pandas` integrates with `matplotlib` for quick plots. For example:

```python
import matplotlib.pyplot as plt

# Histogram of Ages
df['Age'].plot(kind='hist', bins=5, title='Age Distribution')
plt.show()

# Bar plot of average salary by department
dept_avg_salary = df.groupby('Department')['Salary'].mean()
dept_avg_salary.plot(kind='bar', title='Average Salary by Department')
plt.show()
```

> **Important:** If you’re running in a Jupyter notebook, add `%matplotlib inline` at the top for inline display.

---

## 13. Putting It All Together

Here’s a short script that **reads** a CSV (pretend `employees.csv`), **cleans** it, **aggregates** it, and **plots** a result:

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the dataset
df = pd.read_csv('employees.csv')  # Suppose it has columns: Name, Age, City, Salary, Department

# 2. Clean data: drop rows where Name or Department is missing
df.dropna(subset=['Name', 'Department'], inplace=True)

# 3. Convert any date columns if necessary
# df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 4. Filter data to relevant subset: employees in certain departments
df = df[df['Department'].isin(['HR', 'Sales', 'IT', 'Finance'])]

# 5. Group by Department and find mean salary
dept_salary = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)

# 6. Plot the average salary by department
dept_salary.plot(kind='bar', title='Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()
```

---

## 14. Sample “Database” Approach

Although pandas often works with files (CSV, Excel, JSON) or direct DB connections, you can also emulate or connect to an actual SQL database. For example, you could do:

```python
import sqlite3
import pandas as pd

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Create a table in the SQLite database
df.to_sql('employees', conn, index=False)

# Run a SQL query and load into a new DataFrame
df_from_db = pd.read_sql_query("SELECT * FROM employees WHERE Salary > 60000", conn)

print(df_from_db)
```

This approach is useful if you have structured data in SQL or if you want to combine SQL and pandas functionality.

---

# Conclusion

You now have a broad overview of how to go from **basic** to **advanced** with pandas:

1. **Reading / Writing Data** from different file formats.
2. **Inspecting and Summarizing** DataFrames.
3. **Cleaning and Transforming** data (missing values, renaming columns, creating new columns).
4. **Filtering and Indexing** data for subsetting.
5. **Aggregating and Grouping** (groupby, pivot tables).
6. **Joining / Merging** multiple tables.
7. **Working with Time Series** and datetime transformations.
8. **Applying functions, vectorized string operations** for advanced transformations.
9. **Visualizing** data directly from pandas, backed by `matplotlib`.
10. **Interfacing with Databases** (SQL, SQLite).
