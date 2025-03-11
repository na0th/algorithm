/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;
class Solution {
    /**
    트리의 최대 깊이를 구해야 한다.
    
    알고리즘 분류 : DFS 
    어떻게 풀이 ? 트리를 재귀로 DFS 탐색
    해당 노드의 왼쪽, 오른쪽 비교해서 큰 값에서 +1을 한다.

    

     */
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        
        return Math.max(maxDepth(root.left),maxDepth(root.right))+1;
    }
}