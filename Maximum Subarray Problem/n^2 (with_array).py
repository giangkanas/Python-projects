import random 
import time


def makeArr(num,maxn):
    return [random.randint(-maxn,maxn) for _ in range (num)]

random.seed(1053577)
A=makeArr(500,100)
B=makeArr(1000,100)


def max_sabarr_brute(input_array):
    global_max=0
    B = []
    for x in range (len(input_array)+1):
        for j in range (len(input_array)+1):
            
            if input_array[x:j]:
                current_max = sum(input_array[x:j])
                if current_max > global_max:
                    global_max = current_max
                    B.append((x,j-1))
    return global_max, B.pop()

t0 = time.process_time()
pinakas1 = max_sabarr_brute(A)
t1= time.process_time()
pinakas2 = max_sabarr_brute(B)
t2= time.process_time()

print("data1 : ",pinakas1,t1-t0)
print("data2 : ",pinakas2,t2-t1)
 
