n=int(input())
arr=list(map(int,input().split()))
key=int(input())
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print(mid)
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1