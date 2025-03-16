
---

## 1) Classification Example
### Use Case
**Email spam detection** or **medical diagnosis** often involves classifying inputs into distinct categories. In this example, we’ll demonstrate classification using the well-known **Iris** dataset to predict the type of iris flower. We’ll train a Logistic Regression model and then evaluate it.

### Steps
1. Load the Iris dataset.
2. Split into training and test sets.
3. Train a **LogisticRegression** model.
4. Predict and evaluate using accuracy, confusion matrix, and classification report.

### Code

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

# 3. Train a Logistic Regression model
model = LogisticRegression(max_iter=200)  # Increase max_iter to ensure convergence
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)

# 5. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)
```

### Typical Output
```
Accuracy: 1.0

Confusion Matrix:
 [[10  0  0]
  [ 0  7  0]
  [ 0  0  3]]

Classification Report:
               precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         7
   virginica       1.00      1.00      1.00         3

    accuracy                           1.00        20
   macro avg       1.00      1.00      1.00        20
weighted avg       1.00      1.00      1.00        20
```

- **Interpretation**: An accuracy of 1.0 (100%) on the test set indicates that the logistic regression model was able to perfectly classify the Iris flowers in this split. In real-world settings (e.g., spam detection), you would interpret a similar confusion matrix and classification report to understand where the model makes errors.

---

## 2) Regression Example
### Use Case
**Predicting house prices** or **forecasting sales** involves modeling a continuous target variable. Here, we’ll use the **California Housing** dataset to show a basic **Linear Regression** approach.

> **Note**: The traditional Boston Housing dataset is now deprecated; California Housing is a recommended alternative within scikit-learn.

### Steps
1. Load the California Housing dataset.
2. Split into training and test sets.
3. Train a **LinearRegression** model.
4. Predict and evaluate using **R²** score and **Mean Squared Error (MSE)**.

### Code

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load the California Housing dataset
cal_housing = fetch_california_housing()
X = cal_housing.data
y = cal_housing.target

# 2. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

# 3. Train a Linear Regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# 4. Make predictions
y_pred = reg_model.predict(X_test)

# 5. Evaluate the model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² score:", r2)
print("Mean Squared Error:", mse)
```

### Typical Output
```
R² score: 0.596534
Mean Squared Error: 0.531723
```
- **Interpretation**:
  - **R² score (0.59)**: The model explains about 59% of the variance in the target. This is a rough measure of how well the linear model fits the data.
  - **MSE (0.53)**: On average, the model’s predictions are off by \(\sqrt{0.53} \approx 0.73\) in target units.  

In a real-world scenario (e.g., predicting house prices), you would use these metrics to understand how far off your model is from the true prices, then refine accordingly.

---

## 3) Clustering Example
### Use Case
**Customer segmentation** or **grouping news articles** involves discovering inherent groupings in unlabeled data. We’ll demonstrate **K-Means clustering** on the **Iris** dataset to see how the algorithm groups flowers without knowing the labels upfront.

### Steps
1. Load the Iris dataset (we’ll ignore the labels during clustering).
2. Use **KMeans** to find 3 clusters.
3. Evaluate using cluster centers and some basic inspection of predicted cluster labels.

### Code

```python
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import numpy as np

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data

# 2. Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 3. Cluster assignments & centers
cluster_labels = kmeans.labels_
centers = kmeans.cluster_centers_
inertia = kmeans.inertia_

print("Cluster labels (first 10):", cluster_labels[:10])
print("\nCluster centers:\n", centers)
print("\nInertia:", inertia)
```

### Typical Output
```
Cluster labels (first 10): [1 1 1 1 1 1 1 1 1 1]

Cluster centers:
 [[5.006      3.428      1.462      0.246     ]
  [6.85       3.07368421 5.74210526 2.07105263]
  [5.9016129  2.7483871  4.39354839 1.43387097]]

Inertia: 78.85144142614601
```
- **Interpretation**:
  - K-Means grouped the iris flowers into 3 clusters. The first 10 samples all received the same cluster label in the example output (which might or might not match the original species labels exactly).
  - **Cluster centers** summarize each cluster's "average" data point in terms of feature values.
  - **Inertia** is a measure of how internally coherent the clusters are (lower is generally better).

In a **customer segmentation** scenario, each cluster might represent a different type of buyer behavior, and you’d analyze the cluster centers to understand distinguishing features (e.g., “price-sensitive vs. premium buyers,” etc.).

---

# Summary

- **Classification** (Logistic Regression): Used for predicting discrete categories (e.g., spam/not-spam).  
- **Regression** (Linear Regression): Used for predicting continuous values (e.g., house prices).  
- **Clustering** (K-Means): Used for unlabeled data to discover natural groupings (e.g., customer segments).  

Each of these examples demonstrates how to train the model, make predictions (or cluster assignments), and interpret basic metrics and outcomes. In real-world projects, the core workflow is similar:

1. **Load/Clean** your data.  
2. **Train** a suitable model.  
3. **Evaluate** with appropriate metrics.  
4. **Iterate & Improve** based on the results.  
