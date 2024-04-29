a=int(input("enter the number of values"))
b=[]
for i in range(0,a):
     c=int(input("enter the number"))
     b.append(c)
key=int(input("enter the value to be found"))
for i in range (0,a):
     if b[i]==key:
          print("position=",i)
          print(b[i])
     
     
