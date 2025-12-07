import java.util.*;
import java.io.*;

public class Main {
    /*
    미래의 주가를 알게되었을 때, 최대 이익을 구하시오
    홍준이는 매일 3가지중 1개의 행동을 한다.
    방법 1) 주식 하나를 산다.
    방법 2) 원하는 만큼 주식을 판다.
    방법 3) 아무것도 하지 않는다.

    분류 : ?
    어떻게 풀이 ?
    테스트 케이스가 100만개 ->  시간 복잡도 O(N) -> FOR문 1번 순회해야 함
    사는 것은 1개 뿐, 산 시점보다 뒤에 높은 가격이 나오기만 하면 사는 것이 이득

    결국 내 뒤에 나보다 높은 숫자가 나오기만 하면 일단 이득이니 그걸 더해면 됨.
    최대 이득은 (나)와 (내 뒤에 숫자중 최대값)과의 차이를 모두 더한 것.




     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 테스트 케이스 수
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            // 각 테스트 케이스마다
            int N = Integer.parseInt(br.readLine()); // 날짜 수

            int[] price = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                price[i] = Integer.parseInt(st.nextToken());
            }

            // ...
            // 거꾸로 최대값들 갱신하기 7 8 3 5 1 -> 8 8 5 5 1
            int[] suffixMax  = new int[price.length];
            int max = price[price.length - 1];

            for(int i = price.length-1; i>=0; i--){
                if (price[i] > max) {
                    max = price[i];
                }
                suffixMax[i] = max;
            }
            long total = 0;
            for(int i=0; i<price.length; i++){
                total += (suffixMax[i]-price[i]);
            }
            sb.append(total).append('\n');
        }
        System.out.print(sb.toString());
    }
}
