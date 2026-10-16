#  with read ,readline , readlines

with open("mast.txt","r") as f:
 data =f.read()
 print("data of the file is :",data) 


 
with open("mast.txt","r") as f:
 data =f.readlines()
 data1 =f.readline()

 data2 =f.readline()
 data3 =f.readline()
data4 =f.readline()
data5 =f.readline()
data6 =f.readline()
data7 =f.readline() 
print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)    
print(data)