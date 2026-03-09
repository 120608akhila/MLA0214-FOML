import csv
import math
from collections import Counter

data = []

# Read dataset
with open('Credit.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        income = float(row[0])
        debt = float(row[1])
        label = row[2]
        data.append([income, debt, label])


# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


# KNN classifier
def knn(data, test, k):

    distances = []

    for row in data:
        d = distance(row, test)
        distances.append((d, row[2]))

    distances.sort()

    neighbors = distances[:k]

    classes = [n[1] for n in neighbors]

    return Counter(classes).most_common(1)[0][0]


# Test data
test_customer = [42, 9]

result = knn(data, test_customer, 3)

print("Test Customer:", test_customer)
print("Predicted Credit Score:", result)
