import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static class Player {
        private int level;
        private String id;

        public Player(int level, String id) {
            this.level = level;
            this.id = id;
        }

        public int getLevel() {
            return level;
        }

        public String getId() {
            return id;
        }
    }
    /*
    플레이어가 입장 가능한 방이 없으면, 방을 생성하고 입장한다. (이때 해당 방에는 처음 입장한 플레이어 레벨의 -10 ~ +10
    입장 가능한 방이 있으면, 입장하고 , 정원이 다 찰 때까지 대기한다. (입장 가능한 방이 여러개면, 먼저 생성된 방에 입장)
    방의 정원이 모두 차면 게임을 시작한다.

    플레이어의 수 p, 플레이어의 닉네임 n, 플레이어의 레벨 l, 방 한개의 정원 m
    매칭하고, 최종적으로 만들어진 방의 상태와 입장 플레이어들 출력

    분류 : 완전 탐색, 구현

    어떻게 풀이 ?
    1. 리스트를 전부 다 돌아서 입장 가능한지 아닌지 체크(조건은 리스트의 0번째 인덱스 값 범위의 +-10 , 배열의 크기 < 5)
    2. 입장 가능하면 바로 입장하고 그만둠
    3. 전부 돌아도 입장 불가능하면 방을 생성

    * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] parts = br.readLine().split(" ");

        int p = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        List<List<Player>> rooms = new ArrayList<>();

        for(int i=0; i<p; i++){
            String[] part = br.readLine().split(" ");
            int level = Integer.parseInt(part[0]);
            String id = part[1];

            Player player = new Player(level, id);

            // 맨처음 전부 비어있을 경우 초기화
            if (rooms.isEmpty()){
                rooms.add(new ArrayList<>());
                rooms.get(0).add(player);
                continue;
            }
            boolean joined = false;

            for(List<Player> room : rooms){
                //입장할 수 있다면? 입장한다
                if((level >= room.get(0).getLevel()-10 && level <= room.get(0).getLevel()+10) && room.size() < m){
                    room.add(player);
                    joined = true;
                    break;
                }
            }
            //입장할 수 없다면? 그 플레이어가 입장한 방을 생성한다
            if (!joined) {
                List<Player> newRoom = new ArrayList<>();
                newRoom.add(player);
                rooms.add(newRoom);
            }
        }


        for (List<Player> room : rooms) {
            room.sort(Comparator.comparing(Player::getId)); // 닉네임 사전순 정렬
            if (room.size() == m) sb.append("Started!\n");
            else sb.append("Waiting!\n");

            for (Player player : room) {
                sb.append(player.getLevel())
                        .append(" ")
                        .append(player.getId())
                        .append("\n");
            }
        }

        System.out.print(sb.toString().trim());
    }

}
