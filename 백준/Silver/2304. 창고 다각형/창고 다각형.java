import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    N개의 막대 기둥이 존재
    ```
    지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
    지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
    지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
    지붕의 가장자리는 땅에 닿아야 한다.
    비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
    ```
    를 만족시키는 가장 작은 창고 다각형의 면적 구하기

    분류 : 부분 수열? 구현?

    어떻게 풀이 ?
    오목한 부분 없이 평평하게 올라가고, 내려가야 한다.
    4 6 3 10 4 6 8 이면 4 6 10 8이 나오는데
    이거는 가장 큰 10을 기준으로 왼쪽으로 간다면, 내려갔다가 올라오는 부분이 없어야한다. 오른쪽도 마찬가지
    즉, 내려가기만 해야 한다.
    1. 배열의 MAX값을 찾아서 그 MAX가 위치한 인덱스 전까지 왼쪽에서 오르는 수열, 오른쪽에서 오르는 수열을 찾는다.
    2. 그걸 합치고 면적을 구한다.

    1. 왼쪽에서 max값을 찾기 전까지 면적을 더한다. (오르는 수열)
    2. 오른쪽에서부터 왼쪽으로 max를 찾기 전까지 면적을 더한다. (오르는 수열)

    x값을 기준으로 정렬해서 처음부터 끝까지 for문 돌면서 면적 추가하기.
    7
    2 4
    11 4
    15 8
    4 6
    5 3
    8 10
    13 6
    * */
    static int[] arr;
    static int[] leftMax;
    static int[] rightMax;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[1001];
        leftMax = new int[1001];
        rightMax = new int[1001];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            arr[x] = height;

        }
//        System.out.println(Arrays.toString(arr));
        leftMax(1001);
//        System.out.println(Arrays.toString(leftMax));
        rightMax(1001);
//        System.out.print(Arrays.toString(rightMax));

        int total = 0;
        for (int i = 0; i < 1001; i++) {
            total += Math.min(leftMax[i], rightMax[i]);
        }
        System.out.print(total);

    }

    private static void rightMax(int n) {
        int rightMaxNum = arr[n - 1];
        rightMax[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (rightMaxNum < arr[i]) {
                rightMaxNum = arr[i];
            }
            rightMax[i] = rightMaxNum;
        }
    }

    private static void leftMax(int n) {
        int leftMaxNum = arr[0];
        leftMax[0] = arr[0];
        for (int i = 0; i < n; i++) {
            if (leftMaxNum < arr[i]) {
                leftMaxNum = arr[i];
            }
            leftMax[i] = leftMaxNum;
        }
    }


}
