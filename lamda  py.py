
#lambda  using function method
def veera(n):
    return lambda a:  a//n
ragav=veera(2)
print(ragav(20))

print("_____________________________________________________")

#getting prime number by using (filter) library file
def prime(x):
    for i in range(2,x):
        if x%2 ==0:
            return False
        else:
            return True
veera=filter(prime,range(20))
print("Prime Number Are :",list(veera))

print("_____________________________________________________")


#mapping method

def minus(x):
    return (x-1)*x
number=[4,5,6,7,8,9]

listminus=map(minus,number)
print(list(listminus))


print("_____________________________________________________________________________________________________")

                           #practise

def svct(x):
    return lambda v: v*x*v
veera=svct(1)
print(veera(7))

print("_____________________________________________________________________________________________________")


def even(n):
    for i in range(1,n):
        if n%2==0:
           return True
        else:
            return False
veera=filter(even,range(30))
print("Even Numbers are :",list(veera))


print("_____________________________________________________________________________________________________")

def cube(n):
    return n*n*n
digits=[1,2,3,4,5,6,7,8,9,0]

svct=map(cube,digits)
print(list(svct))

print("_____________________________________________________________________________________________________")
