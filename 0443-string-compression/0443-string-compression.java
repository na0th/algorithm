import java.util.*;
class Solution {
    /**
    문자열을 압축
    1개는 숫자가 안 붙는다.

    알고리즘 분류 : 구현?
    어떻게 풀이?
    cur_char , cur_count 2개로 분리

    1) for문으로 chars를 돌면서 cur_char를 갱신
    2) cur_char랑 현재 보고 있는 값이랑 같다면 cur_count+1
    3) 다르다면? count가 1이면 문자만 추가, 1이 아니라면 숫자를 추가
        - 여기서 추가할 때 10넘으면 자리수까지 고려해서 추가해야함..
    4) 모두 다 돌았으면 마지막 cur_char,cur_count를 추가해줌

    */
    public int compress(char[] chars) {
        int write = 0;
        int count = 1;

        for (int read = 1; read <= chars.length; read++) {
            //처음하고 마지막은 제외
            if (read == chars.length || chars[read] != chars[read - 1]) {
                // 문자 기록
                chars[write++] = chars[read - 1];

                // count > 1 이면 숫자 기록
                if (count > 1) {
                    for (char c : String.valueOf(count).toCharArray()) {
                        chars[write++] = c;
                    }
                }

                count = 1;
            } else {
                count++;
            }
        }

    return write;
    }
}