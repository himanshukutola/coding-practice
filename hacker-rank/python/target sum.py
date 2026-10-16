
import array
a=[]
m= int(input("Enter the number of elements in the array: "))

for i in range(m):
    a.append(int(input("Enter element ")))

target= int(input("Enter the target sum: "))

for i in range(len(a)):
    for j in range( i+1,len(a)):
        if a[i] + a[j] == target:
            print(a[i], "and", a[j])
