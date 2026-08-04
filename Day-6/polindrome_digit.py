n=int(input())
temp=n
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
if n==rev:
    print("Polindrome")
else:
    print("Not a Polindrome")