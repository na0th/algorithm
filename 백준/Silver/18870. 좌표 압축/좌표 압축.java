import java.io.*;
import java.util.*;

public class Main {
    /*
    X(i) > X(j)를 만족하는 서로 다른 좌표 갯수
    알고리즘 분류 : Set, Map
    어떻게 풀이 ?
    1. 수를 중복 제거한다
    2. 오름차순 정렬
    3. 해당 수의 인덱스를 저장한다
    4. for문 순회하면서 해당 값의 인덱스를 출력

     */
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        Set<Integer> set = new TreeSet<>();
        List<Integer> realList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            set.add(num);
            realList.add(num);
        }

        List<Integer> list = new ArrayList<>(set); //{-10 -9 2 4 }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<list.size(); i++) {
            map.put(list.get(i), i);
        }
        for (int num : realList) {
            sb.append(map.get(num)).append(" ");
        }
        System.out.print(sb.toString().trim());
    }
}