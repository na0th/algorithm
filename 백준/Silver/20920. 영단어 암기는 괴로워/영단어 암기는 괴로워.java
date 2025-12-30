import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    /*
    만들고자 하는 단어장이 있다. 다음과 같은 우선순위를 적용하여 만든다.
    1. 자주 나오는 단어일수록 앞에 배치
    2. 해당 단어의 길이가 길수록 앞에 배치
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치

    길이가 M이상인 단어만 외운다.

    분류 : 구현, 정렬
    어떻게 풀이?
    1. 정렬 조건으로 단어 카운팅, KEY의 길이, KEY의 사전순

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        Map<String, Integer> map = new HashMap<>();
        //map에 string >= m 인 것들 카운팅
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (s.length() >= m) {
                map.put(s,map.getOrDefault(s,0)+1);
            }
        }
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort((b, a) -> {
            int cmp = Integer.compare(a.getValue(), b.getValue());
            if (cmp !=0) return cmp;

            int stringLengthCmp = Integer.compare(a.getKey().length(), b.getKey().length());
            if (stringLengthCmp !=0) return stringLengthCmp;

            return b.getKey().compareTo(a.getKey());
        });

        for (Map.Entry<String, Integer> entry : list) {
            String key = entry.getKey();
            sb.append(key).append("\n");
        }
        System.out.print(sb.toString().trim());

    }
}
