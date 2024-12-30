### Generative AI Learning Notes (Beginner to Advanced)

---

## **Phase 1: Python Fundamentals**

### **Topics**
#### 1. Data Types, Variables, Loops, and Conditionals
- **Data Types**: Python supports various data types, including:
  - `int`: Integer values (e.g., `5`, `-100`)
  - `float`: Floating-point numbers (e.g., `3.14`, `-0.01`)
  - `str`: Strings for textual data (e.g., "Hello")
  - `list`: Ordered collections (e.g., `[1, 2, 3]`)
  - `tuple`: Immutable ordered collections (e.g., `(1, 2, 3)`)
  - `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

- **Variables and Assignments**:
  ```python
  x = 10  # Assigning an integer
  name = "Alice"  # Assigning a string
  fruits = ["apple", "banana"]  # Assigning a list
  ```

- **Loops and Conditionals**:
  - **For Loop**:
    ```python
    for i in range(5):
        print("Iteration", i)
    ```

  - **While Loop**:
    ```python
    count = 0
    while count < 5:
        print("Count is", count)
        count += 1
    ```

  - **Conditionals**:
    ```python
    age = 18
    if age > 18:
        print("Adult")
    elif age == 18:
        print("Just turned adult")
    else:
        print("Minor")
    ```

#### 2. Functions, Modules, and File Handling
- **Functions**:
  - Functions encapsulate reusable code blocks.
  ```python
  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))
  ```

- **Modules**:
  - Use built-in or custom modules to organize code.
  ```python
  import math

  print(math.sqrt(16))  # Output: 4.0
  ```

- **File Handling**:
  ```python
  # Writing to a file
  with open("example.txt", "w") as file:
      file.write("Hello, World!")

  # Reading from a file
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)
  ```

#### 3. Object-Oriented Programming (OOP)
- **Key Concepts**:
  - **Class**: Blueprint for objects.
  - **Object**: Instance of a class.
  - **Attributes**: Variables within a class.
  - **Methods**: Functions within a class.

- **Example**:
  ```python
  class Car:
      def __init__(self, brand, model):
          self.brand = brand
          self.model = model

      def display_info(self):
          print(f"Car: {self.brand} {self.model}")

  my_car = Car("Toyota", "Corolla")
  my_car.display_info()
  ```

#### 4. NumPy Basics
- **NumPy** is essential for numerical computing.
  ```python
  import numpy as np

  arr = np.array([1, 2, 3])
  print(arr + 5)  # Output: [6, 7, 8]
  ```

### **Practice Labs**
1. **Calculator**:
   - Build a Python program that takes input for two numbers and performs basic operations (add, subtract, multiply, divide).

2. **Word Frequency Analyzer**:
   - Write a program to read a file and count the frequency of each word.

---

## **Phase 2: Machine Learning Basics**

### **Topics**
#### 1. Linear Algebra and Probability Basics
- **Key Concepts**:
  - **Vectors and Matrices**: Foundations for data representation.
  - **Dot Product**: Measures similarity between two vectors.
  - **Probability**: Includes conditional probability, Bayes’ theorem, and distributions (e.g., Gaussian).

- **Dot Product Example**:
  ```python
  import numpy as np

  v1 = np.array([1, 2])
  v2 = np.array([3, 4])
  print(np.dot(v1, v2))  # Output: 11
  ```

- **Probability Example**:
  ```python
  # Probability of event A given event B (P(A|B))
  P_A = 0.6  # Probability of A
  P_B_given_A = 0.8  # Probability of B given A
  P_B = 0.7  # Probability of B

  P_A_given_B = (P_B_given_A * P_A) / P_B
  print(P_A_given_B)
  ```

#### 2. Supervised Learning
- **Key Concepts**:
  - In supervised learning, the algorithm learns from labeled data to predict outputs.
  - Models: Linear regression, logistic regression, decision trees, support vector machines (SVMs).

- **Linear Regression**:
  ```python
  from sklearn.linear_model import LinearRegression

  X = [[1], [2], [3]]  # Features
  y = [2, 4, 6]  # Target
  model = LinearRegression().fit(X, y)
  print(model.predict([[4]]))  # Output: [8.]
  ```

- **Decision Trees**:
  ```python
  from sklearn.tree import DecisionTreeClassifier

  X = [[0, 0], [1, 1]]
  y = [0, 1]
  clf = DecisionTreeClassifier().fit(X, y)
  print(clf.predict([[2, 2]]))
  ```

#### 3. Unsupervised Learning
- **Key Concepts**:
  - Unsupervised learning deals with unlabeled data to find hidden patterns.
  - Models: KMeans, DBSCAN, PCA.

- **Clustering (KMeans)**:
  ```python
  from sklearn.cluster import KMeans
  import numpy as np

  X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
  kmeans = KMeans(n_clusters=2).fit(X)
  print(kmeans.labels_)
  ```

### **Practice Labs**
1. **Housing Prices**:
   - Load a dataset (e.g., Boston Housing) and build a regression model to predict prices.

2. **Customer Segmentation**:
   - Cluster customers using KMeans based on their purchasing behavior.

---

## **Phase 3: Deep Learning Foundations**

### **Topics**
#### 1. Neural Networks Basics
- **Key Concepts**:
  - **Perceptron**: Basic building block of neural networks.
  - **Activation Functions**: Sigmoid, ReLU, tanh.
  - **Loss Functions**: Measures the error (e.g., MSE, cross-entropy).
  - **Backpropagation**: Updates weights using gradient descent.

- **Perceptron Example**:
  ```python
  import numpy as np

  def sigmoid(x):
      return 1 / (1 + np.exp(-x))

  weights = np.array([0.5, -0.5])
  bias = 0.1
  inputs = np.array([1.0, 2.0])
  output = sigmoid(np.dot(weights, inputs) + bias)
  print(output)
  ```

#### 2. Frameworks
- **TensorFlow Example**:
  ```python
  import tensorflow as tf

  model = tf.keras.Sequential([
      tf.keras.layers.Dense(10, activation="relu"),
      tf.keras.layers.Dense(1)
  ])

  model.compile(optimizer="adam", loss="mse")
  model.summary()
  ```

- **PyTorch Example**:
  ```python
  import torch
  import torch.nn as nn

  class NeuralNet(nn.Module):
      def __init__(self):
          super(NeuralNet, self).__init__()
          self.fc = nn.Linear(10, 1)

      def forward(self, x):
          return self.fc(x)

  model = NeuralNet()
  print(model)
  ```

### **Practice Labs**
1. **Digit Classification**:
   - Train a neural network on the MNIST dataset to classify handwritten digits.

2. **Image Classification**:
   - Build a CNN to classify images from the CIFAR-10 dataset.

---

## **Phase 4: Generative AI Concepts**

### **Topics**
#### 1. Generative Models
- **Key Concepts**:
  - Generative models aim to learn the underlying distribution of data to generate new samples.
  - Examples: Autoencoders, GANs, diffusion models.

- **Autoencoders**:
  ```python
  from tensorflow.keras.models import Model
  from tensorflow.keras.layers import Input, Dense

  input_img = Input(shape=(784,))
  encoded = Dense(64, activation="relu")(input_img)
  decoded = Dense(784, activation="sigmoid")(encoded)

  autoencoder = Model(input_img, decoded)
  autoencoder.compile(optimizer="adam", loss="binary_crossentropy")
  ```

#### 2. GANs
- **Key Concepts**:
  - GANs consist of two networks:
    - **Generator**: Creates fake data.
    - **Discriminator**: Distinguishes real data from fake.
  - Training is an adversarial process.

- **Simple GAN Example**:
  ```python
  import tensorflow as tf

  generator = tf.keras.Sequential([
      tf.keras.layers.Dense(128, activation="relu"),
      tf.keras.layers.Dense(784, activation="sigmoid")
  ])

  discriminator = tf.keras.Sequential([
      tf.keras.layers.Dense(128, activation="relu"),
      tf.keras.layers.Dense(1, activation="sigmoid")
  ])
  ```

#### 3. Diffusion Models
- **Key Concepts**:
  - Diffusion models generate data by reversing a gradual noise-adding process.
  - Applications include text-to-image generation (e.g., DALL·E 2).

- **Workflow**:
  - Add Gaussian noise to data in steps.
  - Learn to reverse the noise process to generate samples.

#### 4. Transformers for Generative Tasks
- **Key Concepts**:
  - Transformers leverage the attention mechanism to handle sequences.
  - Widely used in text (GPT, BERT) and image generation (Vision Transformers).

- **Attention Example**:
  ```python
  import tensorflow as tf
  from tensorflow.keras.layers import Attention

  query = tf.random.normal((1, 8, 16))
  value = tf.random.normal((1, 8, 16))
  attention_layer = Attention()
  output = attention_layer([query, value])
  print(output)
  ```

### **Practice Labs**
1. **Digit Generation**:
   - Build a GAN to generate handwritten digits.

2. **Text-to-Image Generation**:
   - Use a pre-trained model like Stable Diffusion to generate images from text prompts.

---

This document now contains expanded theoretical explanations and advanced examples for each phase. Let me know if further depth is required in any specific area!

