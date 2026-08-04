r,c=list(map(int,input().split()))
A=[list(map(int,input().split())) for _ in range(r)]
for j in range(c):
    for i in range(r):
        print(A[i][j],end=" ")
    print()