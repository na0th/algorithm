import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    /*
    정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
    1. 배정될 수 있으면 요청한 금액 그대로 배정한다
    2. 모든 요청이 배정될 수 없는 경우, 특정한 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
       상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
       ex) 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면,
       위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.

    출력 : 배정된 예산들 중 최댓값인 정수를 출력한다.

    분류 : 수학? 완전탐색? -> 완전탐색이라면 시간복잡도 고려 -> M이 10억이므로 완전탐색 불가.. -> 이진탐색
    어떻게 풀이 ?
    1.상한액을 X로 잡고, X이상이면 X로, X이하면 그대로 로 총합을 구한다.
    2. 그 합이 총 예산보다 크면 이진탐색.. -> 1~100000 처음에 50001


    * */
    static int targetNum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] nums = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        targetNum = Integer.parseInt(br.readLine());
        int maxReq = Arrays.stream(nums).max().getAsInt();
        long answer = find(1, maxReq,nums);
        System.out.print(answer);
    }
    public static int find(int left, int right, int[] nums){
        long total = 0;
        int mid = (left + right) / 2;

        if (left > right) {
            return right;
        }
        //mid는 최대 상한 값, 최대 상한 값 이상이면 최대 상한 값을 더하고, 아니면 num을 더한다.
        for(int num : nums){
            if(num <= mid) total += num;
            else {total += mid;}
        }
        //total이 targetNum보다 크다면?
        if (total > targetNum) {return find(left, mid-1, nums);}
        else {return find(mid + 1, right, nums);}
    }
}
