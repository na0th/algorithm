import sys

n = int(sys.stdin.readline())

# print(n)

trian = []
for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    trian.append(a)

# print(trian)

for k,item in enumerate(trian) :
    for i in range(len(item)) :
        if k > 0 :
            if i == 0 :
                item[i] = trian[k-1][0] + item[i]
            elif i == len(item)-1 :
                item[i] = trian[k-1][i-1] + item[i]
            else :
                item[i] = max(trian[k-1][i-1],trian[k-1][i]) +item[i]

print(max(trian[-1]))