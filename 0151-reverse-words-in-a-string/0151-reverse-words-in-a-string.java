import java.util.*;
class Solution {
    /**
    문장 = 단어 몇 개
    문장 순서를 뒤집으면서, 공백은 1칸만 있도록

    알고리즘 분류 : 문자열
    어떻게 풀이?
    공백을 기준으로 split
    List에 담는다.
    정렬을 역으로 or deque를 뒤에서 부터 뺀다

     */
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();

        List<String> reverseWords = Arrays.asList(words);
        Collections.reverse(reverseWords);

        for(String word : words){
            if(word==null || word.isEmpty()){
                continue;
            }
            sb.append(word);
            sb.append(" ");
            
        }
        String answer = sb.toString();
        return answer.stripTrailing();
    }
}