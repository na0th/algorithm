import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    블로그에 글을 쓰기 위해 메모장에 키워드를 적는다
    지금까지 메모장에 써진 키워드는 모두 다르며, 총 N개
    새로운 글의 키워드는 최대 10개
    메모장에 있던 키워드는 글을 쓴 이후에는 지워진다.
    블로그에 글을 쓰고나서 메모장에 있는 키워드의 개수를 구하기

    분류 : 해시? 맵?


    1. 1 ~ N+1 줄까지 메모장에 있는 개의 단어와 N+2 ~ N+M+1 줄까지 M개의 글에 있는 모든 단어를 더한 집합을 비교한다.
    2. 메모장 단어의 갯수는 N개이다. 메모장 단어부터 순회하면서 해당 단어가
    모든 글 단어 집합에 해당 단어가 있는지 확인하고, 있다면 -1한다.
    3. 글을 쓴 이후에는 메모장 단어에서 삭제되어야 한다.


    글에 중복된 키워드가 나오면 어떻게 해야하는지?
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] parts = br.readLine().split(" ");

        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        int answer = n;
        Set<String> memoWords = new HashSet<String>();

        //메모장에 단어들을 추가
        for (int i = 0; i < n; i++) {
            memoWords.add(br.readLine());
        }
        //글의 단어가 메모장에 있으면 삭제하고 answer-1;
        for (int i = 0; i < m; i++) {
            String[] words = br.readLine().split(",");
            for (String word : words) {
                if (memoWords.remove(word)) {
                    answer--;
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.print(sb.toString().trim());
    }
}
