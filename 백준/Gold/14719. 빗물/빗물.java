import java.io.*;
import java.util.*;

public class Main {
    /*
    빗물 고이는 총량 구하기
    알고리즘 분류 : 스택(어려움) + 투포인터(정렬 아님)
    어떻게 풀이?
    스택 어려움
    각 칸 별로 왼쪽벽(최고 높이), 오른쪽 벽(최고 높이) 중 작은 것과 나(해당 칸)의 차이만큼 빗물이 고임
    1. 갱신하면서 배열에 왼쪽부터 해당 칸까지 최대값 넣기, 오른쪽부터 해당칸까지 최대값 넣기

    4 4
    3 0 1 4
     */
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int height = Integer.parseInt(st.nextToken());
        int width = Integer.parseInt(st.nextToken());
        int[] arr = new int[width];
        int[] leftMaxArr = new int[width];
        int[] rightMaxArr = new int[width];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < width; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }
        leftMaxArr[0] = arr[0];
        rightMaxArr[width - 1] = arr[width - 1];
        for (int i = 1; i < width; i++) {
            leftMaxArr[i] = Math.max(arr[i], leftMaxArr[i - 1]);
        }
        for (int i = width - 2; i >= 0; i--) {
            rightMaxArr[i] = Math.max(arr[i], rightMaxArr[i + 1]);
        }
        int sum = 0;
        for (int i = 0; i < width; i++) {
            sum += Math.min(leftMaxArr[i], rightMaxArr[i]) - arr[i];
        }
        System.out.print(sum);

    }
}