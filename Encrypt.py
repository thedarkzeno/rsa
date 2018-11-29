cod=[]
codf=[]
#public keys
n=93019
e=3
#Private keys
p=557
q=167
d=61531
def encode(msg, e, n):
    stri=""
    for ch in msg:
        cod.append(ord(ch))
    for x in range(0,len(cod),1):
        stri=stri + str(pow(cod[x],e)%n)
        stri=stri+" "
    print(stri)
def decode(msg, d, n):
    asd=""
    stri=""
    for k in range(0, len(msg), 1):
        if(msg[k]!=" " and k!=len(msg)-1):
            asd=asd + msg[k]
        else:
            if(k==len(msg)-1):
                 asd=asd + msg[k]
            codf.append(int(asd))
            asd="";  
    for x in range(0, len(codf),1):
        stri=stri + chr((pow(codf[x],d))%n)
    print (stri)
msg1=int(input("do you want to encode or decode?( 1 or 2)"))
if(msg1==1):
    msg=input("what would you like to encode? ")
    encode(msg, e, n)
else:
    msg=input("what would you like to decode? ")
    decode(msg, d, n)