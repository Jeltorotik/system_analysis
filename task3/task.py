import csv
import math

def task(var):
    l = list(csv.reader(var.split("\n")))
    n, k = len(l), len(l[0])

    H = 0
    for j in range(n):
        for i in range(k):
            if int(l[j][i]) == 0:
                continue
            H += (int(l[j][i])/(n-1)) * math.log2(int(l[j][i]) / (n-1))
    H *= -1
    return H



# print(task("2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1"))