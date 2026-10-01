a ={}
n= int (input("enter the number of element "))
for i in range(n):
    key = input("enter the key")
    value = input ("enter the value")
    a[key]=value
print("1 for print \n 2 for insert \n 3 for deletion \n 4 for clear \n 5 for copy in b{}\n  6 testing key \n 7 see value  \n 8 for get method ")
a= int(input ("enter the choice"))
if a ==1 :
   print(a)
elif a==2:
    key, value = input("Enter key and value: ").split()
    a[key] = value
elif a==3:
    print(" 1 to delete element \n 2 to delete dictionary")
    b = int(input("enter the choice"))
    if b == 1:
        key = input("enter the key to delete")
        if key in a:
            del a[key]
            print(f"Key '{key}' deleted successfully.")
        else:
            print(f"Key '{key}' not found in the dictionary.")  
elif a ==4 :
    a.clear
    print("dictionary cleared")
elif a== 5:
    b = a.copy()
    print("Copied dictionary:", b)
elif a==6:
    key = input("Enter the key to test: ")
    if key in a:
        print(f"Key '{key}' exists in the dictionary.")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")
elif a==7:
    key = input("Enter the key to retrieve value: ")
    if key in a:
        print(f"Value for key '{key}': {a[key]}")
    else:
        print(f"Key '{key}' not found in the dictionary.")    
elif a==8:
    key = input("Enter the key to get value using get method: ")
    value = a.get(key, "Key not found")
    print(f"Value for key '{key}': {value}")
else :
    print("invalid choice")