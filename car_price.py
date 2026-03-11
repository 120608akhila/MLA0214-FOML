import csv

X = []
Y = []

# Read dataset
with open('car_price.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        year = float(row[0])
        km = float(row[1])
        price = float(row[2])

        feature = year - (km/100000)   # simple feature
        X.append(feature)
        Y.append(price)

n = len(X)

# Mean values
mean_x = sum(X)/n
mean_y = sum(Y)/n

# Linear Regression calculation
num = 0
den = 0

for i in range(n):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2

m = num/den
b = mean_y - m*mean_x

print("Regression Equation:")
print("Price =",m,"* X +",b)

# Prediction
test_year = 2022
test_km = 7000

test_feature = test_year - (test_km/100000)

predicted_price = m*test_feature + b

print("Predicted Car Price:",predicted_price)
