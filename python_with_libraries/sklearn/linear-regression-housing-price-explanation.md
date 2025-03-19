
---

## 1. Install & Import Required Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

1. **`import numpy as np`**  
   - *Library*: NumPy (alias `np`)  
   - *Purpose*: Provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these arrays efficiently.

2. **`import pandas as pd`**  
   - *Library*: Pandas (alias `pd`)  
   - *Purpose*: Used for data manipulation and analysis; provides DataFrame objects to handle tabular data (rows and columns) easily.

3. **`import matplotlib.pyplot as plt`**  
   - *Library*: Matplotlib’s `pyplot` module (alias `plt`)  
   - *Purpose*: Used for creating static, animated, and interactive data visualizations (e.g., line plots, scatter plots, histograms).

4. **`import seaborn as sns`**  
   - *Library*: Seaborn (alias `sns`)  
   - *Purpose*: Built on top of Matplotlib; used for more refined statistical data visualization such as heatmaps, violin plots, etc.

5. **`from sklearn.model_selection import train_test_split`**  
   - *Function*: `train_test_split`  
   - *Purpose*: Splits arrays or matrices into random train and test subsets, ensuring we can train on one set of data and evaluate on another.

6. **`from sklearn.linear_model import LinearRegression`**  
   - *Class*: `LinearRegression`  
   - *Purpose*: Implements ordinary least squares Linear Regression for predicting a continuous target variable.

7. **`from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score`**  
   - *Functions*:  
     - **`mean_absolute_error` (MAE)**: Measures average magnitude of errors without considering their direction.  
     - **`mean_squared_error` (MSE)**: Measures the average of the squares of errors.  
     - **`r2_score` (R²)**: Indicates how well predictions approximate the real data values (closer to 1 is better).  
   - *Purpose*: Provide ways to evaluate how well the model is performing.

---

## 2. Load a Sample Housing Dataset

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

1. **`from sklearn.datasets import fetch_california_housing`**  
   - *Function*: `fetch_california_housing`  
   - *Purpose*: Loads the California Housing dataset, which contains various features (like median income, house age, etc.) and target values (average house prices).

2. **`data = fetch_california_housing()`**  
   - *Method call*: `fetch_california_housing()`  
   - *Purpose*: Returns a “Bunch” object, which includes data (features) and target (house prices) for California houses.

3. **`df = pd.DataFrame(data.data, columns=data.feature_names)`**  
   - *Creating a DataFrame*: We convert the feature matrix (`data.data`) into a Pandas DataFrame `df`.  
   - *Parameters*:  
     - `data.data`: The actual numeric data (features).  
     - `columns=data.feature_names`: Assigns column names from the dataset’s feature names (e.g., “MedInc”, “HouseAge”, etc.).

4. **`df['PRICE'] = data.target`**  
   - *New column*: Adds the target (house price) as a new column named `PRICE` to the DataFrame.  
   - *Purpose*: Makes it easy to handle features (X) and target (y) in a single DataFrame.

5. **`print(df.head())`**  
   - *Function*: `df.head()`  
   - *Purpose*: Displays the first 5 rows of the DataFrame to preview data structure and initial values.

6. **`print(df.describe())`**  
   - *Function*: `df.describe()`  
   - *Purpose*: Shows summary statistics (mean, standard deviation, min, max, quartiles) for each numeric column, giving an overview of data distribution.

---

## 3. Explore & Visualize Data

```python
# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation with House Price")
plt.show()
```

1. **`plt.figure(figsize=(10, 6))`**  
   - *Function*: `figure()`  
   - *Purpose*: Sets the figure size for the upcoming plot (width=10, height=6 inches).

2. **`sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")`**  
   - *Function*: `sns.heatmap()`  
   - *Parameters*:  
     - `df.corr()`: Computes the correlation matrix of the DataFrame, showing correlation coefficients between features (and with `PRICE`).  
     - `annot=True`: Writes the correlation coefficient inside each cell of the heatmap.  
     - `cmap='coolwarm'`: Color map for the heatmap visualization.  
     - `fmt=".2f"`: Formats the correlation values to 2 decimal places.  
   - *Purpose*: Visualizes how strongly each feature correlates with every other feature (and especially with `PRICE`).

3. **`plt.title("Feature Correlation with House Price")`**  
   - *Function*: `title()`  
   - *Purpose*: Adds a title to the heatmap for clarity.

4. **`plt.show()`**  
   - *Function*: `show()`  
   - *Purpose*: Renders the plot on the screen.

---

## 4. Prepare Data for Training

### Select Features & Target Variable

```python
X = df[['MedInc', 'AveRooms', 'AveOccup', 'HouseAge']]  # Selecting 4 key features
y = df['PRICE']
```

1. **`X = df[['MedInc', 'AveRooms', 'AveOccup', 'HouseAge']]`**  
   - *Variables*: `X` represents the features (independent variables).  
   - *Purpose*: Selecting a subset of columns (here, four columns) from the DataFrame as input features for the model.

2. **`y = df['PRICE']`**  
   - *Variable*: `y` represents the target (dependent variable).  
   - *Purpose*: We separate the house price column as the value the model should predict.

