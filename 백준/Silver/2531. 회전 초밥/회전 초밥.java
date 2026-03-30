import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    /*
        1. 손님이 마음대로 초밥을 먹은 만큼 계산, k개의 접시를 연속해서 먹으면 할인됨
        2. 쿠폰에 적혀있는 초밥을 무료로 줌

        알고리즘 분류 : 슬라이딩윈도우
        어떻게 풀이?
        1. k개씩 끊어서 초밥의 종류를 센다.
        2. 쿠폰에 있는 초밥 종류가 없었다면 cnt+1, 아니면 0 해서  최대값 구하기

    */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int d = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);
        int coupon = Integer.parseInt(parts[3]);

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }
        //원형 만들기 위함
        for (int i = 0; i < n; i++) {
            list.add(list.get(i));
        }

        Map<Integer, Integer> map  = new HashMap<>();
        //초기값 세팅
        for (int j = 0; j < k; j++) {
            map.put(list.get(j), map.getOrDefault(list.get(j), 0) +1 );
        }
        int maxCnt = 0;
        int setCnt = 0;
        for (int num : map.values()) {
            if (num != 0) setCnt++;
        }
        if (!map.containsKey(coupon)) {
            setCnt++;
        }
        maxCnt = Math.max(maxCnt, setCnt);

        for (int i = 1; i <2*n-k+1 ; i++) {
            map.put(list.get(i-1), map.get(list.get(i-1)) - 1);
            map.put(list.get(i+k-1), map.getOrDefault(list.get(i+k-1), 0) +1 );
            int cnt = 0;
            for (int num : map.values()) {
                if (num != 0) cnt++;
            }
            if (map.getOrDefault(coupon, 0) == 0) {
                cnt++;
            }

            maxCnt = Math.max(maxCnt, cnt);
        }
        System.out.print(maxCnt);

    }
}
