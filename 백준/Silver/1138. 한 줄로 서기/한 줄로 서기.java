import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    /*
    N명의 사람들은 매일 아침 한 줄로 선다.
    사람들은 줄 서는 위치를 기록해 놓는다.
    사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만 기억한다. N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

    분류 : 완전탐색? 그리디

    어떻게 풀이 ?
    자신보다 큰 사람이 왼쪽에 몇명있는지 기억한다.
    -> 제일 작은 애부터 시작하면 남은 자리 중에서 자기 자리는 정해져 있음
    1 2 3 4 인데 2 1 1 0 이라면
    1 2 3 4 중에 인덱스 2인 3
    3를 제외한 1 2 4 중 인덱스 1인 2
    2을 제외한 1 4 중 인덱스 1 인 4
    4을 제외한 1 중 인덱스 0인 1

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] cnt = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(i);

        int[] arr = new int[n];

        for (int i = 1; i <= n; i++) {
            int idx = cnt[i-1];
            arr[list.get(idx)] = i;
            list.remove(idx);
        }
        StringBuilder sb = new StringBuilder();
        for (int x : arr) sb.append(x).append(' ');
        System.out.println(sb.toString().trim());
    }
}
