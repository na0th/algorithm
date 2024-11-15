'''
과장은 하면서, 거짓말쟁이가 되기는 싫다?

첫 째줄에 사람 수 n과 파티 수 m이 주어짐
둘 째줄에 진실을 아는 사람 수와 번호 주어짐

3번째 줄부터는 파티에 오는 사람..


문제 설명 :
진실을 아는 사람 파티에서는 거짓말을 하면 안됨..
+ 어떤 사람이 어떤 파티에서는 진실을 듣고,
또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.

지민이는 이런 일을 모두 피해야 한다.

알고리즘 분류 : 구현?

어떻게 풀이 ?
1,2,3,4 가 진실 근데 10이 3,10이랑 있을 때 진실을 들었는데.. 따로 있으니까 거짓이면 거짓
1 10
2 3 10
이걸 어떻게..?

진실을 들었는데, 다른 모임에서는 거짓말을 들은 집단..
진실을 들은 집단하고 거짓을 들은 집단을 나눔..

그래서 진실 set에 append, 거짓 set에 append
그다음에 다시 거짓set으로만 있는지 체크해서 +1

'''

import sys



n,m = map(int,sys.stdin.readline().split())
input_list = list(map(int,sys.stdin.readline().split()))

true_set = set(input_list[1:]) if len(input_list) > 1 else set()


parties = []
for _ in range(m):
    next_put_list = list(map(int,sys.stdin.readline().split()))
    parties.append(next_put_list[1:])

changed = True
while changed:
    changed = False
    for party in parties:
        if true_set & set(party):
            before_update_size = len(true_set)
            true_set.update(party)
            if len(true_set) > before_update_size:
                changed = True

lie_count = 0
for party in parties:
    if not (true_set & set(party)):
        lie_count += 1

print(lie_count)

