import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    /*
        미니게임 (본인이 포함되어야 함)
        2인용 Y
        3인용 F
        4인용 O가 있다.

        신청자 N명과 게임의 종류 (Y,F,O)가 주어 졌을 때 최대 게임 횟수를 구하시오.
        분류 : 수학?
        어떻게 풀이 ?
        2인용 게임이면 N % (2-1)의 몫이 될 것
        3인용 게임이면 N % (3-1)의 몫이 될 것
        4인용 게임이면 N % (3-1)의 몫이 될 것
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int needPeopleCnt = 0;
        int answer = 0;

        Set<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(br.readLine());
        }
        if (parts[1].equals("Y")) {
            needPeopleCnt = 1;
        } else if (parts[1].equals("F")) {
            needPeopleCnt = 2;
        } else if (parts[1].equals("O")) {
            needPeopleCnt = 3;
        }
        answer = set.size() / needPeopleCnt;
        System.out.print(answer);
    }
}
