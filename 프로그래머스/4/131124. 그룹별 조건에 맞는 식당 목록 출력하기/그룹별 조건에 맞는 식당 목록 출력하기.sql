-- 코드를 입력하세요
/*
리뷰를 가장 많이 작성한 회원의 리뷰들을 조회

리뷰를 가장 많이 작성한 회원을 찾는다
->최대 리뷰 개수와 리뷰 개수가 같은 회원 찾기
리뷰들을 조회
->리뷰 테이블하고 조인

*/
SELECT P.MEMBER_NAME, R.REVIEW_TEXT, TO_CHAR(R.REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE P
JOIN REST_REVIEW R
    ON P.MEMBER_ID = R.MEMBER_ID
JOIN (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(*) = (
        SELECT MAX(CNT)
        FROM(
            SELECT COUNT(*) AS CNT
            FROM REST_REVIEW 
            GROUP BY MEMBER_ID
            ) S
        ) 
    ) T ON P.MEMBER_ID = T.MEMBER_ID
ORDER BY R.REVIEW_DATE ASC, R.REVIEW_TEXT ASC
