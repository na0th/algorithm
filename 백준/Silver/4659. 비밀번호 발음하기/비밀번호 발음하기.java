import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Main {
    /*
    패스워드 만들기. 3가지 규칙을 지켜야함
    1. 모음(a,e,i,o,u)를 최소 하나 반드시 포함
    2. 모음이 3개 연속, 자음이 3개 연속 오면 안된다.
    3. 같은 글자가 연속 2번 오면 안되나, ee와 oo는 허용한다.
    예외처리 ee, oo
    분류 : 구현
    어떻게 풀이 ?

    * */
    public static boolean rule1(String string) {
        List<Character> list = List.of('a', 'e', 'i', 'o', 'u');
        for (char c : string.toCharArray()) {
            if (list.contains(c)) {
                return true;
            }
        }
        return false;
    }
    public static boolean rule2(String string) {
        // 길이가 3보다 작으면 연속 불가능하니 true
        if (string.length() < 3) {
            return true;
        }
        List<Character> list = List.of('a', 'e', 'i', 'o', 'u');
        for (int i = 0; i < string.length() - 2; i++) {
            if(list.contains(string.charAt(i)) &&  list.contains(string.charAt(i+1)) && list.contains(string.charAt(i+2))){
                return false;
            } else if (!list.contains(string.charAt(i)) && !list.contains(string.charAt(i + 1)) && !list.contains(string.charAt(i + 2))) {
                return false;
            }
        }
        return true;
    }
    public static boolean rule3(String string) {
        //예외 처리 -> 같은 글자가 ee와 oo는 같은 글자 연속으로 나와도 된다.
        for (int i = 0; i < string.length() - 1; i++) {
            if (string.charAt(i) == string.charAt(i + 1)) {
                return string.charAt(i) == 'e' || string.charAt(i) == 'o';
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        String string;

        while ((string = br.readLine()) != null) {
            if (string.equals("end")) break;
            if (rule1(string) && rule2(string) && rule3(string)) {
                sb.append("<").append(string).append(">").append(" is acceptable.").append("\n");
            }else{
                sb.append("<").append(string).append(">").append(" is not acceptable.").append("\n");
            }
        }
        System.out.print(sb.toString().trim());


    }
}
