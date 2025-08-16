-- 코드를 입력하세요
SELECT 
    MCDP_CD AS "진료과 코드",
    COUNT(*) AS "5월예약건수"
FROM 
    APPOINTMENT
WHERE 
    TO_CHAR(APNT_YMD, 'YYYY') = '2022'
    AND TO_CHAR(APNT_YMD, 'MM') = '05'
GROUP BY 
    MCDP_CD
ORDER BY 
    "5월예약건수" ASC,
    MCDP_CD ASC;