'''
상근이는 나무 M미터가 필요하다.
목재절단기를 이용해서 나무를 구할것이다.

목재절단기는
상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다.
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.
나무의 높이가 20, 15, 10, 17이고 지정한 높이가 15
자른 후 15, 15, 10, 15가 될 것이고,

상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다)

적어도 M미터의 나무를 집에 가져가기 위해서 설정할 수 있는 높이의 최댓값을 구하기 (높이는 양의 정수)

입력 :
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
둘째 줄에는 나무의 높이가 주어진다.

적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

알고리즘 분류 : 이분 탐색?

어떻게 풀이 ?
이분 탐색해서 크면 내리고, 작으면 올림

'''
import sys

n,m = map(int,sys.stdin.readline().split())

trees = list(map(int,sys.stdin.readline().split()))

trees.sort()

def binary_search(left,right,target):
    if left > right:
        return right

    mid = (left + right) // 2

    total = sum(tree - mid for tree in trees if tree > mid)

    if total == target :
        return mid

    elif total < target :
        return binary_search(left,mid-1,target)

    else :
        return binary_search(mid+1,right,target)

print(binary_search(0,max(trees),m))
