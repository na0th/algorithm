-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH,'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE TLNO IS NOT NULL AND GENDER = 'W' AND TO_CHAR(DATE_OF_BIRTH,'MM') = 3
ORDER BY MEMBER_ID ASC;