p=557 #prime 1
q=167 #prime 2
n=p*q #public key
t=(p-1)*(q-1)#totient function
e=3

print ("Public keys: "+str(n)+"; "+str(e))

def invmult(a, remainder, mod):
    q=0
    for x in range(1, mod, 1):
        if((x*e)%mod==remainder):
            q=x
            
    return q
d=invmult(e, 1, t)




print ("Private keys: "+str(p)+"; "+str(q)+"; "+str(d))