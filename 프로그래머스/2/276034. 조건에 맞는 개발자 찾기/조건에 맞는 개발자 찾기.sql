-- 코드를 작성해주세요
/*
DEVELOPERS 테이블에서 'Python' or 'C#'가진 개발자 정보 조회(아이디, 이메일, 이름, 성)
ID 기준 오름차순

CODE를 & 연산을 통해 1이 나오는지 0이 나오는지로 포함 여부 확인이 가능함..
*/
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S
    ON S.CODE & D.SKILL_CODE 
WHERE S.NAME IN ('Python', 'C#')
ORDER BY ID;