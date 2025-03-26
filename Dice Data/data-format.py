import csv
import pandas as pd


nums = list(range(1, 21))
sums = [0] * 20
with open('d20.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d20 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d20.to_csv("d20-Sums.csv", index=False)

nums = list(range(1, 13))
sums = [0] * 12
with open('d12.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d12 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d12.to_csv("d12-Sums.csv", index=False)

nums = list(range(1, 11))
sums = [0] * 10
with open('d10.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d10 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d10.to_csv("d10-Sums.csv", index=False)

nums = list(range(1, 9))
sums = [0] * 8
with open('d8.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d8 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d8.to_csv("d8-Sums.csv", index=False)

nums = list(range(1, 7))
sums = [0] * 6
with open('d6.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d6 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d6.to_csv("d6-Sums.csv", index=False)

nums = list(range(1, 5))
sums = [0] * 4
with open('d4.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        for num in line:
            for i in nums:
                if num == str(i):
                    sums[i-1] += 1

        
d4 = pd.DataFrame({"Value" : nums, "Freq" : sums})

d4.to_csv("d4-Sums.csv", index=False)
