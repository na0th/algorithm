import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
    EX) HHPHHPHPHPHP

    식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K가 주어진다.
    햄버거를 먹을 수 있는 사람의 최대 수를 구하시오.

    분류 : 그리디?
    어떻게 풀이?
    1. 사람이 나오면 왼쪽에서 햄버거를 최대한 찾아본다.
    2. 오른쪽에서 최대한 햄버거를 찾는다.
    3. 햄버거를 먹을 수 있는 사람을 카운팅한다.
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");

        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);

        String s = br.readLine();

        StringBuilder sb = new StringBuilder(s);
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (sb.charAt(i) == 'P') {

                //왼쪽으로 k개를 탐색.
                boolean check = false;
                for (int j = i - k; j < i; j++) {
                    if (j < 0) {
                        continue;
                    }
                    if (sb.charAt(j) == 'H') {
                        sb.setCharAt(j, 'h');
                        cnt++;
                        check = true;
                        break;
                    }
                }
                if (!check) {
                    for (int j = i+1; j <= i+k; j++) {
                        if (j >= s.length()) {
                            continue;
                        }
                        if (sb.charAt(j) == 'H') {
                            sb.setCharAt(j, 'h');
                            cnt++;
                            break;
                        }
                    }
                }

            }
        }
        System.out.print(cnt);

    }
}
