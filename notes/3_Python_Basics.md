# 3. Python Basics

Python is a versatile programming language known for its readability and simplicity. In this guide, we'll cover fundamental Python concepts and provide examples for each topic.

## Keywords

Keywords are reserved words in Python, and they have specific meanings and purposes. You cannot use keywords as identifiers (variable or function names). Here are some common keywords in Python:

```python
# Example of Python keywords
import keyword

print(keyword.kwlist)
```

**Output:**
```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## Identifiers

Identifiers are names given to variables, functions, classes, or other objects in Python. They must follow certain rules:

- They can only start with letters (a-z, A-Z) or underscores (_).
- The rest of the identifier can contain letters, underscores, and digits (0-9).
- Python is case-sensitive, so `myVar` and `myvar` are different identifiers.

Example:

```python
# Examples of valid identifiers
my_variable = 42
my_function = lambda x: x * 2
MyClass = MyClass()
```

## Comments

Comments in Python are used for documentation and code explanation. They are not executed by the interpreter. Python supports both single-line and multi-line comments.

```python
# This is a single-line comment

'''
This is a
multi-line comment
'''

# Example of a comment explaining code
result = 5 + 3  # Calculate the sum of 5 and 3
```

## Data Types

Python supports various data types, including:

- **Integers (`int`):** Whole numbers, e.g., 5, -7, 0.
- **Floats (`float`):** Numbers with a decimal point, e.g., 3.14, -0.5.
- **Strings (`str`):** Sequences of characters enclosed in single or double quotes, e.g., "Hello, World!".
- **Boolean (`bool`):** Represents `True` or `False`.
- **Lists (`list`):** Ordered collections of items, e.g., [1, 2, 3].
- **Tuples (`tuple`):** Ordered, immutable collections, e.g., (1, 2, 3).
- **Sets (`set`):** Unordered collections of unique elements, e.g., {1, 2, 3}.
- **Dictionaries (`dict`):** Key-value pairs, e.g., {'name': 'John', 'age': 30}.

Examples:

```python
# Examples of data types
integer_variable = 42
float_variable = 3.14
string_variable = "Hello, World!"
boolean_variable = True
list_variable = [1, 2, 3]
tuple_variable = (4, 5, 6)
set_variable = {7, 8, 9}
dictionary_variable = {'name': 'John', 'age': 30}
```

## Variables

Variables are used to store data values. In Python, you don't need to declare a variable's data type explicitly. Python infers the data type based on the value assigned to the variable.

Example:

```python
# Assigning values to variables
x = 5
name = "Alice"
is_valid = True
```

## Operators

Operators are used to perform operations on variables and values. Python supports various types of operators:

- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `%`, `**` (exponentiation), `//` (floor division).
- **Comparison Operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Logical Operators:** `and`, `or`, `not`.
- **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`.
- **Identity Operators:** `is`, `is not` (used to compare object identities).
- **Membership Operators:** `in`, `not in` (used to check membership in sequences like lists or strings).

Examples:

```python
# Arithmetic Operators
result = 5 + 3  # Addition
remainder = 10 % 3  # Modulus

# Comparison Operators
is_equal = (5 == 3)  # False

# Logical Operators
logical_result = (True and False)  # False

# Assignment Operators
x = 5
x += 3  # x is now 8

# Identity Operators
a = [1, 2, 3]
b = a
is_same = (a is b)  # True

# Membership Operators
my_list = [1, 2, 3]
is_member = (2 in my_list)  # True
```

These fundamental Python concepts form the building blocks for writing Python programs. As you continue learning and practicing Python, you'll use these concepts extensively to create more complex and functional code.
