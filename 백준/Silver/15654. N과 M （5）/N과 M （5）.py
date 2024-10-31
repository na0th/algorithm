import sys
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))

# print(n,m)
num_list.sort()
# print(num_list)


def permutations(num_list,save_list,pick_count):
    if pick_count == 0 :
        print(*save_list)
        return
        # 끝..

    for i in range(n) :
        if num_list[i] not in save_list:
            save_list.append(num_list[i])
            permutations(num_list,save_list,pick_count-1)
            save_list.remove(num_list[i])

save_list = []
permutations(num_list,save_list,m)