import java.io.*;
import java.util.*;

public class Main {
    /*
    2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다
    알고리즘 분류 : 재귀, 분할정복
    어떻게 풀이?
    문제를 4등분하여 범위를 나눈다.
    (n/2, n/2, count)
    (n/2, n, count + n/4)
    (n, n/2, count + (n/4)*2)
    (n, n, count+ (n/4)*3)
    재귀 종료 조건 : 길이가 1인 경우 map[row][col]에 count를 넣는다.
     */
    static int row;
    static int col;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = pow(2, Integer.parseInt(st.nextToken()));
        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());

        divideConquer(0, 0, n, 0);


    }
    public static void divideConquer(int r, int c, int size, int count) {
        //종료조건
        int half = size / 2;
        int area = half * half;
        if (size == 1) {
            System.out.print(count);
            return;
        }
        if (row < r + half && col < c + half) {
            divideConquer(r, c, half, count);
        }
        // 2사분면
        else if (row < r + half && col >= c + half) {
            divideConquer(r, c + half, half, count + area);
        }
        // 3사분면
        else if (row >= r + half && col < c + half) {
            divideConquer(r + half, c, half, count + area * 2);
        }
        // 4사분면
        else {
            divideConquer(r + half, c + half, half, count + area * 3);
        }
    }
    public static Integer pow(int base, int exp) {
        int result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }
    //        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                System.out.print(map[i][j] + " ");
//            }
//            System.out.println();
//        }
}