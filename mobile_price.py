import csv

X=[]
Y=[]

# Read dataset
with open('mobile_price.csv') as file:

    reader=csv.reader(file)
    next(reader)

    for row in reader:

        ram=float(row[0])
        storage=float(row[1])
        price=float(row[2])

        feature=ram*1000 + storage

        X.append(feature)
        Y.append(price)


n=len(X)

mean_x=sum(X)/n
mean_y=sum(Y)/n

num=0
den=0

for i in range(n):
    num+=(X[i]-mean_x)*(Y[i]-mean_y)
    den+=(X[i]-mean_x)**2

m=num/den
b=mean_y-m*mean_x

print("Price Model:")
print("Price =",m,"* X +",b)


# Prediction
test_ram=8
test_storage=128

test_feature=test_ram*1000 + test_storage

predicted_price=m*test_feature+b

print("Predicted Mobile Price:",predicted_price)
