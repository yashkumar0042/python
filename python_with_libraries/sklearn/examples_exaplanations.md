
1. **Code**  
2. **Detailed breakdown of each line** and its purpose  

Feel free to skip to the example that most interests you!

---

## 1) Classification Example

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
model = LogisticRegression(max_iter=200)
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

### Line-by-Line Explanation

1. **`import numpy as np`**
   - Imports **NumPy**, a fundamental Python library for numerical computations, often used for handling arrays and matrices.

2. **`from sklearn.datasets import load_iris`**
   - Imports the **load_iris** function, which provides the classic Iris flower dataset (already built into scikit-learn).

3. **`from sklearn.model_selection import train_test_split`**
   - Imports the **train_test_split** function, which splits your dataset into training and testing sets.

4. **`from sklearn.linear_model import LogisticRegression`**
   - Imports **LogisticRegression**, a classification algorithm used for predicting discrete classes (e.g., setosa, versicolor, virginica in the Iris dataset).

5. **`from sklearn.metrics import accuracy_score, confusion_matrix, classification_report`**
   - Imports **accuracy_score**, **confusion_matrix**, and **classification_report**, which are metrics for evaluating classification models.

---

6. **`iris = load_iris()`**
   - Loads the entire Iris dataset, which includes data (features) and target (labels) in a **Bunch** object (similar to a dictionary).

7. **`X = iris.data`**
   - Extracts the numeric features (e.g., petal length, petal width, sepal length, sepal width).  
   - `X` will be a 2D NumPy array of shape `[number_of_samples, number_of_features]`.

8. **`y = iris.target`**
   - Extracts the target array (the species of the flower, encoded as 0, 1, 2).

---

9. **`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`**
   - Splits `X` and `y` into training and test sets.  
   - **`test_size=0.2`** means 20% of the data goes to the test set, and 80% goes to the training set.  
   - **`random_state=42`** is a seed for reproducibility: you’ll get the same split each time you run the code.

---

10. **`model = LogisticRegression(max_iter=200)`**
    - Creates an instance of **LogisticRegression**.  
    - **`max_iter=200`** sets the maximum number of iterations for the optimization algorithm (to ensure it converges properly).

11. **`model.fit(X_train, y_train)`**
    - Trains (fits) the logistic regression model using the training data `(X_train, y_train)`.

---

12. **`y_pred = model.predict(X_test)`**
    - Uses the trained model to predict the labels (flower species) on the **test data**.

---

13. **`accuracy = accuracy_score(y_test, y_pred)`**
    - Calculates the **accuracy** of the predictions, which is `(number of correct predictions) / (total predictions)`.

14. **`cm = confusion_matrix(y_test, y_pred)`**
    - Computes the **confusion matrix** to see how often each class was correctly classified versus misclassified.

15. **`report = classification_report(y_test, y_pred, target_names=iris.target_names)`**
    - Creates a **classification report** showing precision, recall, and F1-score for each of the Iris classes.

16. **`print("Accuracy:", accuracy)`**
    - Prints the accuracy.

17. **`print("\nConfusion Matrix:\n", cm)`**
    - Prints the confusion matrix.

18. **`print("\nClassification Report:\n", report)`**
    - Prints the detailed classification metrics.

---

## 2) Regression Example

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

### Line-by-Line Explanation

1. **`import numpy as np`**
   - Again, imports **NumPy** for numerical operations.

2. **`from sklearn.datasets import fetch_california_housing`**
   - Imports the function to load the **California Housing** dataset (housing data from California).

3. **`from sklearn.model_selection import train_test_split`**
   - Same as before, for splitting data into training and test sets.

4. **`from sklearn.linear_model import LinearRegression`**
   - Imports the **LinearRegression** algorithm for predicting continuous values.

5. **`from sklearn.metrics import r2_score, mean_squared_error`**
   - Metrics for evaluating regression: **R²** and **MSE**.

---

6. **`cal_housing = fetch_california_housing()`**
   - Loads the California Housing dataset, returning a Bunch object with `.data` and `.target`.

7. **`X = cal_housing.data`**
   - Extracts the features (e.g., average income, house age, etc.).

8. **`y = cal_housing.target`**
   - Extracts the continuous target variable (median house value in that region).

---

9. **`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`**
   - Splits the dataset into training and test subsets (80% train, 20% test).

---

10. **`reg_model = LinearRegression()`**
    - Creates a Linear Regression model.

11. **`reg_model.fit(X_train, y_train)`**
    - Fits (trains) the model on the training data.

---

12. **`y_pred = reg_model.predict(X_test)`**
    - Uses the trained model to predict house values for the test features.

---

13. **`r2 = r2_score(y_test, y_pred)`**
    - Calculates the **coefficient of determination** (R²). This indicates how much of the variance in the target is explained by the model (1.0 = perfect fit, 0 = no better than just guessing the mean).

14. **`mse = mean_squared_error(y_test, y_pred)`**
    - Computes the **mean squared error**, which is the average of `(true_value - predicted_value)²` across all samples.

15. **`print("R² score:", r2)`**
    - Prints the R² score.

16. **`print("Mean Squared Error:", mse)`**
    - Prints the mean squared error.

---

## 3) Clustering Example

### Code
```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

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

### Line-by-Line Explanation

1. **`import numpy as np`**
   - Imports **NumPy** (as before).

2. **`from sklearn.cluster import KMeans`**
   - Imports the **KMeans** clustering algorithm, which finds groups (clusters) in unlabeled data.

3. **`from sklearn.datasets import load_iris`**
   - Loads the Iris dataset again (though we’ll ignore the true labels for clustering).

---

4. **`iris = load_iris()`**
   - Loads the Iris dataset.

5. **`X = iris.data`**
   - Extracts the feature matrix (4 measurements per iris).

---

6. **`kmeans = KMeans(n_clusters=3, random_state=42)`**
   - Initializes the K-Means clustering with **3 clusters** (we happen to know Iris data has 3 species).  
   - `random_state=42` ensures reproducibility of the cluster initialization.

7. **`kmeans.fit(X)`**
   - Runs the K-Means algorithm on the entire dataset `X`.  
   - K-Means tries to group the data into 3 clusters, assigning each point to the cluster whose center is closest in terms of distance.

---

8. **`cluster_labels = kmeans.labels_`**
   - Accesses the array of cluster labels for each data point (values like 0, 1, or 2).

9. **`centers = kmeans.cluster_centers_`**
   - Shows the **centroid** of each cluster in the 4-dimensional feature space.

10. **`inertia = kmeans.inertia_`**
    - The final value of the **within-cluster sum of squares** (lower generally indicates more cohesive clusters, but also depends on the number of clusters).

11. **`print("Cluster labels (first 10):", cluster_labels[:10])`**
    - Prints out the first 10 assigned cluster labels for reference.

12. **`print("\nCluster centers:\n", centers)`**
    - Prints the coordinates of the 3 cluster centers.

13. **`print("\nInertia:", inertia)`**
    - Prints the K-Means inertia.

---

## Summary

- **Classification (LogisticRegression)**:  
  - Used for predicting categorical outcomes (e.g., type of flower).  
  - Key steps: train_test_split → model.fit → model.predict → evaluate with accuracy, confusion matrix, classification report.

- **Regression (LinearRegression)**:  
  - Used for continuous numeric predictions (e.g., house prices).  
  - Key steps: load data → train_test_split → model.fit → model.predict → evaluate with R², MSE.

- **Clustering (KMeans)**:  
  - Used for finding groups in unlabeled data (e.g., customer segments).  
  - Key steps: load data → kmeans.fit → examine cluster labels, centers, and inertia.
