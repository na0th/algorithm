import java.util.*;
import java.io.*;
import java.lang.Math;
class Solution {
    /**
    문자열 str1,str2가 있을 때,
    반복되는 문자열이 있으면 그걸 리턴
    
    알고리즘 분류 : 문자열
    어떻게 풀이? 
    길이가 긴 게 우선..

    최대공약수를 구한다.
    그후 최대공약수 size만큼 반복되는지 확인하고 되면 문자열리턴, 아니면 "" 리턴 
     */
    public String gcdOfStrings(String str1, String str2) {
        int max = Math.max(str1.length(),str2.length());
        int min = Math.min(str1.length(),str2.length());
        
        int gcd = gcd(max,min);
        String gcdString = str1.substring(0, gcd);
        
        
        StringBuilder sb1 = new StringBuilder();
        for (int i = 0; i < str1.length() / gcd; i++) {
            sb1.append(gcdString);
        }
        String repeatedString1 = sb1.toString();

        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < str2.length() / gcd; i++) {
            sb2.append(gcdString);
        }
        String repeatedString2 = sb2.toString();
        
        if(repeatedString1.equals(str1.toString()) && repeatedString2.equals(str2.toString())){
            return gcdString;
        }else{
            return "";
        }

    }
    private int gcd(int a,int b){
        while(b != 0){
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}