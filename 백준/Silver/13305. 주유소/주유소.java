import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    주유소 최소 비용
    주유소에서 기름을 채워서 갈 수 있음
    알고리즘 분류 :
    어떻게 풀이?
    1.해당 주유소까지 최소 주유소 값으로 다음 주유소까지 이동한다
    2. 주유 값의 total을 구한다
     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] parts = br.readLine().split(" ");
        int[] dist = new int[n - 1];
        for (int i=0; i<n-1; i++) {
            dist[i] = Integer.parseInt(parts[i]);
        }
        int[] price = new int[n];
        String[] prices = br.readLine().split(" ");
        for (int i=0; i<n; i++) {
            price[i] = Integer.parseInt(prices[i]);
        }
        int minPrice = price[0];
        long totalPrice = 0;
        for (int i = 0; i < n-1; i++) {
            minPrice = Math.min(minPrice, price[i]);
            totalPrice += (long) minPrice * dist[i];
        }
        System.out.print(totalPrice);
    }
}
