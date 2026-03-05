import csv
import math

# Read dataset
X = []
y = []

with open('LR.csv') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    
    for row in reader:
        X.append(float(row[0]))
        y.append(int(row[1]))

# Initialize parameters
w = 0
b = 0
learning_rate = 0.01
epochs = 1000


# Sigmoid function
def sigmoid(z):
    return 1/(1+math.exp(-z))


# Training
for _ in range(epochs):

    dw = 0
    db = 0

    for i in range(len(X)):

        z = w*X[i] + b
        y_pred = sigmoid(z)

        dw += (y_pred - y[i]) * X[i]
        db += (y_pred - y[i])

    dw /= len(X)
    db /= len(X)

    w -= learning_rate * dw
    b -= learning_rate * db


# Prediction function
def predict(x):

    z = w*x + b
    p = sigmoid(z)

    if p >= 0.5:
        return 1
    else:
        return 0


# Test sample
test_hours = 3

result = predict(test_hours)

print("Study Hours:", test_hours)
print("Prediction (0=Fail,1=Pass):", result)
