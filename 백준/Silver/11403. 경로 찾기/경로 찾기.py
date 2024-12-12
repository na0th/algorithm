import sys
n = int(sys.stdin.readline())

matrix = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for row in matrix:
    print(*row)