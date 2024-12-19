'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
위의 코드임.
N이 주어졌을 때, fibonacci(N)을 호출했을 때,
0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

알고리즘 분류 : DFS?

어떻게 풀이?
IF 문으로 cnt를 세면 되지 않을까.. fibonacci의 파라미터가 뭔지 확인하고 cnt로 센다?

'''
import sys
n = int(sys.stdin.readline())

dp_zero = {0:1,1:0}
dp_one = {0:0,1:1}
def dfs(k) :
    if k in dp_zero :
        return dp_zero[k],dp_one[k]


    zero_1,one_1 = dfs(k-1)
    zero_2,one_2 = dfs(k-2)

    dp_zero[k] = zero_1 + zero_2
    dp_one[k] = one_1 + one_2

    return dp_zero[k],dp_one[k]

for _ in range(n):

    num = int(sys.stdin.readline())
    count_zero,count_one = dfs(num)
    print(count_zero,count_one)


