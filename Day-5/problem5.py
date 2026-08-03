n=int(input())
if n<=1:
    print("Not a prime Number")
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
if prime:
    print("Prime")
else:
    print("Not a prime")
