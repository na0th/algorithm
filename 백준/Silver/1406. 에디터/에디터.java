import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    /*
    커서는 문장의 맨 앞(맨 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳에 위치할 수 있다.
    L은 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    D는 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    B는 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
    A| -> |
    AB|C -> A|C    B와C사이에 커서가 있는데, 거기서 'B' 실행

    P $는 	$라는 문자를 커서 왼쪽에 추가함

    분류 : 구현?
    어떻게 풀이?
    중간에 자주 삽입, 삭제 되는 구조이니 ArrayList보다는 LinkedList가 적합

    L은 (커서가 맨 앞이면 무시됨) + 커서의 값을 -1한다
    D는 (커서가 맨 뒤면 무시됨) + 커서의 값을 +1한다
    B는 (커서가 맨 앞이면 무시됨) + 커서 왼쪽에 있는 문자를 삭제한다 -> 인덱스 값 삭제
    P '$'는 커서 왼쪽에 '$'라는 문자 추가 -> 인덱스에 추가

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(br.readLine());

        int commandCount = Integer.parseInt(br.readLine());
        int cursor = sb.length();
        for(int i=0; i<commandCount; i++){
            String[] parts = br.readLine().split(" ");
            switch (parts[0]){
                case "L" :
                    if (cursor==0) continue;
                    cursor -=1 ;
                    break;
                case "D" :
                    if(cursor==sb.length()) continue;
                    cursor+=1;
                    break;
                case "B" :
                    if (cursor==0) continue;
                    sb.deleteCharAt(cursor-1);
                    cursor--;
                    break;
                case "P" :
                    char c = parts[1].charAt(0);
                    sb.insert(cursor, c);
                    cursor++;
                    break;
            }
        }
        System.out.println(sb.toString().trim()); // 마지막에 공백 제거
         
    }
}
