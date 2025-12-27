import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    /*
    문자열 S를 T로 바꾸는 게임
    주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 판별하는 프로그램 작성

    연산은 2가지
    - 문자열의 뒤에 A를 추가한다.
    - 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

    분류 : 탐색.. 백트래킹? DFS? BFS?

    어떻게 풀이?
    1. 큐에서 뽑으면, 뽑은 문자열 길이가 T보다 작으면, 주어진 문자열로 연산1, 연산2을 수행하여 큐에 추가한다.
    2. 뽑은 문자열 길이가 T이면, 뽑은 문자열과 T를 비교한다. -> 같으면 얼리 True 리턴
    뽑은 문자열 길이가 T보다 크면, 큐에 추가하지 않는다.
    3. 큐에서 모든 연산을 수행해도 문자열과 같은 경우가 없었다면 False 반환


    했더니 메모리 초과.
    BFS는 문자열마다 2개씩의 큐 요소를 추가해서 큐가 폭발함 (분기 2^k)

    정방향은 2개의 분기가 생기니,
    역방향으로 1. A 제거 2. B 제거 및 REVERSE



    * */
    static boolean found = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<String> queue = new ArrayDeque<>();

        String s = br.readLine();
        String t = br.readLine();

        StringBuilder sb = new StringBuilder(t);
        queue.addFirst(sb.toString());

        while (!queue.isEmpty()) {
            String pick = queue.removeLast();
            
            if (pick.length() < s.length()) continue;

            if (pick.equals(s)) {
                found = true;
                break;
            }
            if (pick.endsWith("A")) {
                String newString = pick.substring(0, pick.length() - 1);
                queue.addFirst(newString);
            }
            if (pick.startsWith("B")) {
                String newString = pick.substring(1);
                String rev = new StringBuilder(newString).reverse().toString();
                queue.addFirst(rev);
            }
        }

        System.out.print(found ? 1 : 0);
    }


}
