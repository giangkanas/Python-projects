import random 
import time
from sys import maxsize 

def makeArr(num,maxn):
    return [random.randint(-maxn,maxn) for _ in range (num)]

random.seed(1053577)
A=makeArr(500,100)
B=makeArr(1000,100)

def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    return max_so_far,start,end



t0 = time.process_time()
pinakas1 = maxSubArraySum(A,len(A))
t1= time.process_time()

pinakas2 = maxSubArraySum(B,len(B))
t2= time.process_time()

print("data1 : ",pinakas1,t1-t0)
print("data2 : ",pinakas2,t2-t1)
 

