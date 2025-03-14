Below is a **two-day curriculum** (each day is 4 hours) covering core Python fundamentals (**Day 1**) and essential data-science libraries (**Day 2**). Each section features **theory** (concepts, definitions), **real-world use examples**, and a **lab** (hands-on practice) to reinforce learning.

---

## **Day 1: Python Core (4 Hours)**

### **1. Introduction to Python**

#### **Theory**
- **What is Python?**  
  Python is a high-level, interpreted, and dynamically typed programming language. It emphasizes readability and simplicity, making it a popular choice for beginners and experts alike.

- **Why Python?**  
  1. **Ease of use and readability** – clean, English-like syntax.  
  2. **Large standard library and community** – supports web development, data science, automation, etc.  
  3. **Cross-platform** – runs on Windows, macOS, Linux.  
  4. **Extensive data science and machine learning ecosystem** (NumPy, pandas, scikit-learn, TensorFlow, etc.).

- **Installation (Anaconda, Jupyter Notebook, VS Code)**  
  1. **Anaconda**: A distribution that comes with Python, Jupyter Notebook, and many data science libraries pre-installed.  
  2. **Jupyter Notebook**: Web-based interactive environment. Ideal for data exploration and quick prototyping.  
  3. **VS Code**: A lightweight yet powerful code editor with extensions for Python development.

- **Writing and Executing Python Scripts**  
  1. **Interactive Mode**: Launch Python shell or use Jupyter Notebook cells.  
  2. **Script Mode**: Write `.py` files and run them via command line (`python script.py`) or within an IDE.

#### **Real Use Examples**  
- **Automation**: Writing simple Python scripts to rename files in bulk or scrape a website.  
- **Data Analysis**: Loading and cleaning CSV files in Jupyter Notebook.  
- **Web Development**: Using frameworks like Django or Flask to build apps.

#### **Lab**  
1. **Running Python scripts in Jupyter Notebook**  
   - Open Anaconda Navigator and launch Jupyter Notebook.  
   - Create a new Notebook (`.ipynb`) and run a cell with `print("Hello, Python!")`.  

2. **Basic print statements**  
   ```python
   print("Hello World")
   name = "Alice"
   print("Hello, my name is", name)
   ```
   - Observe how Jupyter prints results immediately after each cell.

---

### **2. Python Data Types & Variables**

#### **Theory**
- **Variables**  
  - Containers for storing data. Python variables are dynamically typed, meaning you don’t need to declare the type.  
  - Naming conventions (PEP 8): use lowercase letters, underscores for readability (e.g., `student_age`, `total_sum`).

- **Data Types**  
  1. **int** – integer values, e.g., `x = 10`.  
  2. **float** – floating-point numbers, e.g., `price = 3.14`.  
  3. **string** – text data, enclosed in quotes, e.g., `name = "John"`.  
  4. **bool** – boolean, `True` or `False`.  
  5. **list** – mutable sequence, e.g., `numbers = [1, 2, 3]`.  
  6. **tuple** – immutable sequence, e.g., `point = (10, 20)`.  
  7. **dict** – dictionary (key-value pairs), e.g., `person = {"name": "Alice", "age": 30}`.  
  8. **set** – unordered collection of unique items, e.g., `unique_nums = {1, 2, 2, 3}`.

- **Mutable vs. Immutable Types**  
  - **Mutable**: can be changed in place (lists, dictionaries, sets).  
  - **Immutable**: cannot be changed in place (int, float, string, tuple).

#### **Real Use Examples**  
- Storing **configuration data** in dictionaries.  
- Keeping a **list of tasks** for a to-do app.  
- Using **immutable tuples** to represent geographic coordinates.

#### **Lab**  
1. **Creating and manipulating variables**  
   ```python
   age = 25
   name = "Alice"
   is_student = True
   ```
2. **Checking types with `type()`**  
   ```python
   print(type(age))        # <class 'int'>
   print(type(name))       # <class 'str'>
   print(type(is_student)) # <class 'bool'>
   ```
3. **Converting data types**  
   ```python
   # From int to float
   age_float = float(age)

   # From int to string
   age_str = str(age)

   print(age_float, type(age_float))
   print(age_str, type(age_str))
   ```

---

### **3. Operators and Expressions**

#### **Theory**
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`.  
  - Example: `5 + 3 = 8`, `5 ** 2 = 25`.

- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`.  
  - Example: `5 > 3` → `True`.

