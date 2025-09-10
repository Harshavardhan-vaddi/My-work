r,c=map(int,input().split())

m=[]
for i in range(r):
    m.append(list(map(int,input().split())))
print(m)

mat=[[0 for a in range(c+2)] for b in range(r+2)]
for i in range(r):
    for j in range(c):
        mat[i+1][j+1]=m[i][j]

print(mat)

x=[[0,-1],[-1,0],[0,1],[1,0]]

for i in range(1,len(mat)-1):
    for j in range(1,len(mat[i])-1):
        if mat[i][j]==1 or mat[i][j]==(-1):
            for dx, dy in x:
                if (mat[i+dx][j+dy]==2):
                    mat[i][j]=2
                    break

for i in range(1,len(mat)-1):
    for j in range(1,len(mat[i])-1):
        print(mat[i][j],end=" ")
    print()