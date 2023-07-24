def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print("chose the function u wanna perform")
print("1.Add")
print("2.sub")
print("3.mult")
print("4.div")

choice=input("place the choice(1/2/3/4):")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
 
if choice =="1":
    print(a,"+",b,"=",add(a,b))
elif choice =="2":
    print(a,"-",b,"=",sub(a,b))
elif choice =="3":
    print(a,"*",b,"=",mult(a,b))
elif choice =="4":
    print(a,"/",b,"=",div(a,b))
else:
    print("invalid input")













