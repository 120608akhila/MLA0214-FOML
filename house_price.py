import csv

X = []
Y = []

# Read dataset
with open('house_price.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

n = len(X)

# Mean values
mean_x = sum(X)/n
mean_y = sum(Y)/n

# Calculate slope
num = 0
den = 0

for i in range(n):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2

m = num/den

# Intercept
b = mean_y - m*mean_x

print("House Price Model")
print("Price =",m,"* Size +",b)

# Prediction
test_size = 1500

predicted_price = m*test_size + b

print("House Size:",test_size)
print("Predicted Price:",predicted_price)
