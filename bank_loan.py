import csv
import math
from collections import defaultdict

data=[]

with open('bank_loan.csv') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        income=float(row[0])
        age=float(row[1])
        label=row[2]

        data.append([income,age,label])

classes=defaultdict(list)

for row in data:
    classes[row[2]].append(row[:2])

def mean(nums):
    return sum(nums)/len(nums)

def variance(nums):
    m=mean(nums)
    return sum((x-m)**2 for x in nums)/len(nums)

def gaussian(x,m,v):
    return (1/math.sqrt(2*math.pi*v))*math.exp(-(x-m)**2/(2*v))

model={}

for label,rows in classes.items():
    model[label]=[]

    for i in range(2):
        col=[r[i] for r in rows]
        model[label].append((mean(col),variance(col)))

def predict(sample):

    probs={}

    for label,stats in model.items():

        probs[label]=1

        for i in range(2):
            m,v=stats[i]
            probs[label]*=gaussian(sample[i],m,v)

    return max(probs,key=probs.get)

test=[32000,33]

print("Prediction:",predict(test))
