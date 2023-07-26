import matplotlib.pyplot as plt
import numpy as np

# Import the data from the CSV file
data = np.loadtxt("data_science_students.csv", skiprows=1, delimiter=",")

# Get the midsemScore data
midsemScore = data[:, 1]

# Create a bar chart of the midsemScore data
plt.bar(range(len(midsemScore)), midsemScore)

# Add a title to the bar chart
plt.title("Midsem Score")

# Add labels to the x-axis
plt.xlabel("Student")
plt.ylabel("Midsem Score")

# Show the bar chart
plt.show()