import csv

data=[]

with open('iris_perceptron.csv') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        features=list(map(float,row[:4]))
        label=int(row[4])
        data.append((features,label))

# initialize weights
weights=[0,0,0,0]
bias=0
learning_rate=0.1
epochs=10

for _ in range(epochs):

    for x,y in data:

        activation=sum(weights[i]*x[i] for i in range(4))+bias

        prediction=1 if activation>=0 else -1

        if prediction!=y:
            for i in range(4):
                weights[i]+=learning_rate*y*x[i]

            bias+=learning_rate*y

print("Weights:",weights)
print("Bias:",bias)

# Test sample
test=[5.0,3.4,1.5,0.2]

activation=sum(weights[i]*test[i] for i in range(4))+bias
prediction=1 if activation>=0 else -1

print("Prediction:",prediction)
