import java.util.*;
class Solution {
    /**
    문자열 1, 2 번갈아가며 추가된다.

    알고리즘 분류 : 문자열
    어떻게 풀이? 
    문자열1, 문자열2의 크기를 구한다

    문자열1 > 문자열2
    : 
    문자열1과 문자열2를 번갈아더한다(문자열2 크기만큼), 나머지는 문자열1을 더한다.
    문자열2 > 문자열1
    :
    문자열1과 문자열2를 번갈아더하고, 크기 차이만큼 문자열2를 다 더한다
     */
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int maxLength = Math.max(word1.length(), word2.length());

        for (int i = 0; i < maxLength; i++) {
            if (i < word1.length()) {
                sb.append(word1.charAt(i));
            }
            if (i < word2.length()) {
                sb.append(word2.charAt(i));
            }
        }

        return sb.toString();
    }
}