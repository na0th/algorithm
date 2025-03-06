import java.util.*;
class RecentCounter {
    Deque<Integer> pings = new ArrayDeque<>();
    /**
    t-3000 ~ t안에 포함되는 요청 갯수를 카운팅

    알고리즘 분류 : 큐? 왜지??
    어떻게 풀이 ?
    ping 시작 시간을 다 담는다.
    [1 500 3000 3001]
    1 오른쪽으로 들어온다.
    2 나-3000보다 맨 앞이 큰지 체크
    3 작다면 맨 앞의 수를 제거..크거나 같다면 size를 리턴한다..
     */
    public RecentCounter() {
        
    }
    
    public int ping(int t) {
        pings.addLast(t);
        return this.check(t);
    }
    public int check(int t){
        while(pings.size()>=1){
            int num = pings.peekFirst();
            if(num < (t-3000)){
                pings.removeFirst();
            }
            else{
                break;
            }
        }
        return pings.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */