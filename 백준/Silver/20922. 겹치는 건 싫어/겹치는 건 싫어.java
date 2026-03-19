import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Main {
    /*
    같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이 구하기.
    N은 200000이하, K는 100이하
    알고리즘 분류 : 구간 카운트?
    어떻게 풀이?
    1. LEFT = 0, RIGHT는 0 부터 시작
    2. 같은 원소가 전부 K개를 못넘는지 체크 -> 못넘기면 RIGHT+1 넘기면 LEFT+1
    3. 구간 최대 길이를 갱신
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        List<Integer> list = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .boxed()
                .collect(Collectors.toList());
        int left = 0, right = 0;
        int maxLength = 1;
        Map<Integer, Integer> map = new HashMap<>();


        // left right 0,0에서 시작  + checkCount해서 countCount가 true면 right+1 , false면 left+1
        // 3 2 5 5 6 4 4 5 7
        map.put(list.get(0), 1);
        while (right < n - 1) {
            int now = list.get(right);
            if (map.get(now) > k) {
                int num = list.get(left);
                map.put(num, map.getOrDefault(num, 0) - 1);
                left++;
            } else {
                right++;
                int num = list.get(right);
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
            if (map.get(list.get(right)) <= k) {
                if (maxLength < (right - left + 1)) {
                    maxLength = right - left + 1;
                }
            }

        }
        System.out.print(maxLength);
    }
}
