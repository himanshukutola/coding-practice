# write a program to read a text from a given certificate.txt and find whether it contains the word live

f= open("certificate.txt","r")
data = f.read()
data = data.lower()
if "live" in data:
    print("yes")
else:
    print("no")
