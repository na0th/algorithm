a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*",end="")
    for i in range(a-1):
        print("*",end="")
    print()
# print(a + b)