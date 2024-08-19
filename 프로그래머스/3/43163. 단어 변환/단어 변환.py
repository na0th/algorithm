def solution(begin, target, words):
    from collections import defaultdict
    from collections import deque
    '''
    단어가 연결되어 있는지 딕셔너리형으로 만들어야함
    hot : dot, lot
    dot : hot, dog
    dog : log, cog, dot 등등
    
    2중 for문으로 철자 1개만 다른지 check
    '''
    dic = defaultdict(list)
    for i in range(len(words)):
        for j in range(len(words)) :
            cnt = 0
            for k in range(len(words[i])) :
                if words[i][k] != words[j][k] :
                    cnt+=1
            if cnt == 1:
                dic[words[i]].append(words[j])
    for i in range(len(words)):
        cnt = 0
        for j in range(len(words[i])):
            if words[i][j] != begin[j] :
                cnt+=1
        if cnt == 1 :
            dic[begin].append(words[i])
    print(dic)
    
    cnt = 0
    result = []
    def bfs(start_word,target, dic):
        queue = deque([(start_word, 0)])
        visited = set([start_word])

        while queue:
            curr_word, curr_count = queue.popleft()
            if curr_word == target :
                return curr_count
            for next_word in dic[curr_word]:
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, curr_count+1))
        return 0
    return bfs(begin,target,dic)
    