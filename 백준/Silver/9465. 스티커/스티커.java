import java.io.*;
import java.util.*;

public class Main {
    /*
    스티커는  2행 n열로 배치되어 있다
    2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.
     */
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int stickerCnt = Integer.parseInt(br.readLine());
            int[][] dp = new int[2][stickerCnt];
            int[][] map = new int[2][stickerCnt];

            for(int row=0; row<2; row++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int col = 0; col < stickerCnt; col++) {
                    map[row][col] = Integer.parseInt(st.nextToken());
                }
            }
            // n이 1인 경우 예외처리
            dp[0][0] = map[0][0];
            dp[1][0] = map[1][0];
            if (stickerCnt == 1) {
                sb.append(Math.max(dp[0][0], dp[1][0])).append("\n");
                continue;
            }
            for (int c = 1; c < stickerCnt; c++) {
                for (int r = 0; r < 2; r++) {
                    if (c == 1) {
                        if (r == 0) {
                            dp[r][c] = map[r][c] + map[1][c-1];
                        }
                        else{
                            dp[r][c] = map[r][c] + map[0][c-1];
                        }
                    }else{
                        int num = Math.max(dp[0][c-2], dp[1][c-2]);
                        if (r == 0) {
                            dp[r][c] += Math.max(map[r][c] + dp[1][c-1], num+map[r][c]);
                        }else{
                            dp[r][c] += Math.max(map[r][c] + dp[0][c-1], num+map[r][c]);
                        }
                    }
                }
            }
            sb.append(Math.max(dp[0][stickerCnt - 1], dp[1][stickerCnt - 1])).append("\n");
        }
        System.out.print(sb.toString().trim());
    }
}