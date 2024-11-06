class Solution {
    public String solution(int[] food) {
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < food.length; i++) {
            answer.append(String.valueOf(i).repeat(food[i] / 2));
        }
        answer.append(0);
        for (int i = food.length-1; i >= 0; i--) {
            answer.append(String.valueOf(i).repeat(food[i] / 2));
        }
        return answer.toString();
    }
}