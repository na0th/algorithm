import java.util.*;
class Solution {
    /**
    소행성의 속도는 모두 같다..
    인덱스가 상대적 위치를 나타냄
    소행성 작은쪽이 폭발
    크기가 같으면 같이 폭발

    같은 방향으로 움직이면 절대 만나지 않음.


    처음 다른 방향이 나오면 충돌해서 새로운 방향을 만들 수 있음..
    3 5 -6 -> 3 -6 -> -6
    
    마지막에 남은 배열 출력
    알고리즘 분류  : 스택
    어떻게 풀이? 
    1)제일 위에것과 새로 들어올 애를 부호를 비교..
    2)같으면 넣고, 다르면 크기 비교해서 작은 거를 뺌..
    3)반복.. 비어있으면 부호가 같으면 집어넣는다

    10 2 -5 
    10 -5
    10
    */
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> st = new ArrayDeque<>();

        for(int ast : asteroids){
            boolean b = true;

            while(!st.isEmpty()){
                int top = st.peekFirst();
                if( top > 0 && ast < 0){
                    if(Math.abs(top) < Math.abs(ast)){
                        st.removeFirst();
                    }
                    else if(Math.abs(top) == Math.abs(ast)){
                        st.removeFirst();
                        b = false;
                        break;
                    }
                    else{
                        b = false;
                        break;
                    }           
                
            }else{
                break;
                }
            }
             if(b){
                st.addFirst(ast);
            }
        }
            
        
        int[] result = new int[st.size()];
        for (int i = st.size() - 1; i >= 0; i--) {
            result[i] = st.removeFirst();
        }
        return result;
    }
}