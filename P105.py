import math
import csv

with open("Projects\P105\data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    
numbers = len(data)

total = 0

for item in data:
    total = total + float(item[1])

mean = total/numbers

marks = []
for item in data: 
    mark = int(item[1])
    marks.append(mark)

squared_list = []
for number in marks:
    a = number - mean
    a= a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum / numbers

standard_deviation = math.sqrt(result)
print("the standard deviation for data is: ", standard_deviation)
