from collections import defaultdict,deque
import sys

n = int(sys.stdin.readline())
tree = defaultdict(list)
for i in range(n-1) :
    a, b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent = {1: None}

queue = deque([1])
while queue :
    current = queue.popleft()
    for child in tree[current] :
        if child not in parent :
            parent[child] = current
            queue.append(child)

parent = dict(sorted(parent.items()))
for k,v in parent.items() :
    if k == 1 :
        continue
    print(v)




