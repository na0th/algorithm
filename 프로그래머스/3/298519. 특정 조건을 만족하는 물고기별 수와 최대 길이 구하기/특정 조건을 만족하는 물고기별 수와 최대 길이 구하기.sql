-- 코드를 작성해주세요
/*
FISH_INFO에서 평균 길이가 33cm 이상인 물고기들을 종류별로 분류
잡은 수, 최대 길이, 물고기의 종류를 출력
물고기 종류에 대해 오름차순, 10cm이하 10cm로 취급하여 평균 길이를 구해주세요.
*/

SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO I
GROUP BY FISH_TYPE 
HAVING AVG(COALESCE(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE ASC