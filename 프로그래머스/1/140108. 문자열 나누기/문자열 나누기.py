def solution(s):
    from collections import deque
    '''
    글자를 처음 읽고 이걸 x라고 정하고, -> 진행
    x와 x가 아닌 글자의 횟수 셈 
    같아지면 초기화
    
    s가 남아있을 때까지 실행
    x를 지정하고 cnt_x, cnt_else를 1,0으로 초기화
    s에서 pop(0)해서 삭제(deque로 popleft)
    if cnt_x == cnt_else ?
        초기화
    
    x가 아닌 글자가 나왔다 
    cnt
    
    끝났다 ?
    
    초기화 -> x 초기화, cnt_x , cnt_else 초기화
    '''

    def split_string(s):
        s = deque(s) 
        x = None
        cnt_split = 0
        cnt_x, cnt_else = 0, 0

        while s:
            if x is None:
                x = s.popleft()
                cnt_x = 1
            else:
                current = s.popleft()
                if current == x:
                    cnt_x += 1
                else:
                    cnt_else += 1

            if cnt_x == cnt_else:
                cnt_split += 1
                x = None
                cnt_x, cnt_else = 0, 0

        # 나머지 문자열이 남아있다면 한 번 더 추가
        if x is not None:
            cnt_split += 1
        return cnt_split
    
    return split_string(s)
    