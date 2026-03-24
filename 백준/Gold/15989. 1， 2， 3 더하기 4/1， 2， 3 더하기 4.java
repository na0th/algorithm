import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다.
    합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다
    알고리즘 분류 : DP?
    어떻게 풀이?
    1은 1가지
    2는 1+1, 2
    3은 111, 12, 3
    12 + 3
    13+ 2   둘은 같은 케이스라 중복인데..

    23+1
    12+3도 그렇고..

    1로만 만든다..
    1,2 두개만 쓴다.
    1,2,3다 쓴다.

    f(6)은 1로만 만든거 1개, 1,2 2개쓰는 거, 1,2,3까지 다쓰는경우


    1만 써서 만드는 경우
    1,2 써서 만드는 경우 2를 0개 쓴 경우, 2를 1개 쓴 경우..
    1,2,3 써서 만드는 경우 3을 0개 쓴 경우, 3을 1개 쓴 경우?
    g(n) => 1 + g(n-2)
                1 + g(n-4)
                    1 + g(n-6)...
    g(0) = 0
    g(1) = 1
    g(2) = 2
    g(3) = 1 + g(1)  = 1+ 1  = 2
    g(4) = 1 + g(2) = 1 + 2 = 3  => 1111 112 22
    g(5) = 1 + g(3) = 1 + 2 =  3  => 11111 1112 122
    g(6) = 1 + g(4) = 1 + 3 = 4 => 111111 11112 1122 222
    g(n) = (g/2) + 1

    f(6) = g(6) + f(3)
         = g(6) + g(3) + f(0)
         = g(6) + g(3)
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n = Integer.parseInt(br.readLine());

        int[] f = new int[10001];
        int[] g = new int[10001];
        //초기값 셋팅
        f[0] = 0;
        f[1] = 1;
        f[2] = 2;
        f[3] = 3;

        g[0] = 0;
        g[1] = 1;
        g[2] = 2;
        // 점화식
        for (int i = 3; i < 10001; i++) {
            g[i] = 1 + g[i-2];
        }
        for (int i = 4; i < 10001; i++) {
            f[i] = g[i] + f[i-3];
        }

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            sb.append(f[num]).append((" \n"));
        }
        System.out.print(sb.toString().trim());
    }
}
