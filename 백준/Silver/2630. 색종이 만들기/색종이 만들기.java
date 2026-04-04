import java.io.*;
import java.util.*;

public class Main {
    /*
    정사각형 모두 같은 색으로 칠해져있지 않으면 N/2로 4등분함
    더이상 자를 수 없거나, 모두 파란색일 때까지 진행했을 떄, 최종 파란색 색종이, 하얀색 색종이의 갯수

    알고리즘 분류 : 분할정복
    어떻게 풀이?
    start~end는 4개의 범위로 나눌 수 있다.
    0~n/2, 0~n/2
    0~n/2, n/2~n
    n/2~n, 0~n/2
    n/2~n, n/2~n

    end-start의 차이가 1인 경우 break
    모두 1이면.. return 1
    다 1이 아니라면, 다 더해 return 값
     */
    static int[][] map;
    static int n;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        sb.append(divideConquer(0,0, n, 0, n)).append("\n");
        sb.append(divideConquer(1,0, n, 0, n));
        System.out.print(sb.toString());


    }
    public static int divideConquer(int color,int startX, int endX, int startY, int endY) {
        boolean check = true;
        int firstColor = map[startX][startY];
        
        for (int i = startX; i < endX; i++) {
            for (int j = startY; j < endY; j++) {
                if (map[i][j] != firstColor) {
                    check = false;
                    break;
                }
            }
        }
        int midX = (startX + endX) / 2;
        int midY = (startY + endY) / 2;
        if (!check) {
            int sum = 0;
            sum += divideConquer(color, startX, midX, startY, midY);
            sum += divideConquer(color, midX, endX, startY, midY);
            sum += divideConquer(color, startX, midX, midY, endY);
            sum += divideConquer(color, midX, endX, midY, endY);
            return sum;
        }else{
            return firstColor == color ? 1 : 0;
        }
    }
}