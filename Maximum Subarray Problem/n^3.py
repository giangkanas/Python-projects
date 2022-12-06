import random 
import time


def makeArr(num,maxn):
    return [random.randint(-maxn,maxn) for _ in range (num)]

random.seed(1053577)
A=makeArr(500,100)
B=makeArr(1000,100)

def algo1(input_array):
    maxsum=0
    beginindex=1
    endindex=1
    for i in range (len(input_array)):
        for j in range (len(input_array)):
            tempsum=0
            for k in range(i,j):
                tempsum=tempsum+input_array[k]
                if (tempsum>maxsum):
                    maxsum=tempsum
                    beginindex=i
                    endindex=j-1
    return (maxsum,(beginindex,endindex))

t0 = time.process_time()
pinakas1 = algo1(A)
t1= time.process_time()
pinakas2 = algo1(B)
t2= time.process_time()

print("data1 : ",pinakas1,t1-t0)
print("data2 : ",pinakas2,t2-t1)
"""

a = [3, -1, -1, 10, -3, -2, 4]
print(algo1(a))
"""