### Split into Training & Testing Sets

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
```

1. **`train_test_split(X, y, test_size=0.2, random_state=42)`**  
   - *Function*: `train_test_split`  
   - *Parameters*:  
     - `X`: Feature dataset.  
     - `y`: Target dataset.  
     - `test_size=0.2`: 20% of the data will be allocated as the test set, 80% as the training set.  
     - `random_state=42`: Ensures reproducibility of the split.  
   - *Purpose*: Randomly splits the features and targets into training and testing subsets.

2. **`X_train, X_test, y_train, y_test`**  
   - *Variables*:  
     - `X_train`, `y_train`: Training features and target.  
     - `X_test`, `y_test`: Testing features and target.  
   - *Purpose*: Keep the training data separate to train the model and testing data separate to evaluate performance afterward.

3. **`print("Training Data Shape:", X_train.shape)`**  
   - *Function*: `print()`  
   - *Purpose*: Shows the dimensions (rows, columns) of the training feature set. Useful to confirm the split size.

4. **`print("Testing Data Shape:", X_test.shape)`**  
   - *Function*: `print()`  
   - *Purpose*: Shows the dimensions of the test feature set.

---

## 5. Train Linear Regression Model

```python
# Create model instance
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Print model coefficients
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

1. **`model = LinearRegression()`**  
   - *Class instantiation*: Creates an instance of `LinearRegression`.  
   - *Purpose*: Initializes the linear regression model object.

2. **`model.fit(X_train, y_train)`**  
   - *Method*: `fit()`  
   - *Purpose*: Trains (fits) the linear regression model by finding the best-fit line to the training data (X_train and y_train).

3. **`print("Model Coefficients:", model.coef_)`**  
   - *Attribute*: `model.coef_`  
   - *Purpose*: Shows the learned coefficients (weights) for each feature in the regression model.

4. **`print("Intercept:", model.intercept_)`**  
   - *Attribute*: `model.intercept_`  
   - *Purpose*: Displays the constant term (the bias) in the linear regression equation.

---

## 6. Make Predictions on Test Data

```python
y_pred = model.predict(X_test)

# Compare first 10 predictions with actual values
comparison = pd.DataFrame({'Actual Price': y_test[:10], 'Predicted Price': y_pred[:10]})
print(comparison)
```

1. **`y_pred = model.predict(X_test)`**  
   - *Method*: `predict()`  
   - *Purpose*: Uses the trained model to predict house prices for the unseen test features (`X_test`).

2. **`comparison = pd.DataFrame({'Actual Price': y_test[:10], 'Predicted Price': y_pred[:10]})`**  
   - *DataFrame creation*: Compares the first 10 actual price values with the first 10 predicted price values.  
   - *Purpose*: Quick sanity check on how the model’s predictions align with real data.

3. **`print(comparison)`**  
   - *Function*: `print()`  
   - *Purpose*: Outputs the comparison table to the console.

---

## 7. Evaluate Model Performance

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score (R²): {r2:.2f}")
```

1. **`mae = mean_absolute_error(y_test, y_pred)`**  
   - *Function*: `mean_absolute_error`  
   - *Purpose*: Calculates the average absolute difference between predicted and actual values. Lower MAE is better.

2. **`mse = mean_squared_error(y_test, y_pred)`**  
   - *Function*: `mean_squared_error`  
   - *Purpose*: Calculates the average squared difference between predicted and actual values. Lower MSE is better.

3. **`rmse = np.sqrt(mse)`**  
   - *Computation*: Takes the square root of the MSE.  
   - *Purpose*: RMSE (root mean squared error) is often more interpretable because it’s in the same units as the target variable (price).

4. **`r2 = r2_score(y_test, y_pred)`**  
   - *Function*: `r2_score`  
   - *Purpose*: Measures how well future samples are likely to be predicted by the model. It ranges from -∞ to 1 (1 is perfect prediction).

5. **`print(f"Mean Absolute Error (MAE): {mae:.2f}")`**  
   - *Formatting*: `{mae:.2f}` displays the MAE with two decimal places.  
   - *Purpose*: Gives a user-friendly output of each metric.

6. **`print(f"Mean Squared Error (MSE): {mse:.2f}")`**, **`print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")`**, **`print(f"R-squared Score (R²): {r2:.2f}")`**  
   - *Purpose*: Similarly prints MSE, RMSE, and R² in a readable format.

---

## 8. Visualize Predictions vs. Actual Prices

```python
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle="--", color="red")  # Diagonal line
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
```

1. **`plt.figure(figsize=(8, 6))`**  
   - *Function*: `figure()`  
   - *Purpose*: Creates a new figure with specified width and height.

2. **`plt.scatter(y_test, y_pred, color='blue', alpha=0.5)`**  
   - *Function*: `scatter()`  
   - *Parameters*:  
     - `y_test`: Actual prices on the x-axis.  
     - `y_pred`: Predicted prices on the y-axis.  
     - `color='blue'`: Sets the scatter points color.  
     - `alpha=0.5`: Sets transparency so overlapping points are more visible.  
   - *Purpose*: Shows how closely predicted values line up with actual values.

3. **`plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle="--", color="red")`**  
   - *Function*: `plot()`  
   - *Purpose*: Draws a diagonal reference line (ideal prediction line) from the lowest actual price to the highest actual price. Points closer to this line indicate better predictions.

4. **`plt.xlabel("Actual House Price")`, `plt.ylabel("Predicted House Price")`, `plt.title("Actual vs Predicted House Prices")`**  
   - *Functions*: `xlabel()`, `ylabel()`, `title()`  
   - *Purpose*: Label the axes and add a title for clearer interpretation.

5. **`plt.show()`**  
   - *Function*: `show()`  
   - *Purpose*: Displays the plot.

---

## Interpretation of Results

- **R² Score** (close to 1 means the model explains a large portion of the variance in the target variable).  
- **MAE** & **RMSE** (lower values mean predictions are, on average, closer to the actual data).  
- If the metrics are unsatisfactory, consider:  
  - Using more/different features,  
  - Better preprocessing (handling outliers, scaling, feature engineering),  
  - Trying more sophisticated models (e.g., Random Forest, XGBoost).

---
