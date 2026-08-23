arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        min_index=j
        if arr[j]<arr[min_index]:
            arr[i],arr[min_index]=arr[i],arr[min_index]
print(arr)