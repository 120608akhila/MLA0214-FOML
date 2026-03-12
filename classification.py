import csv
import math
from collections import Counter

data=[]

# Read dataset
with open('classification.csv') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        age=float(row[0])
        salary=float(row[1])
        label=row[2]

        data.append([age,salary,label])


# Split features and labels
X=[row[:2] for row in data]
y=[row[2] for row in data]


# -----------------
# KNN Classifier
# -----------------

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def knn_predict(train,test,k):

    distances=[]

    for row in train:
        d=distance(row,test)
        distances.append((d,row[2]))

    distances.sort()

    neighbors=distances[:k]

    labels=[n[1] for n in neighbors]

    return Counter(labels).most_common(1)[0][0]


# -----------------
# Accuracy function
# -----------------

def accuracy(actual,predicted):

    correct=0

    for i in range(len(actual)):
        if actual[i]==predicted[i]:
            correct+=1

    return correct/len(actual)*100


# KNN Predictions
knn_pred=[]

for row in X:
    knn_pred.append(knn_predict(data,row,3))


print("KNN Accuracy:",accuracy(y,knn_pred))
