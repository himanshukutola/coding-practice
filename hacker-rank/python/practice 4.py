# read total numbe rof lines in the txt file 

with open("mast.txt","r") as f:
 data = f.readlines()
 print(len(data))