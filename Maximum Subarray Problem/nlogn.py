import random 
import time


def makeArr(num,maxn):
    return [random.randint(-maxn,maxn) for _ in range (num)]

random.seed(1053577)
A=makeArr(500,100)
B=makeArr(1000,100)


# function to return maximum number among three numbers
def maximum(a, b, c):
  if (a>=b and a>=c):
    return a
  elif (b>=a and b>=c):
    return b
  return c

# function to find maximum sum of subarray crossing the middle element
def max_crossing_subarray(ar, low, mid, high):
  global beginindex,endindex  
  beginindex = 1
  endindex = 1
  
  left_sum = -1000000
  sum = 0
  for i in range(mid, low-1, -1):
    sum = sum+ar[i]
    if (sum>left_sum):
      left_sum = sum
      beginindex=i  
      
      

  right_sum = -1000000
  sum = 0
  for i in range(mid+1, high+1):
    sum = sum+ar[i]
    if (sum>right_sum):
      right_sum = sum
      endindex=i         
  return left_sum+right_sum 

# function to calculate the maximum subarray sum
def max_sum_subarray(ar, low, high):
  if (high == low): # only one element in an array
    return ar[high]

  mid = (high+low)//2
  maximum_sum_left_subarray = max_sum_subarray(ar, low, mid)
  maximum_sum_right_subarray = max_sum_subarray(ar, mid+1, high)
  maximum_sum_crossing_subarray = max_crossing_subarray(ar, low, mid, high)

  # returning the maximum among the above three numbers
  return maximum(maximum_sum_left_subarray, maximum_sum_right_subarray, maximum_sum_crossing_subarray)

t0 = time.process_time()
pinakas1 = max_sum_subarray(A, 0, len(A)-1)

t1= time.process_time()
print("data1 : ",pinakas1,(beginindex,endindex),t1-t0)
beginindex=endindex=1

pinakas2 = max_sum_subarray(B, 0, len(B)-1)
t2= time.process_time()
print("data2 : ",pinakas2,(beginindex,endindex),t2-t1)



