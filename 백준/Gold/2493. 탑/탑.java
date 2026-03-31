import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /**/
    public static class Point{
        int num, index;
        Point(int num, int index) {
            this.num = num;
            this.index = index;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n = Integer.parseInt(br.readLine());
        String[] parts = br.readLine().split(" ");
        int[] nums = new int[parts.length];

        for (int i = 0; i < parts.length; i++) {
            nums[i] = Integer.parseInt(parts[i]);

        }
        ArrayDeque<Point> st = new ArrayDeque<>();
        int[] answer = new int[parts.length];
        for (int i = n-1; i >= 0; i--) {
            //둘이 비교
            if (i == n - 1) {
                st.addLast(new Point(nums[i], i + 1));
                continue;
            }
            while (!st.isEmpty() && st.peekLast().num <= nums[i]) {
                Point pop = st.removeLast();
                answer[pop.index-1] = i+1;
            }
            st.addLast(new Point(nums[i], i+1));
        }
        for (int i : answer) {
            sb.append(i).append(" ");
        }
        System.out.print(sb.toString().trim());
    }
}
