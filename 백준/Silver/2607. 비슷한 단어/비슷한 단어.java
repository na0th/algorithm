import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    /*
    두 개의 단어가 같은 종류의 문자로 이루어져 있다.
    같은 문자는 같은 개수 만큼 있다.

    두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나,
    하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에
    -> 이들 두 단어를 서로 비슷한 단어라고 한다.

    분류 : 구현
    어떻게 풀이?
    1. 문자의 갯수를 센다 EX) D: 1 , O : 1 , G:1 (DOG)
    2. 각 문자열마다 문자의 갯수를 비교 D: 1 , O : 2 , G : 1 (GOOD)
    3. 같은 구성, 한 문자를 더하거나 뺀 경우, 하나의 문자를 다른 문자로 바꾼 경우

    틀림.. A ->  B로 치환된 경우는?
    D,O,G 1 1 1
    D,O,B 1 1 1
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Character, Integer> map = new HashMap<>();
        int answer = 0;

        String s = br.readLine();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        for (int i = 0; i < n-1; i++) {
            String string = br.readLine();
            // 초과한 글자수 <=1 && 부족한 글자수 <=1 이면 비슷한 글자이다.
            int extra = 0, missing = 0;
            Map<Character, Integer> diff = new HashMap<>(map);
            for (char c : string.toCharArray())
                diff.put(c, diff.getOrDefault(c, 0) - 1);

            for (Map.Entry<Character, Integer> entry : diff.entrySet()) {
                int cnt = entry.getValue();
                if (cnt > 0) {
                    extra += cnt;
                }else{
                    missing -= cnt;
                }
            }

            if (extra <= 1 && missing <= 1) {
                answer++;
            }

        }
        System.out.print(answer);


    }
}
