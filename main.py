
import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

products = ["Laptop", "Mobile", "Tablet", "Watch"]
revenue = [500, 800, 300, 200]

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 80]

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Line chart
axes[0, 0].plot(months, sales, marker="o", color="blue")
axes[0, 0].set_title("Monthly Sales")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")

# 2. Bar chart
axes[0, 1].bar(products, revenue, color="green")
axes[0, 1].set_title("Product Revenue")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Revenue")

# 3. Pie chart
axes[1, 0].pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)
axes[1, 0].set_title("Student Marks Distribution")

# 4. Scatter chart
axes[1, 1].scatter(x, y, color="red")
axes[1, 1].set_title("Scatter Plot")
axes[1, 1].set_xlabel("X Values")
axes[1, 1].set_ylabel("Y Values")

plt.tight_layout()
plt.savefig("four_charts.png")
plt.show()
