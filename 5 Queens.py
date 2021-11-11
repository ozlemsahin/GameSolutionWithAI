
import numpy
import random

# start tables
arr1 = numpy.zeros(5)
arr2 = numpy.zeros(5)
horizontalError = 0
diagonalError = 0
sumError = 0
parentError1 = 0
parentError2 = 0


    
# create table with random numbers
def createTable():
    
    for i in range(0,4):
        arr1[i] = random.randint(0,4)
    for i in range(0,4):
        arr2[i] = random.randint(0,4)    



# find errors in table
def findHorizontalErrors(arr):
    
    for currIndex in range(5):
        start = currIndex + 1
        for i in range(int(start),5):
            if(arr[currIndex] == arr[i]):
                global horizontalError 
                horizontalError = horizontalError + 1
    return horizontalError         

def findDiagonalErrors(arr):
    
    #up part
    for currIndex in range(5):
        global diagonalError 
        start = currIndex + 1
        count = 1
        for i in range(int(start),5):
            if(arr[currIndex]-count == arr[i]):
                diagonalError = diagonalError + 1
            count = count + 1
            
    #down part
    for currIndex in range(5):
        start = currIndex + 1
        count = 1
        for i in range(int(start),5):
            if(arr[currIndex]+count == arr[i]):
                diagonalError = diagonalError + 1
            count = count + 1
    
    return diagonalError    

def findFitness(arr):
    global sumError, diagonalError, horizontalError
    sumError += findHorizontalErrors(arr)
    sumError += findDiagonalErrors(arr)
    horizontalError = 0
    diagonalError = 0
    stock = sumError
    sumError = 0
    return stock

#crossover
def crossover(arr1, arr2):
    crossPoint = random.randint(1,3)
    for i in range(0,int(crossPoint)):
        arrNew1 = numpy.zeros(5)
        arrNew2 = numpy.zeros(5)
        copyArray(arrNew1,arr1)
        copyArray(arrNew2,arr2)
        
    for i in range(int(crossPoint),4):
        arrNew1[i] = int(arr2[i])
        arrNew2[i] = int(arr1[i])
        
    return [arrNew1, arrNew2]

    
def copyArray(arr1, arr2):

    for i in range(len(arr1)):
        arr1[i] = arr2[i]

    
#mutation       
def mutation(arr):
    mutationPoint = random.randint(0,4)
    arr[int(mutationPoint)] = random.randint(0,4)


def createGeneration():
    global arr1
    global arr2
    
    #first we have 2 parent 
    arrs = crossover(arr1,arr2)
    print("after crossover:")
    print(arrs[0])
    print(arrs[1])
    mutation(arrs[0])
    mutation(arrs[1])
    print("after mutation:")
    print(arrs[0])
    print(arrs[1])
    err1 = findFitness(arrs[0])
    err2 = findFitness(arrs[1])
    print("fitness by order")
    print(arr1)
    print(parentError1)
    print(arr2)
    print(parentError2)
    print(arrs[0])
    print(err1)
    print(arrs[1])
    print(err2)
    
    #find least errored 2 table
    if(err1<parentError1):
        arr1 = arrs[0];
    elif(err1<parentError2):
        arr2 = arrs[0]
    if(err2<parentError1):
        arr1 = arrs[1];
    elif(err2<parentError1):
        arr2 = arrs[1]
    
    print("after selektion:")
    print(arr1)
    print(arr2)
    
    
#to run    
createTable() #create parent
print(arr1)
print(arr2)


for i in range(100):
    print("BEGINN")
    print(arr1)
    print(arr2)
    parentError1 = findFitness(arr1)
    parentError2 = findFitness(arr2)
    createGeneration()
    horizontalError = 0
    diagonalError = 0
    sumError = 0
    parentError1 = 0
    parentError2 = 0