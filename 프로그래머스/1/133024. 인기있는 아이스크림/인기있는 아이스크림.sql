/*
상반기에 판매된 아이스크림의 맛을 
총주문량 내림차순 정렬하고, 출하 번호 오름차순 정렬
*/
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC