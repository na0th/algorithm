
-- 코드를 입력하세요
/*
09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
이때 결과는 시간대 순으로 정렬해야 합니다.
*/
SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR , COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) BETWEEN 9 AND 19
GROUP BY TO_NUMBER(TO_CHAR(DATETIME, 'HH24'))
ORDER BY HOUR