import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구하기
    1 4 2 5 1 은 2일동안 7명(2,5)이 최대
    1 1 1 1 1 5 1은 5일동안 9명(1,1,1,1,5), (1,1,1,5,1)

    분류 : 완전탐색?
    어떻게 풀이?
    1. X일씩 끊어서 방문자수를 구한다. 5일이면 1,2 | 2,3 | 3,4 | 4,5
    2. (방문자수, COUNT)꼴로 저장한다
    3. 최대 방문자 수를 찾아서 방문자수와 COUNT를 출력한다
    + 방문자수가 전부 0이면 SAD로 예외처리
    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int x = Integer.parseInt(parts[1]);

        int[] numArr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Map<Integer, Integer> map = new HashMap<>();

        int sum = 0;
        for (int i = 0; i < x; i++) sum += numArr[i];
        map.put(sum,1); // 등록

        for (int i = x; i < n; i++) {
            sum += numArr[i];
            sum -= numArr[i-x];
            map.put(sum, map.getOrDefault(sum,0)+1);
        }


        Integer maxKey = Collections.max(map.keySet());
        if(maxKey == 0){
            sb.append("SAD");
        }
        else{sb.append(maxKey).append(" ").append(map.get(maxKey));}

        System.out.print(sb.toString().trim());
    }


}
