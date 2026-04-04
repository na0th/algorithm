import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    김진영이 듣도 보도 못한 사람의 명단을 구하기
    듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람 명단도 마찬가지

    알고리즘 분류 : 해시
    어떻게 풀이 ?
    1. 2개의 해시맵에 명단 저장
    2. 한쪽 해시맵 순회하면서 다른 해시에도 존재하면 추가
    3. 정렬
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        Set<String> set1 = new HashSet<>();
        Set<String> set2 = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set1.add(br.readLine());
        }
        for (int i = 0; i < m; i++) {
            set2.add(br.readLine());
        }
        List<String> list = new ArrayList<>();
        for (String s : set1) {
            if (set2.contains(s)) {
                list.add(s);
            }
        }
        Collections.sort(list);
        sb.append(list.size()).append("\n");
        for (String s : list) {
            sb.append(s).append("\n");
        }
        System.out.print(sb.toString().trim());
    }
}
