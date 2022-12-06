import random
random.seed(1053577)

class HashTable:
    
    def __init__(self):
        self.max_load_factor = 0.5
        self.resizes = 0
        self.count_collisions = 0
        self.size = 0
        self.INITIAL_CAPACITY = 997
        self.table = [None]*self.INITIAL_CAPACITY

    def len(self):
        return self.size

    def number_of_resizes(self):
        return self.resizes

    def numcollissions(self):
        return self.count_collisions 
    
    def insert(self,key,value1,value2):
        self.size += 1
        key_hash = self.hash(key)
        while self.table[key_hash] is not None: 
            if self.table[key_hash][0] == key:
                ##############
                tc = self.table[key_hash][1]
                tc+=value1
                totaldays = []
                beforedays = self.table[key_hash][2]
                for i in range(6):
                    totaldays.append(beforedays[i]+value2[i])
                tuple = (key,tc,totaldays)
                ##############
                self.size -= 1
                break
            else:
                self.count_collisions += 1
                key_hash = self.increment_key(key_hash)
        if self.table[key_hash] is None:
            tuple = (key,value1,value2)
        self.table[key_hash] = tuple
        if self.size / float(self.INITIAL_CAPACITY) >= self.max_load_factor:
            count_collisions=0
            self.resize()
            self.resizes+=1

    def get(self,key):
        index = self.find_item(key)
        return self.table[index][1],self.table[index][2]

    def delete(self,key):
        index = self.find_item(key)
        self.table[index] = None

    def hash(self,key):
        return hash(key) % self.INITIAL_CAPACITY

    def increment_key(self,key):
        return (key+1) % self.INITIAL_CAPACITY

    
    def find_item(self,key):
        key_hash = self.hash(key)
        if self.table[key_hash] is None:
            raise KeyError
        if self.table[key_hash][0] != key:
            original_key=key_hash
            while self.table[key_hash][0] != key:
                key_hash = self.increment_key(key_hash)
                if self.table[key_hash] is None:
                    raise KeyError
                if key_hash == original_key:
                    raise KeyError
        return key_hash
    
    def resize(self):
        self.INITIAL_CAPACITY = self.INITIAL_CAPACITY * 2
        self.size = 0
        old_table = self.table
        self.table = [None] * self.INITIAL_CAPACITY
        for tuple in old_table:
            if tuple is not None:
                self.table[self.size] = tuple

    def findmostcost(self):
        maximum_cost = 0
        position_cost = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i][1] > maximum_cost:
                    maximum_cost = self.table[i][1]
                    position_cost = i
        return position_cost

    def findmostvisits(self):
        maximum_visits = 0
        position_visits = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if sum(self.table[i][2]) > maximum_visits:
                    maximum_visits = sum(self.table[i][2])
                    position_visits = i
        return position_visits


        
H=HashTable()
theseis=[]
l=["A","B","C","D"]
card="1234567890123456"
meres=["ΔΕΥΤΕΡΑ","ΤΡΙΤΗ","ΤΕΤΑΡΤΗ","ΠΕΜΠΤΗ","ΠΑΡΑΣΚΕΥΗ","ΣΑΒΒΑΤΟ"]
m=0
t=0
w=0
th=0
f=0
s=0


for i in range(1000000):
    week=[6]
    card=list("1234567890123456")
    k=0
    while k<4:
        y=random.randint(0,15)
        if y not in theseis:
            theseis.append(y)
            k=k+1
        
    dictionary = dict(zip(theseis,l))
    theseis=[]
    for j in range(16):
        if j in dictionary:
            card[j]=dictionary[j]
    card="".join(card)
    Day=random.choice(meres)
    if Day==meres[0]:
            week=[1,0,0,0,0,0]
            m+=1
    elif Day==meres[1]:
            week=[0,1,0,0,0,0]
            t+=1
    elif Day==meres[2]:
            week=[0,0,1,0,0,0]
            w+=1
    elif Day==meres[3]:
            week=[0,0,0,1,0,0]
            th+=1
    elif Day==meres[4]:
            week=[0,0,0,0,1,0]
            f+=1
    elif Day==meres[5]:
            week=[0,0,0,0,0,1]
            s+=1
    
    
    dictionary={}
    Cost=random.randint(10,100)

    H.insert(card,Cost,week)
   

print(H.table)
#######################################################################
position = H.findmostcost()    
print("(Α) Η ΚΑΡΤΑ ΜΕ ΤΟ ΜΕΓΑΛΥΤΕΡΟ ΠΟΣΟ ΠΛΗΡΩΜΩΝ ΕΙΝΑΙ Η : ",H.table[position][0],"\n    ΜΕ ΣΥΝΟΛΙΚΟ ΠΟΣΟ : ",H.table[position][1])
#######################################################################
pos = H.findmostvisits()
print("(Β) Η ΚΑΡΤΑ ΜΕ ΤΟ ΜΕΓΑΛΥΤΕΡΟ ΠΛΗΘΟΣ ΕΠΙΣΚΕΨΕΩΝ ΕΙΝΑΙ Η : ",H.table[pos][0],"\n    ΜΕ ΣΥΝΟΛ0 ΕΠΙΣΚΕΨΕΩΝ : ",sum(H.table[pos][2]))     
#######################################################################
total_visits=[m,t,w,th,f,s]
total_visits_per_day=[]
p=0
for i in range(6):
    total_visits_per_day.append([])
    day = meres[i]
    visits = total_visits[i]
    total_visits_per_day[p]=[day,visits]
    p+=1
total_visits_per_day.sort()
print("(Γ) Η ΜΕΡΑ ΜΕ ΤΙΣ ΠΕΡΙΣΣΟΤΕΡΕΣ ΕΠΙΣΚΕΨΕΙΣ ΕΙΝΑΙ Η : ",total_visits_per_day[5][0],"\n    ΜΕ ΣΥΝΟΛΟ ΕΠΙΣΚΕΠΤΩΝ : ",total_visits_per_day[5][1])
#########################################################################
print("(Δ) Ο ΑΡΙΘΜΟΣ ΤΩΝ ΣΥΓΚΡΟΥΣΕΩΝ ΓΙΑ LOAD FACTOR = 0.5 : ",H.numcollissions())
