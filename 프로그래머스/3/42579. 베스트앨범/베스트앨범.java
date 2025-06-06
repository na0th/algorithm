import java.util.*;
import java.util.stream.*;
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
    
    class Song{
        int index;
        int plays;
        Song(int index, int plays) {
            this.index = index;
            this.plays = plays;
        }   
    }
    public int[] solution(String[] genres, int[] plays) {
        
        Map<String,Integer> genreMap = new HashMap<>();
        Map<String, List<Song>> genreToSongs = new HashMap<>();
        
        for(int i=0; i<plays.length; i++){
            //있으면 더하고, 없으면 추가하고
            String genre = genres[i];
            int playCount = plays[i];
            
            genreMap.put(genre, genreMap.getOrDefault(genre, 0) + playCount);
            if (!genreToSongs.containsKey(genre)) {
                genreToSongs.put(genre, new ArrayList<>());
            }
            genreToSongs.get(genre).add(new Song(i, playCount));

        }
        List<String> genreOrder = new ArrayList<>(genreMap.keySet());
        genreOrder.sort((a, b) -> (genreMap.get(b)).compareTo(genreMap.get(a))); //내림차순

        List<Integer> result = new ArrayList<>();
        
        for(String genre : genreOrder){
            List<Song> songs = genreToSongs.get(genre);
            songs.sort((a,b) -> {
                       if (b.plays==a.plays) return Integer.compare(a.index,b.index);
                        return Integer.compare(b.plays,a.plays);
                    });
            result.add(songs.get(0).index);
            if (songs.size() > 1) result.add(songs.get(1).index);
        }
        return result.stream().mapToInt(i -> i).toArray();
       
    }
}