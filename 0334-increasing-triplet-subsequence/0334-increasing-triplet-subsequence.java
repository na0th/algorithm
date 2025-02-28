import java.util.*;

class Solution {
    /**
    증가하는 3개의 수가 있으면 true, 없으면 false
    알고리즘 분류 : 완전탐색? -> n이 10^5라서 안된다..
    구현?
    어떻게 풀이 ? 
    num은 자기보다 큰 값이 존재하면 교체한다. cnt+=1한다. 
    끝까지 갔을 때, cnt가 2이상이면 true 반환하기
    이건 맨처음 숫자에만 해당되는 건데..

    그럼 이걸 정렬을 기준으로 생각해보면?
    제일 작은 값의 인덱스보다 큰 게 2개 이상 있으면 된다..
    32415
    1(4)
    2(2)
    3(1)
    4(3)
    5(5)
     */
    class Pair{
        int index, value;
        Pair(int index, int value){
            this.index = index;
            this.value = value;
        }
        
        private int getValue(){
            return this.value;
        }
        private int getIndex(){
            return this.index;
        }
    }
    
    public boolean increasingTriplet(int[] nums) {
        int count = 0;
        List<Pair> pairs = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            pairs.add(new Pair(i,nums[i]));
        }

        pairs.sort(Comparator.comparingInt(p->p.value));

        Pair point_pair = pairs.get(0);
        for(Pair pair : pairs){
            if (point_pair.getIndex() > pair.getIndex()){
                count+=1;
            }
        }
        System.out.println(count);
        if (count >=2){
            return true;
        }
        else{
            return false;
        }
    }
}