- **Logical Operators**: `and`, `or`, `not`.  
  - Example: `(5 > 3) and (2 < 1)` → `False`.

- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, etc.  
  - Example: `x += 2` is equivalent to `x = x + 2`.

- **Identity Operators**: `is`, `is not`.  
  - Check if two references point to the same object.  
  - Example: `x is y`.

- **Membership Operators**: `in`, `not in`.  
  - Check membership in sequences, e.g., `x in list`.

#### **Real Use Examples**  
- Calculating **discounted prices** in an e-commerce application.  
- Checking if a **user input** is in an allowed list of commands.  
- Creating **compound conditions** for loan eligibility (`age > 18 and income > 30000`, etc.).

#### **Lab**  
1. **Writing expressions using different operators**  
   ```python
   a = 10
   b = 3

   print(a + b)     # 13
   print(a / b)     # 3.333...
   print(a // b)    # 3
   print(a ** b)    # 1000
   ```
2. **Evaluating logical expressions**  
   ```python
   print(a > 5 and b < 5)    # True
   print(a == 10 or b == 5)  # True
   print(not (b == 3))       # False
   ```

---

### **4. Control Flow Statements**

#### **Theory**
- **Conditional Statements**: `if`, `elif`, `else`.  
  - Syntax relies on indentation to define code blocks.
  ```python
  if condition:
      # code
  elif condition:
      # code
  else:
      # code
  ```

- **Looping**  
  1. **for loop**: iterate over a sequence (list, tuple, dict keys, etc.).  
     ```python
     for item in [1, 2, 3]:
         print(item)
     ```
  2. **while loop**: repeat until a condition is false.  
     ```python
     while condition:
         # code
     ```

- **Iterating over Lists, Dictionaries**  
  - Lists: `for element in my_list:`  
  - Dictionaries: `for key, value in my_dict.items():`

#### **Real Use Examples**  
- **Validating form inputs** (if certain fields are empty, return an error).  
- **Batch processing** files from a list or directory.  
- **Filtering** a dictionary of product data based on a threshold price.

#### **Lab**  
1. **Writing programs using loops and conditions**  
   ```python
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       if num % 2 == 0:
           print(num, "is even")
       else:
           print(num, "is odd")
   ```
2. **Using a while loop**  
   ```python
   count = 3
   while count > 0:
       print("Count:", count)
       count -= 1
   ```

---

### **5. Functions & Modules**

#### **Theory**
- **Defining Functions**  
  ```python
  def function_name(param1, param2="default"):
      # code
      return result
  ```
- **Function Arguments**  
  1. **Positional**: parameters must be in correct order.  
  2. **Keyword**: specify parameter names, e.g., `func(arg_name=value)`.  
  3. **Default**: if not provided, uses the default value.  
  4. **Variable-Length**: `*args` for non-keyword args, `**kwargs` for keyword args.

- **lambda Functions**  
  - Anonymous functions for concise operations.
  ```python
  square = lambda x: x * x
  ```
- **Importing and Using Modules**  
  - Built-in modules: `math`, `random`, etc.  
  - Custom modules: create `.py` files with functions or classes.

#### **Real Use Examples**  
- **Utility functions** for data processing (e.g., `clean_text(text)` in text analytics).  
- **Mathematical calculations** using the `math` module (e.g., `math.sqrt(x)`).  
- **Random sampling** in games or simulations with the `random` module.

#### **Lab**  
1. **Creating custom functions**  
   ```python
   def greet(name="Guest"):
       return f"Hello, {name}!"

   print(greet("Alice"))
   print(greet())
   ```
2. **Using built-in modules**  
   ```python
   import math

   num = 16
   print("Square root of 16:", math.sqrt(num))

   import random
   print("Random number between 1 and 10:", random.randint(1, 10))
   ```

---

### **6. File Handling**

#### **Theory**
- **Reading and Writing Files**  
  - `open(file, mode)` – returns a file object.  
  - **Common modes**: `'r'` (read), `'w'` (write, truncates file), `'a'` (append), `'r+'` (read/write).  

- **with open() as file**  
  - Automatically closes the file after exiting the block.  
  - Example:
    ```python
    with open("data.txt", "r") as f:
        content = f.read()
    ```

#### **Real Use Examples**  
- **Data logging**: writing logs to a `.txt` file.  
- **Configuration**: reading parameters from a text or JSON file.  
- **Batch data processing**: reading CSV lines and summarizing them.

