-- 코드를 작성해주세요
/*
사원별 성과급 정보 조회

기준 점수에 따른 평가 
현재 연봉과 평가 등급에 따른 성과급 비율로 성과급을 계산
*/
WITH PLUS_GRADE AS (
    SELECT G.EMP_NO, G.YEAR, AVG(G.SCORE) AS AVG_SCORE,
        CASE 
            WHEN AVG(G.SCORE) >= 96 THEN 'S'
            WHEN AVG(G.SCORE) >= 90 THEN 'A'
            WHEN AVG(G.SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE,
        CASE
            WHEN AVG(G.SCORE) >= 96 THEN 0.20  -- 예: S 30%
            WHEN AVG(G.SCORE) >= 90 THEN 0.15   -- A 20%
            WHEN AVG(G.SCORE) >= 80 THEN 0.10   -- B 10%
            ELSE 0.00                      -- C 0%
        END AS BONUS_RATE
    FROM HR_GRADE G
    GROUP BY G.EMP_NO, G.YEAR
)
# SELECT *
# FROM PLUS_GRADE

SELECT E.EMP_NO, E.EMP_NAME, G.GRADE, (E.SAL*G.BONUS_RATE) AS BONUS
FROM HR_DEPARTMENT D
JOIN HR_EMPLOYEES E ON D.DEPT_ID = E.DEPT_ID
JOIN PLUS_GRADE G ON E.EMP_NO = G.EMP_NO
ORDER BY E.EMP_NO ASC