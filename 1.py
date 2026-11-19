import math
a=0
for i in range(1,686001):
    if (i%2!=0):
        a+= i**2

#print(a)

b=0



for i in range(1,1000):
    if (i%3==0 or i%5==0):
        b+=i
#print(b)

def fib():
    a=1
    b=2
    c=0
    while(b<4000000):
        if(b%2==0):
            c+=b
        z=a
        a=b
        b=b+z
    print(c)



def is_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            return False
    return True


def biggest_prime():
    a=0
    for i in range (2,600851475143//2):
        if(is_prime(i)):
            if (600851475143%i==0):
                print(i)
                a=i
    print(a)

biggest_prime()