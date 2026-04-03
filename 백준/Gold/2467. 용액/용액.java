import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    /*
    산성 용액(양수)과 알칼리 용액(음수)를 섞어 0에 가장 가까운 용액을 만든다.
    알고리즘 분류 : 투포인터
    어떻게 풀이?
    기준을 정해야 하기 때문에 수를 정렬한다.
    Left 포인터, Right 포인터를 맨 왼쪽, 오른쪽에 위치한다
    각 포인터에 위치한 값의 합이 0보다 큰 경우, 오른쪽 포인터를 왼쪽으로 1칸 당긴다. (오른쪽에는 큰 수가 위치햇으니 더 작게 만든다)
    각 포인터에 위치한 값의 합이 0보다 작은 경우, 왼쪽 포인터를 오른쪽으로 1칸 당긴다.(왼쪽에는 작은 수가 위치했으니 더 크게 만든다)
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] parts = br.readLine().split(" ");
        List<Integer> nums = new ArrayList<>();
        for (String s : parts) {
            nums.add(Integer.parseInt(s));
        }
        //오름차순 정렬
        Collections.sort(nums);
        int left = 0;
        int right = n-1;
        int[] answer = new int[2];

        int totalNearByZero = Integer.MAX_VALUE;
        while (left < right) {
            int leftNum = nums.get(left);
            int leftRight = nums.get(right);
            int sum = leftNum + leftRight;

            if(Math.abs(totalNearByZero) > Math.abs(leftNum+leftRight)){
                totalNearByZero = sum;
                answer[0] = leftNum;
                answer[1] = leftRight;
            }
            if(sum > 0){right--;}
            else {left++;}

        }
        System.out.print(answer[0] + " " + answer[1]);
    }
}
