import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    /*
    키 순서대로 번호를 부여
    키가 작으면 1번 크면 20번이고, 반 아이는 항상 20명 (키가 같은 경우는 없다)

    위치를 찾는 방법이다.
    1. 아무나 뽑아서 맨 앞에 세운다
    2. 자기 앞에 자기보다 키가 큰 학생이 없으면 거기에 선다
    3. 자기 앞에 키가 큰 학생이 있다면, 맨 앞에 서고, 모든 학생들은 1걸음 뒤로간다.

    분류 : 정렬?

    어떻게 풀이?
    1. for문 순회하면서, 해당 인덱스의 값보다 큰 값을 앞에서부터 찾는다.
    2. 앞에서 부터 큰 값 발견 시, answer +1 -> 뒤로 이동해야 하니까 
    
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int num = Integer.parseInt(br.readLine());

        for(int i=0; i<num; i++){
            int answer = 0;
            int[] parts = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for(int p=2; p<parts.length; p++){
                for(int q = 1; q < p; q++){
                    // 앞에서부터 인덱스 p까지 큰 애가 있다면?
                    if(parts[p]<parts[q]){
                        answer++;
                    }
                }
            }
            sb.append(parts[0]).append(" ").append(answer).append("\n");


        }
        System.out.print(sb.toString().trim());
    }
}
