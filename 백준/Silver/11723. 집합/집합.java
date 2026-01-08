import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    /*
    비어있는 공집합 S가 주어졌을 때
    add : S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove : S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check : S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle :  S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all : S를 {1, 2, ..., 20} 으로 바꾼다.
    empty : s를 공집합으로 바꾼다.

    분류 : 구현

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            String command = parts[0];
            if (command.equals("all")) {
                for (int k = 1; k <= 20; k++) {
                    set.add(k);
                }
                continue;
            }
            if (command.equals("empty")) {
                set.clear();
                continue;
            }

            int num = Integer.parseInt(parts[1]);
            switch (command) {
                case "add":
                    set.add(num);
                    break;
                case "remove":
                    set.remove(num);
                    break;
                case "check":
                    if (set.contains(num)) sb.append("1").append("\n");
                    else sb.append("0").append("\n");
                    break;
                case "toggle":
                    if (set.contains(num)) set.remove(num);
                    else set.add(num);
                    break;
            }
        }
        System.out.print(sb.toString().trim());

    }

}
