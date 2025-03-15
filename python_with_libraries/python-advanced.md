Below is an **expanded, two-day curriculum** featuring **detailed theoretical notes** and **real-world coding examples** for each topic. Each topic includes an explanation of concepts, plus **practical use-cases** that illustrate how these concepts might be applied in real-life scenarios. Finally, you'll find **coding labs** with **hands-on examples**.

---

# **Day 1: Python Core (4 Hours)**

## **1. Introduction to Python**

### **Theory**

1. **What is Python?**  
   - **High-level, interpreted language**: Python code is executed line by line.  
   - **Dynamically typed**: You don’t need to explicitly declare variable types.  
   - **Multipurpose**: Used for web development, data science, automation, scripting, etc.

2. **Why Python?**  
   - **Readability**: A clean and straightforward syntax that is beginner-friendly.  
   - **Large Community and Ecosystem**: Vast libraries for data science, AI, web dev, etc.  
   - **Portability**: Runs on multiple platforms without much change to code.

3. **Installation**  
   - **Anaconda**: Comes with Python, Jupyter Notebook, and many scientific libraries.  
   - **Jupyter Notebook**: Interactive environment for writing code, visualizing data, and documentation in one place.  
   - **VS Code**: Lightweight editor with Python extensions for debugging and code completion.

4. **Writing and Executing Python Scripts**  
   - **Interactive Mode** (REPL/Jupyter Notebook).  
   - **Script Mode** (`.py` files executed via terminal or an IDE).

### **Real-Time Use Case Example**

- **Automating File Organization**: You can write a Python script to go through a downloads folder, categorize files by type, and move them into separate folders automatically (e.g., images, documents, videos).
  
  ```python
  import os
  import shutil

  def organize_downloads(download_path):
      for filename in os.listdir(download_path):
          if filename.endswith(".jpg") or filename.endswith(".png"):
              shutil.move(os.path.join(download_path, filename),
                          os.path.join(download_path, "Images", filename))
          elif filename.endswith(".pdf") or filename.endswith(".docx"):
              shutil.move(os.path.join(download_path, filename),
                          os.path.join(download_path, "Documents", filename))
          # Add more conditions as needed
  
  organize_downloads("/Users/John/Downloads")
  ```

### **Lab**  

1. **Running Python Scripts in Jupyter Notebook**  
   - Launch Jupyter Notebook from Anaconda.  
   - Create a new notebook (`New > Python 3`).  
   - In the first cell, type:
     ```python
     print("Hello, Python!")
     ```
   - Run the cell to see the output.

2. **Basic Print Statements**  
   ```python
   name = "Alice"
   print("Hello, my name is", name)
   print(f"Hello, my name is {name}")  # Using f-string
   ```

---

## **2. Python Data Types & Variables**

### **Theory**

1. **Variables**  
   - **Dynamic Typing**: You can write `x = 10` and later `x = "Hello"` without type declarations.  
   - **Naming Conventions**: Use lowercase and underscores (e.g., `student_name`, `total_amount`).

2. **Data Types**  
   - **int**: e.g., `age = 25`  
   - **float**: e.g., `pi = 3.14`  
   - **str**: e.g., `city = "London"`  
   - **bool**: `True` or `False`  
   - **list**: e.g., `numbers = [1, 2, 3]` (mutable, ordered)  
   - **tuple**: e.g., `coords = (10, 20)` (immutable, ordered)  
   - **dict**: e.g., `person = {"name": "Alice", "age": 25}` (mutable, key-value pairs)  
   - **set**: e.g., `unique_items = {1, 2, 3}` (unordered, unique elements)

3. **Mutable vs. Immutable**  
   - **Mutable**: list, dict, set → can be changed in place.  
   - **Immutable**: int, float, string, tuple → cannot be changed in place; new objects are created on reassignment.

### **Real-Time Use Case Example**

- **Web Form Data Handling**: When receiving user data (like age, name, preferences) from a web form, you store them in variables or dictionaries. Then you can validate or process them further (for example, check if age is an integer, name is a string, etc.).

  ```python
  form_data = {
      "name": "Bob",
      "age": "30",  # from a text input
      "newsletter": "True"
  }
  
  # Convert data types
  form_data["age"] = int(form_data["age"])
  form_data["newsletter"] = (form_data["newsletter"] == "True")
  
  print(form_data)
  # {'name': 'Bob', 'age': 30, 'newsletter': True}
  ```

### **Lab**

1. **Creating and Manipulating Variables**  
   ```python
   age = 25
   height = 5.6
   student_name = "Alice"
   is_enrolled = True

   print(age, height, student_name, is_enrolled)
   ```

