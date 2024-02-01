def solution(cacheSize, cities):
#   캐시 크기는 0~30
# 대소문자 구분 안함
#     캐시 히트 시 1초, 캐시 미스 시 5초

#   1, 2 ,1이면 
#   1,2에서 -> 2,1로 바뀌어야 함

    cache = []
    cnt_sec = 0
    for city in cities :
        
        # print(cache,cnt_sec)
        city = city.lower()
        if len(cache) < cacheSize :
            if city not in cache :
                cache.append(city)
                cnt_sec += 5
                continue
            else :
                idx = cache.index(city)
                cache.append(city)
                del cache[idx]
                cnt_sec += 1
                continue
                
        if len(cache) == cacheSize :
            if city not in cache :
                cache.append(city)
                del cache[0]
                cnt_sec += 5
                continue
            else : 
                idx = cache.index(city)
                cache.append(city)
                del cache[idx]
                cnt_sec += 1
                continue
            
            
                
    answer = cnt_sec
    return answer