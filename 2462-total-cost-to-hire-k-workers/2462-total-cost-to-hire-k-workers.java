import java.util.*;
class Solution {
    /**
    후보자만큼 앞에서 집합 , 뒤에서 집합 구성
    서로 최저값이 같으면 인덱스가 낮은 거로 채용
    근로자 뽑는데 최소 비용 반환

    알고리즘 분류 :
    어떻게 풀이 ? 
    앞에서 우선순위 큐, 뒤에 우선순위 큐 
    서로 최솟값을 뽑은 후, 비교한다음 같으면, 인덱스를 비교
    뽑힌 우선순위큐에 새로운 값을 채워넣음 
    candidate => c
    left = c , right = n-c+1
    뽑힌 쪽이 왼쪽이면 left+1 인덱스 값을.. 오른쪽이면 right-1 값을 넣음
    k명 뽑으면 끝냄
    */
    static class Worker implements Comparable<Worker> {
        int cost;
        int index;

        Worker(int cost, int index) {
            this.cost = cost;
            this.index = index;
        }

        @Override
        public int compareTo(Worker other) {
            if (this.cost != other.cost) return this.cost - other.cost;
            return this.index - other.index;
        }
    }
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Worker> leftHeap = new PriorityQueue<>();
        PriorityQueue<Worker> rightHeap = new PriorityQueue<>();

        int n = costs.length;
        int left = 0;
        int right = n - 1;

        for (int i = 0; i < candidates; i++) {
            if (left <= right) leftHeap.offer(new Worker(costs[left], left++));
            if (left <= right) rightHeap.offer(new Worker(costs[right], right--));
        }

        long total = 0;

        for(int i=0; i< k ; i++){
            Worker fromLeft = leftHeap.peek();
            Worker fromRight = rightHeap.peek();

            if (rightHeap.isEmpty() || (!leftHeap.isEmpty() && fromLeft.compareTo(fromRight) <= 0)){
                Worker chosen = leftHeap.poll();
                total += chosen.cost;
                if (left <= right) {
                    leftHeap.offer(new Worker(costs[left], left++));
                }
            }else {
                Worker chosen = rightHeap.poll();
                total += chosen.cost;

                if (left <= right) {
                    rightHeap.offer(new Worker(costs[right], right--));
                }
            }
        }   
        return total;
    
    }
}