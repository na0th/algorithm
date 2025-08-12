-- 코드를 입력하세요
/*
보호소 들어올 때는 중성화 X
보호소를 나갈 때는 중성화된 동물

spayed female -> spayed female 은 이미 중성화 취급
intact male -> Neutered Male은 보호소 들어왓 중성화 취급
intact female -> spayed female은 보호서 들어와서 중성화 취급

*/
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE (I.SEX_UPON_INTAKE = 'Intact Male' AND O.SEX_UPON_OUTCOME = 'Neutered Male') 
    OR (I.SEX_UPON_INTAKE = 'Intact Female' AND O.SEX_UPON_OUTCOME = 'Spayed Female')
ORDER BY I.ANIMAL_ID ASC