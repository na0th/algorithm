import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    /*
    (몸무게, 키) 꼴로 여러 사람의 데이터가 주어지는데
    A가 B보다 덩치가 크다고 정의하려면 몸무게와 키 모두 커야 함.
    데이터가 주어졌을 때, 각 사람의 덩치 등수를 적어야 한다.
    분류 : 완전탐색
    어떻게 풀이 ?
    1. 각 사람마다 모든 사람과 비교해서 자신보다 몇명이 덩치가 큰지 따진다.
    2. 자신보다 덩치가 큰 수를 기준으로 덩치 등수를 산출

    1 1 0 1 3 이라면 2 2 1 2 5가 된다.
    덩치 큰 사람이 0명이면 그 사람은 1등이 되고,
    * */
    public static class Person{
        int weight;
        int height;
        int rank;
        Person(int weight, int height, int rank){
            this.weight = weight;
            this.height = height;
            this.rank = rank;
        }
    }
    public static void diff(Person p1, Person p2) {
        if(p1.weight < p2.weight && p1.height < p2.height){
            p1.rank++;
        } else if (p1.weight > p2.weight && p1.height > p2.height) {
            p2.rank++;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int n = Integer.parseInt(br.readLine());
        Person[] arr = new Person[n];
        for(int i=0; i<n; i++){
            int[] parts = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                                    .toArray();
            arr[i] = new Person(parts[0],parts[1],1);
        }
        //Person이 배열에 있는 상황에서 2중 for문으로 비교하기
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                diff(arr[i],arr[j]);
            }
        }
        for (Person p : arr) {
            sb.append(p.rank).append(" ");
        }
        System.out.print(sb.toString().trim());


    }
}
