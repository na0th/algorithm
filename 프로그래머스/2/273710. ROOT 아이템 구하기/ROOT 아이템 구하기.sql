-- 코드를 작성해주세요\
/*
ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.

*/

SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO I
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID ASC