#### **Lab**  
1. **Creating, Reading, and Writing Text Files**  
   ```python
   # Writing to a file
   with open("sample.txt", "w") as file:
       file.write("Hello, Python!\n")
       file.write("File handling demo.")

   # Reading from a file
   with open("sample.txt", "r") as file:
       content = file.read()
       print("File Content:\n", content)
   ```

---

### **7. Exception Handling**

#### **Theory**
- **try-except-finally**  
  - `try`: code that may raise an exception.  
  - `except`: handle specific or general exceptions.  
  - `finally`: execute code regardless of whether an exception occurred.

- **raise**  
  - Manually raise an exception for invalid states or data.

- **Handling Different Error Types**  
  - `ZeroDivisionError`, `ValueError`, `FileNotFoundError`, etc.

#### **Real Use Examples**  
- **Input validation**: if a user enters invalid data, raise `ValueError`.  
- **Network requests**: handle connection timeouts and other I/O errors.  
- **File reading**: gracefully handle missing files.

#### **Lab**  
1. **Implementing exception handling in Python scripts**  
   ```python
   def safe_division(a, b):
       try:
           result = a / b
       except ZeroDivisionError:
           print("Error: Cannot divide by zero!")
           return None
       else:
           return result
       finally:
           print("Division attempted.")

   print(safe_division(10, 0))
   print(safe_division(10, 2))
   ```

---

## **Day 2: Python Libraries (4 Hours)**

### **1. NumPy – Numerical Computing (1 Hour)**

#### **Theory**
- **Introduction to NumPy**  
  - Core library for scientific computing in Python.  
  - Provides **ndarray** (multi-dimensional arrays) with fast operations.

- **Creating NumPy Arrays**  
  ```python
  import numpy as np

  arr = np.array([1, 2, 3])
  arr_zeros = np.zeros((2, 3))
  arr_ones = np.ones((3, 3))
  arr_arange = np.arange(0, 10, 2)
  ```

- **Array Indexing and Slicing**  
  - Similar to Python lists, but more powerful for multi-dimensional data.

- **Basic Array Operations**  
  - Element-wise addition, subtraction, multiplication, division.  
  - Aggregation: `np.sum()`, `np.mean()`, `np.std()`, etc.

- **Reshaping and Broadcasting**  
  - `reshape()`, adjusting shape without changing data.  
  - Broadcasting rules allow operations on arrays with different shapes.

#### **Real Use Examples**  
- **Matrix operations**: linear algebra for solving systems of equations.  
- **Signal processing**: large arrays of numeric data (audio, sensor readings).  
- **Image processing**: images as 2D or 3D arrays (height × width × channels).

#### **Lab**
```python
import numpy as np

# 1. Creating arrays
arr = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]])

# 2. Element-wise operations
arr_doubled = arr * 2
print("Doubled:", arr_doubled)

# 3. Reshape
reshaped = arr.reshape((2, 2))
print("Reshaped to 2x2:\n", reshaped)

# 4. Broadcasting
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print("Broadcast result:\n", a + b)
```

---

### **2. Pandas – Data Manipulation (1 Hour)**

#### **Theory**
- **Introduction to Pandas**  
  - Built on NumPy, optimized for tabular data.  
  - **DataFrame**: 2D labeled data structure.

- **Creating and Reading DataFrames**  
  - From dictionaries, lists, or reading files (`read_csv`, `read_excel`).  
  ```python
  import pandas as pd
  df = pd.read_csv("data.csv")
  ```

- **Selecting, Filtering, and Sorting Data**  
  - `df[["col1", "col2"]]` or `df.loc[row_index, col_index]`.  
  - Boolean filtering: `df[df["Age"] > 30]`.  
  - Sorting with `.sort_values()`.

- **Handling Missing Values**  
  - `df.isnull()`, `df.dropna()`, `df.fillna()`.

- **Grouping and Aggregating**  
  - `df.groupby("Category")["Value"].mean()` for summary stats.

#### **Real Use Examples**  
- **Financial analysis**: reading CSVs of stock prices, grouping by date, calculating daily returns.  
- **Customer data**: merging multiple CSVs, cleaning duplicates, generating summary stats.  
- **Survey results**: filtering respondents by region, analyzing average responses.

