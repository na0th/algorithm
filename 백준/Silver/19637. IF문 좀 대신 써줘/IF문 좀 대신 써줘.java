import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    전투력 시스템
    A이하는 WEAK, B이하는 NORMAL, C 이하는 STRONG이라는 표현을 붙인다고 하자.

    주의 : 어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.
       = 같은 상한선을 가진 칭호가 뒤에 나오면 등록하지 않으면 된다.
       = 전투력이 주어지면, 맨 앞 칭호부터 상한선 밑에 해당하는지 확인하면 된다.(비내림차순)

    분류 : 구현
    (1 ≤ N, M ≤ 10^5)

    시간 초과!! 10^5으로 n^2이 나와서 초과됨.. 이분탐색해서 값을 찾아야 한다.
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        Map<String, Integer> map = new HashMap<>();
        Map<Integer, String> reverse = new HashMap<>();

        Set<Integer> used = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] sets = br.readLine().split(" ");
            int limitNum = Integer.parseInt(sets[1]);
            if (used.contains(limitNum)) continue;
            
            used.add(limitNum);
            map.put(sets[0], limitNum);
            reverse.put(limitNum, sets[0]);
        }
        List<Integer> list = new ArrayList<>(reverse.keySet());
        Collections.sort(list);
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(br.readLine());
            String str = reverse.get(search(num, 0, list.size()-1, list));
            sb.append(str).append("\n");
        }

        System.out.print(sb.toString().trim());

    }

    private static int search(int num, int start, int end, List<Integer> list) {
        if (start == end) {
            return list.get(start);
        }
        int midIdx = (start+end)/2;
        int mid = list.get(midIdx);
        if (num <= mid) {
            return search(num, start, midIdx,list);
        }else{
            return search(num, midIdx + 1, end, list);
        }
    }
}
