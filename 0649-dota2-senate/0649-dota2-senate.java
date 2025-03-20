import java.util.*;
class Solution {
    /**
    두 가지 권리중 하나를 행사
    1) 상원의원 1명의 권리를 금지시킴
    2) 승리를 선언 -> 투표권을 갖은 상원의원이 모두 같은 정당에 있다면 승리를 선언
    라운드는 계속 된다..

    모든 상원의원이 최상의 전략을 구사..
    이긴 정당을 예측하시오


    알고리즘 분류 : ?
    어떻게 풀이 
    음.. 승리 선언은 의미가 없고, 상대를 먼저 모두 제거를 해버리는게 중요
    누가 먼저 제거될지 어떻게 알까?
    ... 앞에서부터 제거시키자? 뒤에서부터?
    
    아이디어 !
    rCount,dCount 둘 다 0 시작
    0)r이나 d가 나오면 상대 count를 뒤져서 0인지 확인함, 0이 아니면 나는 제거됨.
    1)r이 나오면 1 더함, d가 나오면 1 더함
    2)r or d를 뒤로 보냄
    반복..
    
    그러면 언제끝나는가>? rTotal, dTotal을 미리 구해서, 둘중하나가 0이되면 끝낸다..
     
    
    */
    public String predictPartyVictory(String senate) {
        int rCount =0, dCount = 0;
        int rTotal = (int) senate.chars().filter(c -> c == 'R').count();
        int dTotal = (int) senate.chars().filter(c -> c == 'D').count();
        Deque<Character> q = new ArrayDeque<>();
        for(char c : senate.toCharArray()){
            q.addLast(c);
        }

        while(rTotal>0 && dTotal>0){
            char senator = q.pollFirst();

            if(senator == 'R'){
                if(dCount>0){
                    dCount--;
                    rTotal--;
                }else{
                    rCount++;
                    q.addLast(senator);
                }
            }
            else {
                if (rCount > 0) {
                    rCount--; 
                    dTotal--;  
                } else { 
                    dCount++; 
                    q.addLast(senator);
                }
            }

        }
        return rTotal > 0 ? "Radiant" : "Dire";
    }
}