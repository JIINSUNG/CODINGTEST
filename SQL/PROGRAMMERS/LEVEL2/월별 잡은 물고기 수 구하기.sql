-- https://school.programmers.co.kr/learn/courses/30/lessons/293260

SELECT COUNT(ID) as FISH_COUNT, MONTH(TIME) as MONTH
FROM FISH_INFO
GROUP BY MONTH
ORDER BY MONTH ASC
