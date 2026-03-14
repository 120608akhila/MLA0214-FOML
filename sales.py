import csv

X=[]
Y=[]

with open('sales.csv') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

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

print("Sales Model: Sales =",m,"* Month +",b)

# Future prediction
future_month=10

predicted_sales=m*future_month+b

print("Predicted Sales for Month",future_month,":",predicted_sales)