#### **Lab**
```python
import pandas as pd

# 1. Reading a CSV
df = pd.read_csv("employee_data.csv")
print("Head:\n", df.head())

# 2. Filtering data
filtered = df[df["Salary"] > 50000]
print("High salary employees:\n", filtered)

# 3. Handling missing values
df["Department"] = df["Department"].fillna("Not Assigned")
df = df.dropna(subset=["Salary"])

# 4. Grouping
dept_salary = df.groupby("Department")["Salary"].mean()
print("Average salary by department:\n", dept_salary)
```

---

### **3. Matplotlib – Data Visualization (1 Hour)**

#### **Theory**
- **Introduction to Matplotlib**  
  - Base plotting library in Python.  
  - Usually used via `import matplotlib.pyplot as plt`.

- **Creating Basic Plots**  
  1. **Line Plot**: `plt.plot(x, y)`.  
  2. **Bar Plot**: `plt.bar(categories, values)`.  
  3. **Scatter Plot**: `plt.scatter(x, y)`.  
  4. **Histogram**: `plt.hist(data, bins=...)`.

- **Customizing Plots**  
  - Titles, labels, legends: `plt.title("...")`, `plt.xlabel("...")`, `plt.ylabel("...")`, `plt.legend()`.  
  - Saving plots: `plt.savefig("plot.png")`.

#### **Real Use Examples**  
- **Data exploration**: histogram of numeric columns to see distributions.  
- **Performance metrics**: bar charts for monthly sales or website visits.  
- **Scientific plots**: scatter plots for correlation in experimental data.

#### **Lab**
```python
import matplotlib.pyplot as plt

# 1. Line chart
years = [2018, 2019, 2020, 2021, 2022]
sales = [200, 250, 300, 350, 400]

plt.plot(years, sales)
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")
plt.show()

# 2. Scatter plot
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Random Scatter Plot")
plt.show()

# 3. Customized plot
categories = ["A", "B", "C"]
values = [10, 20, 15]
plt.bar(categories, values)
plt.title("Example Bar Plot")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
```

---

### **4. Scikit-Learn – Machine Learning Basics (1 Hour)**

#### **Theory**
- **Introduction to Scikit-learn**  
  - Comprehensive library for machine learning algorithms (classification, regression, clustering).  
  - Emphasizes a **consistent API** with `fit()`, `predict()`, `score()` methods.

- **Loading Datasets**  
  - Built-in datasets (Iris, Breast Cancer, Wine).  
  - `from sklearn.datasets import load_iris`.

- **Data Preprocessing**  
  1. **train_test_split** – to create training and testing sets.  
  2. **Feature scaling** – `StandardScaler`, `MinMaxScaler`.

- **Simple Linear Regression Example**  
  - Steps:  
    1. Split data.  
    2. Create model instance (`LinearRegression()`).  
    3. Fit model with training data.  
    4. Predict on test data.  
    5. Evaluate with metrics like MSE, R².

#### **Real Use Examples**  
- Predicting **house prices** with multiple features (square footage, location, etc.).  
- Classifying **emails** into spam vs. non-spam with logistic regression.  
- Clustering **customer segments** in marketing.

#### **Lab**
```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# 1. Load a dataset (for demonstration, we'll use Iris)
iris = load_iris()
X = iris.data  # features: sepal length, sepal width, etc.
y = iris.target  # target: species classes (0,1,2)

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Simple model: Linear Regression (even though Iris is typically classification)
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predictions
predictions = model.predict(X_test)
print("Predictions:", predictions[:5])
print("Actual values:", y_test[:5])

# 5. Checking performance
# For classification tasks, you might use accuracy_score or confusion_matrix.
# For regression, R-squared is available via model.score(X_test, y_test).
score = model.score(X_test, y_test)
print("R^2 score:", score)
```

> Even though Linear Regression isn’t ideal for a categorical target like in Iris, this lab demonstrates the basic scikit-learn workflow. In a real scenario, you would use a classification model (e.g., `LogisticRegression`, `DecisionTreeClassifier`, etc.) for Iris.

---

## **Summary**

By the end of **Day 1**, you will have:
- A solid foundation of **Python syntax**, data types, control flow, and error handling.
- Confidence in writing scripts to handle basic file operations and create reusable functions.

By the end of **Day 2**, you will:
- Understand how to use **NumPy** for numerical array operations.  
- Manipulate and analyze tabular data with **pandas**.  
- Create data visualizations with **Matplotlib**.  
- Implement a basic machine learning workflow with **scikit-learn**.

This two-day course sets the stage for more advanced topics like deep learning, big data processing, and specialized domain applications, but the fundamentals learned here are essential for any Python-based data analysis or development. 

Happy learning and coding!
