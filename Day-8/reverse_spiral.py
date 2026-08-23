# spiral matrix-2
n=int(input())
matrix=[]
num=1
for i in range(n):
    row=[]
    for j in range(n):
        row.append(num)
        num+=1
    matrix.append(row)
print("Spiral Traversel:")
for r in range((n+1)//2):
    for c in range(r,n-r):
        print(matrix[r][c],end=" ")
    for c in range(r+1,n-r):
        print(matrix[c][n-r-1],end=" ")
    if r!=n-r-1:
        for c in range(n-r-2,r-1,-1):
            print(matrix[n-r-1][c],end=" ")
        for c in range(n-r-2,r,-1):
            print(matrix[r][c],end=" ")