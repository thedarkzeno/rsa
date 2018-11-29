import time
import math
number = int(input("Get primes between 1 and : "))
ini = time.time()
count=0
primes=[2]
step=2
initial=3
if(number<0):
    print('error, value must be greater than 0')
else:
    print("The number 2 is prime!")
    for num in range(initial,number+1,step):
        raiz=math.sqrt(num)
        count=0
        for num2 in range(0,len(primes),1):
        
            if(num % primes[num2] == 0):
                count=count+1
            if(count>1):
                break
            if(primes[num2]>raiz):
                break
        if(count<1):
            print("The number "+str(num)+" is prime!")
            primes.append(num)
    end = time.time()
    print("")
    print(str(len(primes))+" prime numbers between 1 and "+str(number))
    print("")
    print("execution time: "+ str(end-ini))
