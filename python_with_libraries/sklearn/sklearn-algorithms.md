
---

# **1. Supervised Learning (Labeled Data)**

Supervised learning involves training models using input-output pairs. The model learns from the labeled data to predict the output for new inputs.

---

## **1.1. Regression Algorithms (Predicting Continuous Values)**

### **1.1.1. Linear Regression**
Linear regression is used to model the relationship between a dependent variable (\( Y \)) and an independent variable (\( X \)).

#### **Mathematical Formula**
\[
Y = \beta_0 + \beta_1X + \epsilon
\]
where:
- \( Y \) = Target variable (dependent)
- \( X \) = Feature variable (independent)
- \( \beta_0 \) = Intercept (constant)
- \( \beta_1 \) = Coefficient (slope)
- \( \epsilon \) = Error term (residual)

#### **Example Code**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generating dataset
X = np.array([[1], [2], [3], [4], [5]])  # Independent variable
y = np.array([2, 4, 6, 8, 10])  # Dependent variable

# Initializing and training the model
model = LinearRegression()
model.fit(X, y)

# Making a prediction
X_test = np.array([[6]])
prediction = model.predict(X_test)

# Output results
print("Coefficient (Slope):", model.coef_[0])  # β1
print("Intercept:", model.intercept_)  # β0
print("Prediction for X=6:", prediction[0])

# Visualizing the data
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.scatter(X_test, prediction, color="green", marker="x", label="Prediction for X=6")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
```

#### **Explanation**
1. **`X = np.array([[1], [2], [3], [4], [5]])`** → Independent variable (reshaped into a 2D array for sklearn).
2. **`y = np.array([2, 4, 6, 8, 10])`** → Dependent variable.
3. **`model = LinearRegression()`** → Creates a linear regression model.
4. **`model.fit(X, y)`** → Trains the model.
5. **`model.predict([[6]])`** → Predicts the output for X=6.
6. **`model.coef_`** → The slope (\(\beta_1\)).
7. **`model.intercept_`** → The intercept (\(\beta_0\)).
8. **Plotting**: Shows a scatter plot of the data and the best-fit regression line.

---
  
### **1.1.2. Ridge and Lasso Regression**
#### **Concept**
- **Ridge Regression (L2 Regularization):** Adds penalty **\( \lambda \sum w^2 \)** to prevent overfitting.
- **Lasso Regression (L1 Regularization):** Adds penalty **\( \lambda \sum |w| \)**, which can shrink some weights to zero (feature selection).

#### **Example Code**
```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X, y)
lasso.fit(X, y)

print("Ridge Coefficients:", ridge.coef_)
print("Lasso Coefficients:", lasso.coef_)
```

#### **Explanation**
- Ridge and Lasso help when features are highly correlated.
- **Alpha** controls regularization strength:
  - Higher **alpha** → More regularization (simpler model).
  - Lower **alpha** → Less regularization.

---

### **1.1.3. Decision Tree Regression**
#### **Concept**
- Decision Trees split data based on **feature values**.
- It creates **if-else** rules to predict continuous values.

#### **Example Code**
```python
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor()
dt.fit(X, y)

print("Decision Tree Prediction for X=6:", dt.predict([[6]]))
```

#### **Explanation**
- Splits data recursively into smaller subsets.
- Unlike Linear Regression, it does **not assume linearity**.

---

## **1.2. Classification Algorithms (Predicting Categories)**

### **1.2.1. Logistic Regression**
#### **Concept**
- Used for **binary classification** (e.g., spam vs. not spam).
- Uses **Sigmoid Function**:
  \[
  P(Y=1 | X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X)}}
  \]
- Outputs a probability between **0 and 1**.

#### **Example Code**
```python
from sklearn.linear_model import LogisticRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 1, 1, 1])  # Binary classification (0 or 1)

model = LogisticRegression()
model.fit(X, y)

print("Probability for X=3.5:", model.predict_proba([[3.5]]))
print("Prediction:", model.predict([[3.5]]))
```

#### **Explanation**
- **`predict_proba`** gives the probability of belonging to each class.
- **`predict`** assigns the class with the highest probability.

---

### **1.2.2. Random Forest Classifier**
#### **Concept**
- Ensemble of multiple decision trees (reduces overfitting).
- Uses **majority voting**.

#### **Example Code**
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("Random Forest Prediction:", model.predict([[3.5]]))
```

#### **Explanation**
- **`n_estimators=100`** → Uses 100 trees.
- Aggregates results of all trees.

---

### **1.2.3. Support Vector Machine (SVM)**
#### **Concept**
- Finds the **optimal hyperplane** to separate classes.
- **Maximizes margin**.

#### **Example Code**
```python
from sklearn.svm import SVC

model = SVC(kernel='linear')
model.fit(X, y)

print("SVM Prediction:", model.predict([[3.5]]))
```

#### **Explanation**
- **Kernel Trick**: Maps data to higher dimensions if it's not linearly separable.

---

## **2. Unsupervised Learning (No Labeled Data)**

### **2.1. k-Means Clustering**
#### **Concept**
- Partitions data into \( k \) clusters.

#### **Example Code**
```python
from sklearn.cluster import KMeans

X = np.array([[1], [2], [3], [10], [11], [12]])
model = KMeans(n_clusters=2)
model.fit(X)

print("Cluster Labels:", model.labels_)
```

#### **Explanation**
- **Chooses \( k \) centroids** and groups points based on distance.
- Updates centroids iteratively.

---

## **Finally **
- **Regression**: Predicts continuous values (Linear, Ridge, Lasso, Decision Tree Regression).
- **Classification**: Predicts categories (Logistic, Random Forest, SVM).
- **Clustering**: Groups data without labels (k-Means).
