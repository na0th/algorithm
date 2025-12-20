import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    N*N 정사각형이 주어지고
    '*'는 쿠키런의 몸 표시이다.
    쿠키는 머리, 심장, 허리, 좌우 팔 다리로 이루어져 있고,
    머리는 심장 바로 위 1칸
    왼쪽 팔은 심장 바로 왼쪽, 오른쪽 팔은 심장 바로 오른쪽
    허리는 심장 바래 아래 쪽, 왼쪽 다리는 허리 왼쪽 아래, 오른쪽 다리는 허리 오른쪽 아래 붙어있다.

    분류 : 구현
    어떻게 풀이 ?
    1. 포인트들을 잡는다.
    예를 들어, 머리는 2중 FOR돌면서 가장 처음 몸인 곳 -> '*'
    심장은 머리의 1칸 아래

    출력 : 왼팔,오른팔,허리,왼다리,오른다리
    허리 = 머리를 기준으로 '-'가 나올 때까지 아래로 이동
    팔 = 머리 1칸 아래에서 가로 길이
    왼팔 = 허리 끝 1칸 왼쪽 아래 기준으로 세로 길이
    오른팔 = 허리 끝 1칸 오른쪽 아래 기준으로 세로 길이

    구해야 할 것, 머리, 심장, 허리 끝
    * */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int n = Integer.parseInt(br.readLine());
        char[][] table = new char[n][n];

        for (int i = 0; i < n; i++) {
            String parts = br.readLine();
            for (int j = 0; j < n; j++) {
                table[i][j] = parts.charAt(j);
            }
        }
        String headPoint = findHead(table, n);
        String heartPoint = findHeart(headPoint);
        String waistEndPoint = findWaistEnd(table, n, headPoint);
        String[] parts = heartPoint.split(",");

        int waistLength = calWaistLength(table, n, headPoint);
        int leftArmLength = calLeftArmLength(table, n, heartPoint);
        int rightArmLength = calRightArmLength(table, n, heartPoint);
        int leftLegLength = calLeftLegLength(table, n, waistEndPoint);
        int rightLegLength = calRightLegLength(table, n, waistEndPoint);

        sb.append(Integer.parseInt(parts[0]) + 1)
                .append(" ")
                .append(Integer.parseInt(parts[1]) + 1)
                .append("\n");

        sb.append(leftArmLength).append(" ")
                .append(rightArmLength).append(" ")
                .append(waistLength).append(" ")
                .append(leftLegLength).append(" ")
                .append(rightLegLength);


        System.out.print(sb.toString().trim());

    }

    public static String findHead(char[][] table, int n) {
        //2중 for문에서 첫번째로 등장하는 '*'이 머리이다.
        String headPoint = "";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (table[i][j] == '*') {
                    headPoint = i + "," + j;
                    return headPoint;
                }
            }

        }
        return headPoint;
    }

    public static String findHeart(String headPoint) {
        //심장은 머리 1칸 아래 칸
        StringBuffer sb = new StringBuffer();
        String[] parts = headPoint.split(",");
        String heartPoint = "";

        int i = Integer.parseInt(parts[0]);
        int j = Integer.parseInt(parts[1]);

        heartPoint = String.valueOf(sb.append(i+1).append(",").append(j));
        return heartPoint;
    }

    public static String findWaistEnd(char[][] table, int n, String headPoint) {
        StringBuffer sb = new StringBuffer();
        String[] parts = headPoint.split(",");
        String waistEndPoint = "";

        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);

        for (int i = w; i < n; i++) {
            if (table[i][h] != '*') {
                waistEndPoint = String.valueOf(sb.append(i-1).append(",").append(h));
                break;
            }
        }
        return waistEndPoint;
    }

    public static int calWaistLength(char[][] table, int n, String headPoint) {
        String[] parts = headPoint.split(",");

        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);

        int length = 0;
        for (int i = w; i < n; i++) {
            if (table[i][h] == '*') {
                length++;
            }
        }
        return length-2;
    }

    public static int calLeftArmLength(char[][] table, int n, String heartPoint) {
        // 심장 있는 포인트 기준, 왼쪽 팔 길이
        String[] parts = heartPoint.split(",");
        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);
        int leftarmLength = 0;
        for (int j = 0; j < h; j++) {
            if (table[w][j] == '*') {
                leftarmLength++;
            }
        }
        return leftarmLength;
    }
    public static int calRightArmLength(char[][] table, int n, String heartPoint) {
        // 심장 있는 포인트 기준, 오른쪽 팔 길이
        String[] parts = heartPoint.split(",");
        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);
        int rightarmLength = 0;
        for (int j = h+1; j < n; j++) {
            if (table[w][j] == '*') {
                rightarmLength++;
            }
        }
        return rightarmLength;
    }
    public static int calLeftLegLength(char[][] table, int n, String waistEndPoint) {
        String[] parts = waistEndPoint.split(",");
        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);

        int leftLegLength = 0;
        for (int i = w+1; i < n; i++) {
            if (table[i][h-1] == '*') {
                leftLegLength++;
            }
        }
        return leftLegLength;
    }
    public static int calRightLegLength(char[][] table, int n, String waistEndPoint) {
        String[] parts = waistEndPoint.split(",");
        int w = Integer.parseInt(parts[0]);
        int h = Integer.parseInt(parts[1]);

        int rightLegLength = 0;
        for (int i = w+1; i < n; i++) {
            if (table[i][h+1] == '*') {
                rightLegLength++;
            }
        }
        return rightLegLength;
    }

}
