-- 코드를 작성해주세요
/*
2번 형질을 보유하지 않으면서 1,3번 형질을 보유하고 있는 대장균 개체를 (COUNT)
GENOTYPE이.. 
*/

SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE    
  (GENOTYPE & 2) = 0       -- 2번 형질 X
  AND ((GENOTYPE & 1) = 1 OR (GENOTYPE & 4) = 4) -- 1번 형질  OR 3번 형질