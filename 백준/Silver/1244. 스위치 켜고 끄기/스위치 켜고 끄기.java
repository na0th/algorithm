import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    /*
    남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
    여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
    그 구간에 속한 스위치의 상태를 모두 바꾼다. 구간에 속한 스위치 개수는 항상 홀수가 된다.

    첫 째줄에는 스위치 개수가 주어진다.(100이하의 양의 정수)
    둘 째줄에는 각 스위치의 상태가 주어진다. (켜져있으면 1, 꺼져있으면 0)
    셋 째줄에는 학생수가 주어진다. (100이하의 양의 정수)
    넷 째줄부터 마지막 줄까지는 학생의 성별, 학생이 받은 수

    분류 : 구현

    어떻게 풀이?
    1. 남학생은 받은 수의 배수를 전부 스위치 상태를 바꿈
    2. 여학생은 자기가 받은 수를 중심으로 left, right가 같은지 체크해서 한칸씩 넓혀나감


    * */
    static int[] nums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        nums = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            int[] line = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            if (line[0] == 1) {
                man(line);
            } else if (line[0] == 2) {
                girl(line);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            sb.append(nums[i]).append(' ');
            if ((i + 1) % 20 == 0) sb.append('\n');
        }
        System.out.print(sb.toString().trim());
    }

    private static void man(int[] line) {
        int k = line[1];
        for (int j = k; j <= nums.length; j += k) {
            nums[j-1] = flip(nums[j-1]);
        }
    }

    private static void girl(int[] line) {
        int left = line[1]-1;
        int right = line[1]-1;
        //처음 값 뒤집기
        nums[line[1]-1] = flip(nums[line[1]-1]);

        while (left-1 >=0 && right +1 <nums.length && nums[left-1]==nums[right+1]) {
            left--;
            right++;
            nums[left] = flip(nums[left]);
            nums[right] = flip(nums[right]);
        }
    }

    private static int flip(int num) {
        if (num == 1) {
            return 0;
        }else {
            return 1;
        }
    }
}
