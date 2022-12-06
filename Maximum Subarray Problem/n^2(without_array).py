import random 
import time


def makeArr(num,maxn):
    return [random.randint(-maxn,maxn) for _ in range (num)]

random.seed(1053577)
A=makeArr(500,100)
B=makeArr(1000,100)


def algo2(input_array):
    
    maxsum=0
    beginindex=1
    endindex=1
    for i in range(len(input_array)):
        tempsum=0
        for j in range(i,len(input_array)):
            tempsum = tempsum + input_array[j]
            if (tempsum > maxsum):
                maxsum=tempsum
                beginindex=i
                endindex=j
    return maxsum , beginindex , endindex

t0 = time.process_time()
pinakas1 = algo2(A)
t1= time.process_time()
pinakas2 = algo2(B)
t2= time.process_time()

print("data1 : ",pinakas1,t1-t0)
print("data2 : ",pinakas2,t2-t1)
"""

a = [3, -1, -1, 10, -3, -2, 4]
print(algo2(a))

"""
