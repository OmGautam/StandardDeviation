import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    dataSet = list(reader)
data = dataSet[0] 

def mean(data):
    n = len(data)
    sum = 0
    for i in data:
        sum += int(i)
    average = sum/n
    return(average)

# squaring and difference values
squaredList = []
for num in data:
    diff = int(num) - mean(data)
    diff = diff**2
    squaredList.append(diff)

# calculating sum of defference and square values
add = 0
for value in squaredList:
    add += value

# dividing the added values by total number of values (n-1)
# len(data) = n
result = add/(len(data) - 1)

# calculating square root using predefined function "sqrt" in math module
standardDeviation = math.sqrt(result)

print(standardDeviation)






