#declare array
A = []

#number of elements as input
n=9

#getting key board inputs bethween 10 to 20
for i in range(0,n):
    number = int(input("Enter Value : "))
    if(number>10 and number<20):
        A.append(number)
    else:
        print("invalid process")
    i=i+1
print(A)

#function
def insertionSort(A):

    for i in range(1,len(A)): #traverse the length of the array
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1]= A[j]
            j = j-1
        A[j+1]=key
insertionSort(A)
print("Orderd Array : ")
print(A)
