n=int(input())
power=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**power
    temp//=10
if sum==n:
    print("Armstrong")
else:
    print("Not a Armstrong")