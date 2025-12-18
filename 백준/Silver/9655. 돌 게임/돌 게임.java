import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    /*
    돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 승리
    두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하기. 게임은 상근이부터 시작.

    분류 : 수학, DP
    어떻게 풀이 ?
    자기 걸 가져간 다음 상대에게 넘긴다. -> 리버스
    1개만 남았을 때는 누가 승리하는가?
    F(0) = 패배   = 0
    F(1) = 리버스 F(1-1) =  리버스 F(0) = 승리 = 1
    2개만 남았을 때는 누가 승리하는가?
    F(2) = 리버스 F(2-1) = 리버스 F(1) = 패배 = 0
    F(3) = 리버스 F(3-3) = 승리 = 1
    F(4) = 리버스 F(4-1) OR 리버스 F(4-3) 중 승리가 가능하면 승리 MAX(리버스(F(3), 리버스(F(1))
    F(5) = 리버스 F(5-1) OR 리버스 F(5-3) 중 승리가 가능하면 승리
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n =  Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        dp[0]=0;
        if (n >= 1) dp[1] = 1;
        if (n >= 2) dp[2] = 0;
        for(int i=3; i<n+1; i++){
            dp[i]= Math.max(reverse(dp[i-1]),reverse(dp[i-3]));
        }
        switch(dp[n]) {
            case 0 :
                System.out.print("CY");
                break;
            case 1 :
                System.out.print("SK");
        }
    }
    public static int reverse(int num){
        if (num == 0){return 1;}
        else return 0;
    }
}
