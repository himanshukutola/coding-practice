#  with read ,readline , readlines

with open("mast.txt","r") as f:
 data =f.read()
 print("data of the file is :",data) 


 


with open("certificate.txt","r") as f:
 data =f.readlines()
 print(data)