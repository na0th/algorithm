import java.util.*;
class Solution {
    public boolean isPalindrome(int x) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();

        String stringX = String.valueOf(x);

        // for(char c : StringX.toCharArray()){
        //     sb1.append(c);
        // }
        // for(char c : StringX.toCharArray()){
        //     sb2.append(c);
        // }
        for(int i=0; i<stringX.length(); i++){
            sb1.append(stringX.charAt(i));
        }
        for(int i=stringX.length()-1; i>=0; i--){
            sb2.append(stringX.charAt(i));
        }


        String stringSb1 = sb1.toString();
        String stringSb2 = sb2.toString();
        if(stringSb1.equals(stringSb2)){
            return true;
        }
        else{
            return false;
        }

    }
    
}