import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환을 최소로 하는 프로그램을 작성
    이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있다.
    예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

    알고리즘 분류 : 교환을 최소로.. 그리디? (X)
    어떻게 풀이?
    a가 연속이면 되니까, a의 갯수를 세서 앞에서부터 그만큼 확인했을 떄, b의 갯수가 최소인 상황이면 된다.


    엣지 : 마지막에 문자





    * */
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        String word = br.readLine();
        count = countA(word);
        String s = word + word;
        int min = Integer.MAX_VALUE;
        //aaabb면 3번보면된다.
        for (int i = 0; i < word.length(); i++) {
            int countB = 0;
            for (int k = 0; k < count; k++) {
                if (s.charAt(i + k) == 'b') {
                    countB++;
                }
            }
            min = Math.min(min, countB);
        }
        System.out.print(min);
    }


    public static int countA(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == 'a') {count++;}
        }
        return count;
    }
}
