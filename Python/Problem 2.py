# -Create a Python script that reads a CSV file containing information about employees (Name, Age, Salary) and generates a new CSV file with the same information sorted by Age in descending order.
import pandas as pd
print("Solution 2")

data = pd.read_csv("assets/employee.csv")
data = pd.DataFrame(data)
print(type(data))
print(data.columns)
sorted = data.sort_values(by="age", ascending=False)

sorted.to_csv("assets/newFile.csv", index=False)

