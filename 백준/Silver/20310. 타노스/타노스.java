import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    0과 1로 이루어진 문자열 S가 있다.
    문자열 S는 짝수 개의 0, 짝수 개의 1을 포함
    타노스는 문자열 S에서 절반의 0, 절반의 1을 제거한다.
    S로 가능한 사전순으로 가장 빠른 문자열 찾기

    분류 : 그리디, 구현
    어떻게 풀이?
    1. 사전순으로 가장 빠른 문자열은 가장 작은 수
    2. 가장 작은 수를 만들기 위해서는 0은 뒤에서부터 빼고, 1은 앞에서 부터 빼면 되지 않을까?

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder sb = new StringBuilder(s);

        int zeroCount = 0, oneCount = 0;
        // 0과 1의 개수 세기
        for (char c : s.toCharArray()) {
            if (c == '1') {
                oneCount++;
            }else{
                zeroCount++;
            }
        }
        // 1은 앞에서부터 oneCount/2개 건너 뛴 다음 제거한다.
        // 0은 뒤에서부터 zeroCount/2개 만큼 제거한다.
        int checkOne = 0, checkZero = 0;
        for (int i = sb.length() - 1; i >= 0; i--) {
            if (sb.charAt(i) == '1') {
                if (checkOne >= (oneCount / 2)) {
                    sb.deleteCharAt(i);
                }
                checkOne++ ;
            }else{
                if (checkZero < (zeroCount / 2)) {
                    sb.deleteCharAt(i);
                }
                checkZero++ ;
            }

        }
        System.out.print(sb.toString().trim());
    }
}
