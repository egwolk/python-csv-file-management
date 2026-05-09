import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "product", "price"])
    writer.writerow([1, "Laptop", 45000])