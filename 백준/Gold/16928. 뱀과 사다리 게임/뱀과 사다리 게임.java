import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class Main {
    /*
    1~6이 나오는 주사위, 주사위 눈의 수만큼 이동한다.
    10*10 100칸의 판이 있고,
    더 높은 수로 이동하는 사다리, 더 아래 수로 이동하는 뱀의 몇몇 칸에 존재한다.
    이를 이용해서 주사위를 최소로 굴려서,가장 빨리 100번쨰 칸에 도달하는 횟수 구하기

    분류 : BFS
    어떻게 풀이?
    왼쪽은 현재 칸, 오른쪽은 주사위를 굴린 횟수
    1. 각 칸에 도달하면, 100칸을 도달했거나 넘어갔는지 확인한다.
    2. 그 칸에 사다리, 뱀이 있는지 확인하고 있다면 안내된 곳으로 이동한다.
    3. 칸에 사다리나 뱀이 없다면, 주사위를 굴린 횟수는 1회 증가하고, 현재 칸에서 (1,2,3,4,5,6)을 더하는 6가지의 경우의 수가 있다.
    4. 큐에 6가지 경우를 전부 넣는다.
    => (F(N),1) -> (F(N+1),1+1),(F(N+2),1+1),(F(N+3),1+1),(F(N+4),1+1),(F(N+5),1+1),(F(N+6),1+1)

    + 이렇게 하니 메모리 초과됨. visited를 통해서 재방문 안하도록 하기.
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]) + Integer.parseInt(parts[1]);

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String[] values = br.readLine().split(" ");
            map.put(Integer.parseInt(values[0]), Integer.parseInt(values[1]));
        }

        Deque<int[]> dq = new ArrayDeque<>();
        boolean[] visited = new boolean[150];

        // 첫 번째 원소는 현재 위치(cur_pos), 두 번째 원소는 주사위 던진 횟수(dice_cnt)
        dq.addFirst(new int[]{1, 0});

        while (!dq.isEmpty()) {
            int[] pick = dq.removeLast();
            int cur_pos = pick[0];
            int dice_cnt = pick[1];

            // 100칸 or  넘어가면 종료하고 리턴
            if (cur_pos == 100) {
                System.out.print(dice_cnt);
                break;
            }
            for (int i = 1; i <= 6; i++) {
                //100 이상은 넣지 않는다.
                int next = cur_pos + i;

                if (next > 100) {
                    continue;
                }
                if (map.containsKey(next)) {
                    next = map.get(next);
                }
                if (!visited[next]) {
                    visited[next] = true;
                    dq.addFirst(new int[]{next, dice_cnt + 1});
                }
            }
        }
    }
}
