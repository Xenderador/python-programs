#greater or not
import random
#random.randint(0,100)
listofvals = [random.randint(0,100) for i in range(10)]
num_ip = eval(input("please enter a number."))
for i in listofvals:
    if i<num_ip:
        print(i," is greater then",num_ip)
    elif i>num_ip:
        print(i," is lesser then",num_ip)
    else:
        print(i," is Same as ",num_ip)
#armstrong number
num_ip = (input("please enter a number."))
total =0
for i in num_ip:
    total+= int(i)**len(num_ip) 

    if total==int(num_ip):
        print("Armstrong number")
    else:
        print("Not an Armstrong Number")
    #prime number
    num_ip = (input("please enter a number."))
    if num_ip >1:
        for i in range(2,num_ip):
           if (num_ip%i)==0:
                print (num_ip," is not  a Prime number")
                break
           else:
                print(num_ip,"is a prime number")

