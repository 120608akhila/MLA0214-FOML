import csv
import math
from collections import defaultdict

# Read dataset
data = []
with open('iris_nb.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        features = list(map(float,row[:4]))
        label = row[4]
        data.append(features + [label])

# Separate by class
separated = defaultdict(list)

for row in data:
    separated[row[4]].append(row[:4])

# Mean
def mean(numbers):
    return sum(numbers)/len(numbers)

# Variance
def variance(numbers):
    avg = mean(numbers)
    return sum((x-avg)**2 for x in numbers)/len(numbers)

# Gaussian probability
def gaussian(x, mean, var):
    return (1/math.sqrt(2*math.pi*var)) * math.exp(-(x-mean)**2/(2*var))

# Train model
model = {}

for label,rows in separated.items():
    model[label] = []
    
    for i in range(4):
        column = [row[i] for row in rows]
        model[label].append((mean(column),variance(column)))

# Prediction
def predict(sample):
    
    probabilities = {}
    
    for label,stats in model.items():
        
        probabilities[label] = 1
        
        for i in range(4):
            m,v = stats[i]
            probabilities[label] *= gaussian(sample[i],m,v)
    
    return max(probabilities,key=probabilities.get)

# Test sample
test_flower = [5.0,3.4,1.5,0.2]

prediction = predict(test_flower)

print("Test Flower:",test_flower)
print("Predicted Class:",prediction)
