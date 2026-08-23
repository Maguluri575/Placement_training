n=int(input())
arr=list(map(int,input().split()))
key=int(input())
found=False
for i in range(n):
    if arr[i]==key:
        print(i)
        found=True
        break
if not found:
    print(-1)
