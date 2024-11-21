'''

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

이렇게 나, 왼쪽 자식, 오른쪽 자식이 주어졌을 때, 전위 중위 후위 순회 순서 출력

알고리즘 분류: 트리 순회

어떻게 풀이?
일단 트리 자료구조를 만들어야 함..?
graph= {
1: [2,3]
2: [0,3]
3: [0,0]
} 뭐 이런 식으로 표현했다면 가능하려나..

그러면 전위 순회는? 내가 전에 위치
 -> 나 왼 오

 중위 순회는 내가 중간에 위치
 ->왼 나 오

 후위 순회는 내가 후에 위치
 -> 왼 오 나


 전위 순회는 왼쪽 오른쪽이 있다면 나는 일단 방문
 내가 방문되어 있으면 왼쪽을 확인? 왼쪽이 방문 안되어 있으면 방문 후 왼쪽으로 이동

 graph보다는 트리로 구현해보기
'''

class Node :
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

import sys
n = int(sys.stdin.readline())


def build_tree(n):
    nodes={}
    root = None
    for _ in range(n):

        mid,left,right = sys.stdin.readline().split()
        if mid not in nodes:
            nodes[mid] = Node(mid)
        current = nodes[mid]

        if _ == 0 :
            root = current

        if left != '.':
            if left not in nodes:
                nodes[left] = Node(left)
            current.left = nodes[left]


        if right != '.':
            if right not in nodes:
                nodes[right] = Node(right)
            current.right = nodes[right]

    return root

def preorder(node):
    if not node :
        return
    print(node.data,end="")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node :
        return
    inorder(node.left)
    print(node.data,end="")
    inorder(node.right)

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end="")
root = build_tree(n)

preorder(root)
print()
inorder(root)
print()
postorder(root)