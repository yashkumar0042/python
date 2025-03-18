Here is a **complete example** of using **Linear Regression** to predict **house prices** using `scikit-learn`.

---

## **🏠 House Price Prediction using Linear Regression**
### **🔹 Steps Covered:**
1. Load & visualize the dataset  
2. Preprocess the data (handle missing values, feature scaling, etc.)  
3. Split data into training and test sets  
4. Train a **Linear Regression model**  
5. Make predictions on test data  
6. Evaluate the model using **R² score and Mean Absolute Error (MAE)**  

---

### **📌 1. Install Required Libraries**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

---

### **📌 2. Load a Sample Housing Dataset**
For this example, we'll use **Boston Housing Dataset** (available in `sklearn.datasets`).

```python
from sklearn.datasets import fetch_california_housing

# Load California housing dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add target column (House Price)
df['PRICE'] = data.target

# Display dataset information
print(df.head())  # First 5 rows
print(df.describe())  # Summary statistics
```

---

### **📌 3. Explore & Visualize Data**
Before building the model, let's check **correlation** between features.

```python
# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation with House Price")
plt.show()
```

---

### **📌 4. Prepare Data for Training**
#### **🔹 Select Features & Target Variable**
```python
# Select independent variables (features) and dependent variable (price)
X = df[['MedInc', 'AveRooms', 'AveOccup', 'HouseAge']]  # Selecting 4 key features
y = df['PRICE']
```

#### **🔹 Split into Training & Testing Sets**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
```

---

### **📌 5. Train Linear Regression Model**
```python
# Create model instance
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Print model coefficients
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

---

### **📌 6. Make Predictions on Test Data**
```python
# Predict house prices on test data
y_pred = model.predict(X_test)

# Compare first 10 predictions with actual values
comparison = pd.DataFrame({'Actual Price': y_test[:10], 'Predicted Price': y_pred[:10]})
print(comparison)
```

---

### **📌 7. Evaluate Model Performance**
```python
# Calculate model evaluation metrics
mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error
rmse = np.sqrt(mse)  # Root Mean Squared Error
r2 = r2_score(y_test, y_pred)  # R-squared (model accuracy)

# Print evaluation results
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score (R²): {r2:.2f}")
```

---

### **📌 8. Visualize Predictions vs. Actual Prices**
```python
# Scatter plot of actual vs predicted prices
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle="--", color="red")  # Diagonal line
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
```

---

## **📊 Interpretation of Results**
- If **R² score is close to 1**, the model explains most of the variance in house prices.  
- **Lower MAE & RMSE** indicate better accuracy.  
- If performance is poor, **more features, better preprocessing, or a different model (like Random Forest or XGBoost)** may be needed.  
