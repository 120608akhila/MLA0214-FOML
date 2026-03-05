import csv

# Read dataset
X = []
Y = []

with open('Linear.csv') as file:
    reader = csv.reader(file)
    next(reader)   # skip header
    
    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

n = len(X)

# Calculate mean
mean_x = sum(X)/n
mean_y = sum(Y)/n

# Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x)**2

m = num / den

# Calculate intercept (b)
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)


# Prediction
test_hours = 6

predicted_score = m * test_hours + b

print("Study Hours:", test_hours)
print("Predicted Score:", predicted_score)
