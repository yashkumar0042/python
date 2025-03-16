
---

## 1. Installation and Setup

If you haven’t installed Matplotlib already, you can do so via pip:

```bash
pip install matplotlib
```

Then, in your Python script or Jupyter notebook:

```python
import matplotlib.pyplot as plt
```

That’s all you need to start!

---

## 2. Basic Line Plot

A simple line plot is often the first step in learning Matplotlib.

**Code Example:**

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure()  # Create a new figure
plt.plot(x, y)  # Plot y against x
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

**Output Description:**
- A single figure appears displaying a line that goes through points (1,1), (2,4), (3,9), etc. 
- The x-axis is labeled “X-axis” and the y-axis “Y-axis”.
- The plot has a title “Basic Line Plot”.

---

## 3. Multiple Lines on One Plot

You can easily plot more than one line on the same figure by calling `plt.plot()` multiple times.

**Code Example:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]

plt.figure()
plt.plot(x, y1, label="Linear")
plt.plot(x, y2, label="Quadratic")
plt.title("Multiple Lines on One Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()  # Show the legend
plt.show()
```

**Output Description:**
- One figure with two lines: 
  - The first line (labeled “Linear”) is a straight line from (1,1) to (5,5).
  - The second line (labeled “Quadratic”) curves upward from (1,1) to (5,25).
- A legend differentiates between the two lines.

---

## 4. Scatter Plot

Scatter plots are useful for visualizing the relationship between two sets of data points without connecting them with lines.

**Code Example:**

```python
import matplotlib.pyplot as plt
import random

# Generate random data for demonstration
x = [i for i in range(20)]
y = [random.randint(0, 100) for _ in range(20)]

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

**Output Description:**
- A figure shows a collection of 20 scattered points distributed randomly in the vertical range (0 to 100), horizontally arranged from x=0 to x=19.

---

## 5. Bar Plot

Bar plots help compare discrete categories or groups.

**Code Example:**

```python
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [10, 24, 36, 15]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

**Output Description:**
- A figure shows four bars labeled "A", "B", "C", and "D" on the x-axis.
- Their respective heights are 10, 24, 36, and 15.

---

## 6. Histogram

A histogram shows the distribution of numerical data.

**Code Example:**

```python
import matplotlib.pyplot as plt
import random

# Generate random data for demonstration
data = [random.gauss(50, 10) for _ in range(1000)]  # 1000 points around mean=50, std=10

plt.figure()
plt.hist(data, bins=20)  # 20 bins
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

**Output Description:**
- A figure with bars (bins) showing the distribution of the 1000 random points. 
- The data is centered around 50 with various heights reflecting frequency counts.

---

## 7. Box Plot (Box and Whisker Plot)

A box plot provides a summary of the data distribution—showing median, quartiles, and outliers.

**Code Example:**

```python
import matplotlib.pyplot as plt
import random

# Generate two groups of data for demonstration
group1 = [random.gauss(50, 5) for _ in range(100)]
group2 = [random.gauss(60, 10) for _ in range(100)]
data = [group1, group2]

plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()
```

**Output Description:**
- A figure with two box plots side by side:
  - The first is centered near 50 with a smaller spread (standard deviation ~5).
  - The second is centered near 60 with a larger spread (standard deviation ~10).

---

## 8. Pie Chart

Pie charts help show proportions of categories that make up a whole.

**Code Example:**

```python
import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Cherry", "Date"]
sizes = [30, 25, 25, 20]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
```

**Output Description:**
- A figure with a circular pie chart split into 4 slices labeled “Apple”, “Banana”, “Cherry”, and “Date”.
- Each slice’s size corresponds to 30%, 25%, 25%, and 20% respectively.
- The `autopct` parameter displays the percentage on each slice.

---

## 9. Adding Annotations

Annotations let you add textual descriptions to specific points on the plot.

**Code Example:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.figure()
plt.plot(x, y, marker='o')
plt.title("Plot with Annotations")

# Choose a point to annotate
point_x = x[3]
point_y = y[3]

# Add an annotation pointing to the 4th data point
plt.annotate(
    "Peak Value", 
    xy=(point_x, point_y), 
    xytext=(point_x+0.3, point_y+0.3), 
    arrowprops=dict(arrowstyle="->")
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

**Output Description:**
- A figure with five data points connected by lines.
- A label “Peak Value” with an arrow pointing to the point (4,8).

---

## 10. Logarithmic Scale

You can use logarithmic scales to better visualize data spanning wide ranges.

**Code Example:**

```python
import matplotlib.pyplot as plt

x = [10**i for i in range(5)]   # [1, 10, 100, 1000, 10000]
y = [10**(2*i) for i in range(5)]  # [1, 100, 10000, 1000000, 100000000]

plt.figure()
plt.plot(x, y, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.title("Log-Log Plot")
plt.xlabel("Log-scaled X-axis")
plt.ylabel("Log-scaled Y-axis")
plt.show()
```

**Output Description:**
- A line plot where both x and y axes are on a logarithmic scale.
- The points appear in a straight line relationship since \( y = x^2 \).

---

## 11. Advanced: 3D Plotting

Matplotlib also allows 3D plotting via `mpl_toolkits.mplot3d`.

**Code Example:**

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate a 3D surface (e.g., z = sin(r))
theta = np.linspace(0, 2*np.pi, 30)
r = np.linspace(0, 5, 20)
theta, r = np.meshgrid(theta, r)
X = r * np.cos(theta)
Y = r * np.sin(theta)
Z = np.sin(r)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # Create a 3D axis
ax.plot_surface(X, Y, Z)
ax.set_title("3D Surface Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
```

**Output Description:**
- A new figure opens in 3D with a surface shaped by \(\sin(r)\), where \(r\) is the distance from the origin.
- You can rotate the plot (in interactive environments) to see the surface from different angles.

---

## 12. Saving Figures

Instead of (or in addition to) displaying a figure, you can save it to a file (PNG, PDF, SVG, etc.):

```python
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Saved Figure")
plt.savefig("my_plot.png")  # Save as a PNG file
plt.show()
```

A file named **my_plot.png** will be created in your current working directory.

---

## Conclusion

Matplotlib is a powerful and flexible library for creating a wide variety of plots. Here’s what we covered:

1. **Line Plots** – The most basic form of plotting.
2. **Multiple Lines** – Plot several datasets in one figure.
3. **Scatter Plots** – Great for visualizing the relationship between two data sets.
4. **Bar Plots** – Compare values among discrete categories.
5. **Histograms** – Examine the distribution of numeric data.
6. **Box Plots** – Summarize data distributions with quartiles and outliers.
7. **Pie Charts** – Show proportional segments of a whole.
8. **Annotations** – Add arrows and text to highlight features of interest.
9. **Log Scales** – Useful for wide-range data.
10. **3D Plots** – Visualize surfaces and 3D relationships.
11. **Saving Figures** – Store your plots for sharing or publication.
