-- 코드를 입력하세요
SELECT (FLOOR(PRICE / 10000) * 10000), COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY FLOOR(PRICE / 10000)
ORDER BY FLOOR(PRICE / 10000)