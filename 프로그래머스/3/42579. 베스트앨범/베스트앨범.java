import java.util.*;
class Solution {
    /*
    장르별로 가장 많이 재생된 노래 2개씩 모아서 베스트 앨범
    1. 많이 재생된 장르 먼저
    2. 장르내에서 많이 재생된 노래 먼저
    3. 재생횟수까지 같다면, 고유번호가 낮은 노래 먼저 수록
    
    알고리즘 분류 :  해시
    
    어떻게 풀이?
    장르에 play수만큼을 더해서 제일 많이 재생된 장르를 뽑아야 함.
    장르당 최대 2개.. (곡이 1개라면 1개만..)
    
    그러면.. value들이 정렬이 되어야 하는데..?
    */
    
    
    public int[] solution(String[] genres, int[] plays) {
        
        Map<String,Integer> genreMap = new HashMap<>();
        Map<String, List<int[]>> genreToSongs = new HashMap<>();
        
        for(int i=0; i<plays.length; i++){
            //있으면 더하고, 없으면 추가하고
            genreMap.put(genres[i], genreMap.getOrDefault(genres[i], 0) + plays[i]);
            genreToSongs.computeIfAbsent(genres[i], k -> new ArrayList<>()).add(new int[]{i, plays[i]});  
        }
        
        List<String> genreOrder = new ArrayList<>(genreMap.keySet());
        genreOrder.sort((a, b) -> genreMap.get(b) - genreMap.get(a)); //내림차순
        
        List<Integer> result = new ArrayList<>();
        for(String genre : genreOrder){
            List<int[]> songs = genreToSongs.get(genre);
            songs.sort((a,b) -> {
                       if (b[1]==a[1]) return a[0]-b[0];
                        return b[1]-a[1];
                    });
            result.add(songs.get(0)[0]);
            if (songs.size() > 1) result.add(songs.get(1)[0]);
        }
        return result.stream().mapToInt(i -> i).toArray();
        // System.out.println(genreMap.toString());
        // System.out.println(genreToSongs.toString());
        
        
    }
}