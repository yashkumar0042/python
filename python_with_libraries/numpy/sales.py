import numpy as np

# Daily sales data for a month (30 days)
sales_data = np.array([230, 255, 190, 210, 310, 275, 290, 300,
                       310, 305, 350, 400, 320, 330, 280, 270,
                       260, 300, 290, 240, 235, 245, 255, 265,
                       275, 285, 295, 305, 315, 325])

mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)
std_sales = np.std(sales_data)

print("Mean sales:", mean_sales)
print("Median sales:", median_sales)
print("Standard deviation of sales:", std_sales)
