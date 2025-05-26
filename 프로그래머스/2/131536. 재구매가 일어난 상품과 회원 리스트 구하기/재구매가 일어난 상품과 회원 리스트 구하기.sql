-- 코드를 입력하세요
/*
동일한 회원이 동일한 상품 재구매한 데이터를 구하여
재구매한 회원 ID와 상품 ID를 출력
회원 ID로 오름차순, 상품 ID로 내림차순
*/
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*)>=2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;