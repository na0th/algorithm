import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    /*
    shift / shift -> show sug로 자동완성 끄고 키기

    옵션의 단축키 지정하기
    1. 왼쪽 단어부터 첫글자가 단축키인지 확인, 아니라면 단축키로 설정
    2. 모든 단어 첫글자가 단축키라면, 왼쪽부터 알파벳을 보며 단축키로 지정안된 것이 나오면 단축키로 지정
    3. 옵션의 모든 단어의 알파벳이 단축키라면 그냥 둔다.

    알고리즘 분류 : 구현
    어떻게 풀이?
    1. 단어마다 첫글자 단축키 확인 (Set에 있는지)
    2. 왼쪽부터 모든 알파벳 확인 -> 모든 단어의 알파벳이 단축키라면 그냥 둔다.
    3. 단축키로 지정된 알파벳에 [ ] 추가
    * */
    static Set<Character> set = new HashSet<>();
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String line = br.readLine();
            int shortCutIndex = findShortcutIndex(line);
            if (shortCutIndex != -1) {
                sb.append(line.substring(0, shortCutIndex)).append("[").append(line.charAt(shortCutIndex)).append("]")
                  .append(line.substring(shortCutIndex+1,line.length()));
            }
            else{sb.append(line);}
            sb.append("\n");

        }
        System.out.print(sb.toString().trim());

    }
    public static int findShortcutIndex(String line){
        //맨처음 알파벳만 체크
        if (!set.contains(Character.toLowerCase(line.charAt(0)))) {
            set.add(Character.toLowerCase(line.charAt(0)));
            return 0;
        }
        //각 단어의 맨처음 체크
        for (int i=1; i<line.length(); i++) {
            if (line.charAt(i-1)==' ' && line.charAt(i) != ' ') {
                if (!set.contains(Character.toLowerCase(line.charAt(i)))) {
                    set.add(Character.toLowerCase(line.charAt(i)));
                    //단축키를 지정한 표시 [part.charAt[0]] <<
                    return i;
                }
            }
        }

        //모든 단어의 알파벳 체크
        for (int i = 0; i < line.length(); i++) {
            if (!set.contains(Character.toLowerCase(line.charAt(i))) && line.charAt(i) != ' ') {
                set.add(Character.toLowerCase(line.charAt(i)));
                return i;
            }
        }

        return -1;
    }

}