2. **Checking Types**  
   ```python
   print(type(age))           # <class 'int'>
   print(type(height))        # <class 'float'>
   print(type(student_name))  # <class 'str'>
   print(type(is_enrolled))   # <class 'bool'>
   ```

3. **Converting Data Types**  
   ```python
   age_str = str(age)
   height_int = int(height)
   print(age_str, type(age_str))     # '25' <class 'str'>
   print(height_int, type(height_int))  # 5 <class 'int'>
   ```

---

## **3. Operators and Expressions**

### **Theory**

1. **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//` (integer division), `%` (modulus), `**` (exponent).  
2. **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`.  
3. **Logical Operators**: `and`, `or`, `not`.  
4. **Assignment Operators**: `=`, `+=`, `-=`, etc.  
5. **Identity Operators**: `is`, `is not` (checks if two references point to the same object).  
6. **Membership Operators**: `in`, `not in` (checks if an element is in a sequence).

### **Real-Time Use Case Example**

- **Shopping Cart Calculation**: Summing prices, applying discounts, checking if a coupon code is valid, and verifying membership status for additional discounts.

  ```python
  total_price = 100
  discount_code = "SUMMER21"
  is_member = True

  if discount_code == "SUMMER21" and is_member:
      total_price *= 0.8  # 20% off for members
  elif discount_code == "SUMMER21":
      total_price *= 0.9  # 10% off

  print("Final Price:", total_price)
  ```

### **Lab**

1. **Arithmetic and Comparison**  
   ```python
   a, b = 10, 3
   print("Addition:", a + b)         # 13
   print("Floor Division:", a // b)  # 3
   print("Exponent:", a ** b)        # 1000
   print("Is a > b?", a > b)         # True
   ```

2. **Logical Expressions**  
   ```python
   x = 5
   y = 2
   result = (x > 0 and y < 3)
   print(result)  # True
   ```

---

## **4. Control Flow Statements**

### **Theory**

1. **Conditional Statements**  
   ```python
   if condition:
       # code
   elif condition2:
       # code
   else:
       # code
   ```
2. **For Loop**: Iterate over lists, tuples, dictionaries.  
3. **While Loop**: Repeats until a condition is false.

### **Real-Time Use Case Example**

- **Batch Processing Files**:  
  ```python
  import os

  directory = "/path/to/files"
  for filename in os.listdir(directory):
      if filename.endswith(".csv"):
          print("Found a CSV file:", filename)
      else:
          print("Not a CSV file:", filename)
  ```

- **While Loop for Retrying**  
  ```python
  attempts = 3
  while attempts > 0:
      password = input("Enter password: ")
      if password == "secret":
          print("Access granted!")
          break
      else:
          attempts -= 1
          print("Wrong password, try again!")
  ```

### **Lab**

1. **Writing Programs Using Loops and Conditions**  
   ```python
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       if num % 2 == 0:
           print(num, "is even")
       else:
           print(num, "is odd")
   ```

2. **Using While Loop**  
   ```python
   count = 5
   while count > 0:
       print("Countdown:", count)
       count -= 1
   print("Liftoff!")
   ```

---

## **5. Functions & Modules**

### **Theory**

1. **Defining Functions**  
   ```python
   def function_name(param1, param2="default"):
       # code
       return result
   ```
2. **Function Arguments**: positional, keyword, default, variable-length (`*args`, `**kwargs`).  
3. **Lambda Functions** (anonymous functions):  
   ```python
   square = lambda x: x * x
   ```
4. **Importing and Using Modules**  
   - Built-in modules: `math`, `random`.  
   - Custom modules: your own `.py` files.

### **Real-Time Use Case Example**

- **Reusable Utility Functions**:  
  ```python
  # math_utils.py
  def add(a, b):
      return a + b

  def multiply(a, b):
      return a * b
  ```

  ```python
  # main.py
  import math_utils
  result = math_utils.add(5, 10)
  print(result)  # 15
  ```

- **Randomizing Game Events**:  
  ```python
  import random

  def roll_dice():
      return random.randint(1, 6)

  print(roll_dice())
  ```

### **Lab**

1. **Creating Custom Functions**  
   ```python
   def greet(name="Guest"):
       return f"Hello, {name}!"

   print(greet("Alice"))
   print(greet())
   ```
2. **Using Built-in Modules**  
   ```python
   import math
   import random

   print("Square root of 16:", math.sqrt(16))
   print("Random number 1-10:", random.randint(1, 10))
   ```

---

## **6. File Handling**

### **Theory**

1. **Reading and Writing Files**  
   - `open(filename, mode)` → returns a file object.  
   - **Modes**:  
     - `r` (read),  
     - `w` (write, truncates existing file),  
     - `a` (append),  
     - `r+` (read/write).  
2. **Using `with open()`**  
   - Ensures the file is properly closed after usage.

### **Real-Time Use Case Example**

- **Logging System**: Appending log messages to a file every time an event occurs (e.g., user login).

  ```python
  def log_event(message, log_file="events.log"):
      with open(log_file, "a") as f:
          f.write(message + "\n")

  log_event("User Alice logged in.")
  log_event("User Bob changed password.")
  ```

### **Lab**

1. **Creating, Reading, and Writing Text Files**  
   ```python
   # Writing a file
   with open("sample.txt", "w") as file:
       file.write("Hello, Python!\nThis is a file handling demo.")

   # Reading a file
   with open("sample.txt", "r") as file:
       content = file.read()
       print("File Content:\n", content)
   ```

---

## **7. Exception Handling**

### **Theory**

1. **try-except-finally**  
   - `try`: code that might raise an exception.  
   - `except`: handle the exception.  
   - `finally`: code that runs regardless of an exception.  
2. **raise** to trigger exceptions manually.

### **Real-Time Use Case Example**

- **User Input Validation**: If user enters a value that can’t be converted to int, handle `ValueError`.

  ```python
  def get_user_age():
      try:
          age = int(input("Enter your age: "))
          return age
      except ValueError:
          print("Invalid age. Please enter a number.")
          return None
  ```

### **Lab**

1. **Implementing Exception Handling**  
   ```python
   def safe_division(a, b):
       try:
           return a / b
       except ZeroDivisionError:
           print("Error: Cannot divide by zero!")
           return None
       finally:
           print("Operation attempted.")

   print(safe_division(10, 0))
   print(safe_division(10, 2))
   ```

---

# **Day 2: Python Libraries (4 Hours)**

## **1. NumPy – Numerical Computing (1 Hour)**

### **Theory**

1. **Introduction to NumPy**  
   - **ndarray**: core data structure for fast array operations.  
   - **Vectorized Operations**: more efficient than Python lists due to C-level optimizations.

2. **Creating NumPy Arrays**  
   ```python
   import numpy as np
   arr = np.array([1, 2, 3])
   arr_zeros = np.zeros((2, 3))
   arr_ones = np.ones((3, 3))
   arr_arange = np.arange(0, 10, 2)
   ```

3. **Array Indexing and Slicing**  
   - Similar to list slicing, but can handle multiple dimensions (`arr[1:, :2]`, etc.).

4. **Basic Array Operations**  
   - Element-wise: `+`, `-`, `*`, `/`, and functions like `np.sum(arr)`, `np.mean(arr)`.

5. **Reshaping and Broadcasting**  
   - `arr.reshape(new_shape)` to change shape without changing data.  
   - Broadcasting allows arithmetic between arrays of different shapes if compatible.

### **Real-Time Use Case Example**

- **Image Processing**: An image can be seen as a 3D NumPy array (height × width × color_channels). You can manipulate pixel values or apply filters.

  ```python
  import numpy as np
  # Simulating a grayscale image of 2x2
  img = np.array([[100, 150],
                  [200, 250]])
  # Increase brightness by 50 for all pixels
  brighter_img = img + 50
  print(brighter_img)
  ```

### **Lab**

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
print("Reshaped:\n", reshaped)

# 4. Broadcasting
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print("Broadcast result:\n", a + b)
```

---

## **2. Pandas – Data Manipulation (1 Hour)**

### **Theory**

1. **Introduction to Pandas**  
   - Built on NumPy, optimizes tabular data operations.  
   - **DataFrame**: 2D labeled data structure with columns of potentially different types.

2. **Creating and Reading DataFrames**  
   ```python
   import pandas as pd
   df = pd.read_csv("data.csv")
   ```

3. **Selecting, Filtering, and Sorting Data**  
   - `df[["col1", "col2"]]`, `df.loc[row_indexer, col_indexer]`, boolean indexing, etc.

4. **Handling Missing Values**  
   - `df.dropna()` or `df.fillna(value)`.

5. **Grouping and Aggregating**  
   - `df.groupby("Category")["Value"].mean()` for summary.

### **Real-Time Use Case Example**

- **Sales Data Analysis**: Reading a CSV of daily sales, grouping by month, and computing totals.

  ```python
  import pandas as pd

  sales_df = pd.read_csv("daily_sales.csv")
  monthly_sales = sales_df.groupby("Month")["Sales"].sum()
  print("Monthly Sales:\n", monthly_sales)
  ```

### **Lab**

```python
import pandas as pd

# 1. Reading CSV
df = pd.read_csv("employee_data.csv")
print("Head:\n", df.head())

# 2. Filtering
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

## **3. Matplotlib – Data Visualization (1 Hour)**

### **Theory**

1. **Introduction to Matplotlib**  
   - **pyplot** interface for quick plotting.  
   - Common plots: **line**, **bar**, **scatter**, **histogram**.

2. **Customizing Plots**  
   - Titles: `plt.title("...")`  
   - Labels: `plt.xlabel("...")`, `plt.ylabel("...")`  
   - Legends: `plt.legend()`  
   - Saving: `plt.savefig("plot.png")`

### **Real-Time Use Case Example**

- **Monitoring Website Traffic**: Plot a line chart of daily visitors to see trends over time.

  ```python
  import matplotlib.pyplot as plt

  days = [1, 2, 3, 4, 5]
  visitors = [100, 120, 80, 150, 200]

  plt.plot(days, visitors)
  plt.title("Daily Website Visitors")
  plt.xlabel("Day")
  plt.ylabel("Number of Visitors")
  plt.show()
  ```

### **Lab**

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Line chart
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Scatter plot
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
plt.scatter(x_rand, y_rand)
plt.title("Random Scatter Plot")
plt.show()

# 3. Bar plot
categories = ["A", "B", "C"]
values = [10, 20, 15]
plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.show()
```

---

## **4. Scikit-Learn – Machine Learning Basics (1 Hour)**

### **Theory**

1. **Introduction to Scikit-learn**  
   - Provides machine learning algorithms in a consistent API.  
   - Key Steps: 
     1. **Data loading**,  
     2. **Preprocessing**,  
     3. **Model fitting**,  
     4. **Prediction**,  
     5. **Evaluation**.

2. **Loading Datasets**  
   - Built-in (e.g., `load_iris`, `load_breast_cancer`) or external CSV.

3. **Data Preprocessing**  
   - `train_test_split` to partition data.  
   - **Scaling** (e.g., `StandardScaler` or `MinMaxScaler`).

4. **Simple Linear Regression Example**  
   - `LinearRegression()` from `sklearn.linear_model`.  
   - Evaluate with MSE or R².

### **Real-Time Use Case Example**

- **House Price Prediction**: Using features like square footage, number of bedrooms, and location to predict house prices.  
  - Steps: gather data in a DataFrame, split into train/test sets, fit a regression model, predict, and evaluate.

```python
# Pseudocode:
# 1. df = pd.read_csv("house_data.csv")
# 2. X = df[["sqft", "bedrooms", "bathrooms"]]
# 3. y = df["price"]
# 4. X_train, X_test, y_train, y_test = train_test_split(...)
# 5. model.fit(X_train, y_train)
# 6. predictions = model.predict(X_test)
# 7. measure accuracy
```

### **Lab**

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# 1. Load Iris dataset
iris = load_iris()
X = iris.data  # sepal length, sepal width, petal length, petal width
y = iris.target # species (0, 1, or 2)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Instantiate model
model = LinearRegression()

# 4. Fit model
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)
print("Predictions:", predictions[:5])
print("Actual    :", y_test[:5])

