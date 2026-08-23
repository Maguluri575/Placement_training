# spiral matrix-1
n=int(input())
matrix=[[0] * n for _ in range(n)]
num=1
for r in range((n+1)//2):
    for c in range(r,n-r):
        matrix[r][c]=num
        num+=1
    for c in range(r+1,n-r):
        matrix[c][n-r-1]=num
        num+=1
    for c in range(n-r-2,r-1,-1):
        matrix[n-r-1][c]=num
        num+=1
    for c in range(n-r-2,r,-1):
        matrix[c][r]=num
        num+=1
print("\nMatrix:")
for row in matrix:
    print(*row)
pp=1
print("\n(0,0)")
for i in range(n):
    for j in range(n):
        if matrix[i][j]%11==0:
            print(f"({i},{j})")
            pp+=1
print("The Powerpoint:{pp}")