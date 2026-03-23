import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /*
    볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다.
    규칙 1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다
    규칙 2. 옮길 수 있는 볼의 색깔은 한 가지이다. 한번 선택하면 그 색깔 볼만 옮길 수 있다.

    알고리즘 분류 : 스택?? DP?
    그래야 움직이는 횟수가 제일 적다. 한번에 건너뛰는 길이가 제일 크기때문
    어떻게 풀이?
    근데 왼쪽으로 이동시키는 것, 오른쪽으로 이동시키는 것 고려해야 할 것 같다.
    1. R,B 둘다 오른쪽 R,B볼 부터 가장 오른쪽으로 넘긴다, 왼쪽으로 넘긴다
    각각 2가지씩 방안이 있어서 4가지 방법에서 최소 구하자


    BRBRB -> BBBRR = BRBB|R  BBB| RR
    * BBR RBB RB RB -> BBR| RBB| RB|BR -> BBRRBBBB|RR -> BBRBBBB|RRR -> BBBBBB|RRRR
    */
    static int size;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        size = Integer.parseInt(br.readLine());
        String balls = br.readLine();
        char[] ball = balls.toCharArray();
        int leftR = 0;
        int rightR = 0;
        int leftB = 0;
        int rightB = 0;
        int countRed = countRed(ball);
        int countBlue = countBlue(ball);
        leftR = countRed - countFirst(ball, 'R');
        rightR = countRed - countReverse(ball, 'R');
        leftB = countBlue - countFirst(ball, 'B');
        rightB = countBlue - countReverse(ball, 'B');
        int min = Math.min(Math.min(leftR, leftB), Math.min(rightR, rightB));
        System.out.print(min);
    }

    public static int countRed(char[] ball) {
        int redCount = 0;
        for (char c : ball) {
            if (c == 'R') {
                redCount++;
            }
        }
        return redCount;
    }
    public static int countBlue(char[] ball) {
        return size-countRed(ball);
    }
    public static int countFirst(char[] ball, char c) {
        int count = 0;
        for (int i = 0; i < ball.length; i++) {
            if (ball[i] == c) {
                count++;
            }else{
                break;
            }
        }
        return count;
    }
    public static int countReverse(char[] ball, char c) {
        int count = 0;
        for (int i = ball.length - 1; i>0; i--) {
            if (ball[i] == c) {
                count++;
            }else{
                break;
            }
        }
        return count;
    }

}
