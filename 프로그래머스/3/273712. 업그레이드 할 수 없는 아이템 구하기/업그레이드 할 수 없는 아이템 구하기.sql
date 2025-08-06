-- 코드를 작성해주세요
/*
루트 아이템
PARENT 아이템
A->B->C면
C의 PARENT는 B
B의 PARENT는 A
A는 루트


더 이상 업그레이드할 수 없는 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬해 주세요

더 이상 업그레이드할 수 없다.. => PARENT 목록에 그 ID가 없다

*/

SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
LEFT JOIN ITEM_TREE P ON I.ITEM_ID = P.PARENT_ITEM_ID
WHERE P.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID DESC;