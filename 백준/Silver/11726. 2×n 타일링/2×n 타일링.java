import java.io.*;
import java.util.*;

public class Main {
    /*
    2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하기
    1칸은 세로 1칸 방법
    2칸은 가로 2칸, 세로1칸 2가지 방법
    3칸이면 f(2)에서 세로 1칸추가  + f(1)에서 세로2칸 + f(1)에서 가로2칸 방식이 있다. => f(2)+2f(1)
    4칸이면 f(3)에서 세로 1칸 + f(2)에서 세로2칸, 가로2칸 => f(3)+2f(2)
     */
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long[] dp = new long[n + 2];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] %10007 + dp[i - 2]%10007;
        }
        System.out.print(dp[n]%10007);
    }
}