import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    한 팀은 여섯 명의 선수로 구성되며, 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산한다.
    점수는 자격을 갖춘 팀의 주자들에게만 주어지며 결승점을 통과한 순서대로 점수를 받는다
    가장 낮은 점수를 얻는 팀이 우승을 하게 된다. 여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외된다.
    동점인 경우 다섯 번째 주자가 더 빨리 들어온 팀이 우승

    첫 번째 줄에 테스트 케이스의 수를 나타내는 정수 T
    두 번째 줄부터는 두 줄에 하나의 테스트 케이스에 해당하는 데이터가 주어진다

    분류 : 구현
    어떻게 풀이?
    1. 전부 순회하면서 각 팀의 선수 숫자를 카운팅한다
    2. 다시 각 선수들을 돌면서 팀의 숫자가 6명 이상인지 확인하여 맞다면 점수를 부여한다.
    3. 점수를 합산하고 동점이라면 다섯번째 주자를 확인한다.


     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            Map<Integer, List<Integer>> map = new HashMap<>();
            Map<Integer, Integer> mapCount = new HashMap<>();

            int[] nums = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            // 팀원 카운트
            for (int k = 0; k < n; k++) {
                //count 세기
                mapCount.put(nums[k], mapCount.getOrDefault(nums[k], 0) + 1);
            }

            int grade = 1;
            for (int num : nums) {
                //6명이 있는 팀에 대해서만 등수 매기기
                if (mapCount.getOrDefault(num,0) == 6) {
                    if (!map.containsKey(num)) {
                        map.put(num, new ArrayList<>());
                    }
                    // 해당 팀끼리 묶기
                    map.get(num).add(grade++);
                }
            }

            //6명 이하 팀은 삭제
            map.entrySet().removeIf(e -> e.getValue().size() < 6);

            // map 내부 리스트를 정렬해서 상위 4개의 점수만 합산
            List<Map.Entry<Integer, List<Integer>>> entries = new ArrayList<>(map.entrySet());
            entries.sort((a, b) -> {
                List<Integer> A = a.getValue();
                List<Integer> B = b.getValue();

                int sumA = A.get(0) + A.get(1) + A.get(2) + A.get(3);
                int sumB = B.get(0) + B.get(1) + B.get(2) + B.get(3);

                // 오름차순: 상위4합이 작은 게 우선
                int cmp = Integer.compare(sumA, sumB);
                if (cmp != 0) return cmp;

                int fifthA = A.get(4);
                int fifthB = B.get(4);

                // 오름차순: 5번째도 작은 게 우선
                return Integer.compare(fifthA, fifthB);
            });
            sb.append(entries.get(0).getKey()).append("\n");
        }
        System.out.print(sb.toString().trim());

    }
}