# 6. Evaluate with R^2 score
score = model.score(X_test, y_test)
print("R^2 score:", score)
```

> *Note:* Using LinearRegression on a classification dataset (Iris) is not typically correct from a machine-learning standpoint, but it demonstrates the mechanics of model fitting and evaluation. For classification, you’d use a classifier like `LogisticRegression` or `DecisionTreeClassifier`.

---

# **Conclusion and Next Steps**

By the end of these two days:

- You’ll have a **solid grasp of Python fundamentals**: data types, loops, functions, modules, file handling, and exception handling.  
- You’ll also understand the basics of **NumPy, pandas, Matplotlib, and scikit-learn** for data science tasks:
  1. **NumPy** for fast, vectorized operations on arrays.  
  2. **pandas** for reading, cleaning, and transforming tabular data.  
  3. **Matplotlib** for visualizing data and insights.  
  4. **scikit-learn** for a quick start in machine learning.

**Next Steps** might include:
- **Advanced Python topics**: OOP, decorators, generators, threading, asynchronous programming.  
- **Deep dive into data science**: Feature engineering, model optimization, hyperparameter tuning, cross-validation, advanced ML algorithms.  
- **Web frameworks**: Flask or Django for creating web apps with Python backends.  
- **Deployment**: Containerization with Docker, or cloud services like AWS, Azure, or GCP.

With these fundamentals, you’re well on your way to building robust Python applications and data science pipelines. Good luck and happy coding!
