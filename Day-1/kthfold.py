try:
    n=int(input())
    arr=list(map(int,input().split()))
    key=int(input())
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    if key>=1 and key<=n:
        print(arr[key-1])
    else:
        print("invalid k")
except:
    print("Invalid input")