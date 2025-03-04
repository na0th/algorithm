import java.util.*;

class Solution {
    /**
    nums1 배열과 nums2 배열이 주어진다.
    nums1, nums2의 길이는 1000 이하일 때
    1 입장에서 2에는 없는 값만 남김.
    2 입장에서는 1에는 없는 값만 남김.

    [[a],[b]] 꼴로 리턴

    알고리즘 분류 :  집합? 
    어떻게 풀이 ? 
    1. nums1을 집합으로 만든다, nums2를 집합으로 만든다.
    2. nums1에 모든 값에 대해서 nums2에 있는지 확인한다.
    2-1. 없다면 리스트 a에 추가한다.
    3. nums2에 모든 값에 대해서 nums1에 있는지 확인한다.
    3-2. 없다면 리스트 b에 추가한다

    리턴한다.

     */
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
       
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for(int num: nums1) set1.add(num);
        for(int num: nums2) set2.add(num);
        
        List<Integer> numList1 = new ArrayList<>();
        List<Integer> numList2 = new ArrayList<>();

        for(int num : set1){
            if (!set2.contains(num)){
                numList1.add(num);
            }
        }
        for(int num: set2){
            if (!set1.contains(num)){
                numList2.add(num);
            }
        }
        
        

        return Arrays.asList(numList1,numList2);
    }
}