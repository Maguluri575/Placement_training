import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
x,y=a,b
while y:
    x,y=y,x%y
gcd=x
print((a*b)//gcd) 
