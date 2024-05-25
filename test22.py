n=int(input("Enter the number: "))
# for i in range(0,n+1):
if (n%2) == 0:
        print(n,"is even number")
else:
        print(n,"is odd number")
        
        
        
 
n=int(input("Enter the number: "))
if n>1:
    for i in range(2,int(n/2)+1):
        if (n%i==0):
            print(n,"is not prime number")
            break
    else:
        print(n,"is prime number")
else:
    print(n,"is not prime number")
    
    
1
2 2
3 3 3 
4 4 4 4 
5 5 5 5 5
    

def triangle():
    for i in r



    n=int(input("Enter the number: "))
fact=1
if n<0:
    print("negative number factorial not exist")
elif (n==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
       fact=fact*i
    print("factorial of",n,"is",fact)