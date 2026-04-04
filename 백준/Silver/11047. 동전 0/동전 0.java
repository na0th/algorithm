import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    /*
    N종류의 동전이 있고, 합이 k인 경우를 만드려고 할 떄, 사용한 동전 갯수의 최솟값 구하기
   (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
   위의 문구 때문에, 비싼 동전부터 그리디하게 나누면 되지 않을까?
    알고리즘 분류 : 그리디
    어떻게 풀이 ?
    1. 비싼 동전부터 나누면서 동전 count 구하기
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int money = Integer.parseInt(parts[1]);
        int[] coins = new int[n];
        for (int i = n-1; i >=0; i--) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        int coinCnt = 0;

        int idx = 0;
        while (money > 0) {
            coinCnt += money/coins[idx];
            money = money % coins[idx];
            idx++;
        }

        System.out.print(coinCnt);
    }
}
