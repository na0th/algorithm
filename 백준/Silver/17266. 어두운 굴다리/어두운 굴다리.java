import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    /*
    모든 길 0~N을 밝히게 가로등을 설치하기.
    각 가로등은 높이만큼 주위를 비출 수 있다
    최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다.
    최소한의 예산이 들 높이를 구하자. 단 가로등은 모두 높이가 같아야 하고, 정수이다

    굴다리 길이 N
    가로등의 갯수 M
    가로등의 위치 EX) 2, 4

    분류 : 탐색
    N이 10만이고, 가로등 갯수도 최대 10만
    최악의 경우 10만*10만 이라 일반적인 탐색으로 불가능

    어떻게 풀이 ?
    1. 이분 탐색으로 범위의 중간 값이 가로등을 전부 비출 수 있으면, 높은 범위만 탐색
    2. 범위의 중간 값이 가로등을 전부 비출 수 없으면, 낮은 범위만 탐색
    3. 탐색 종료 조건은? 중간 값의 -1을 한 값은 가로등을 전부 비출 수 없다면, 중간 값이 최적값
    * */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] pos = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        System.out.print(search(pos, 0, n,n));
    }

    private static boolean makeRange(int[] pos, int h, int n) {
        int rangeRight = 0;
        for (int curPos : pos) {
            int L = Math.max(0, curPos - h);
            int R = Math.min(n, curPos + h);

            //중간의 범위 연결이 끊기면 false 리턴
            if (L > rangeRight) return false;

            rangeRight = Math.max(rangeRight, R);
            //
            if(rangeRight >= n) return true;

        }
        return rangeRight >= n;
    }

    private static int search(int[] pos, int start, int end,int n) {
        if (start == end) return start;
        int mid = (start + end) / 2;
        // if 가로등을 비출 수 있다면
        if (makeRange(pos, mid, n)) {
            return search(pos,start,mid,n);
        } // if 가로등을 비출 수 없다면
        else{
            return search(pos, mid + 1, end,n);
        }
    }
}
