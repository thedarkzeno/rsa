import time
import math
number = int(input("Tipe the public key that you would like to break (ex: 93019) : "))
ini = time.time()
count=0
countDiv=0
primes=[2]
step=2
initial=3
end=0
root=math.sqrt(number)
if(number<=0):
    print('error, value must be greater than 0')
else:
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
            
            if(number%num==0):
                countDiv+=1
                print("parent prime: "+str(num))
            primes.append(num)
            if(countDiv==2):
                break
        if(countDiv==2):
                break
    end = time.time()
    print("")
    print("")
    print("Execution time: "+ str(end-ini))