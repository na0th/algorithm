/* Write your PL/SQL query statement below */
/*
자신의 article을 본 author 찾기
*/
select distinct(author_id) as id
from views
where author_id = viewer_id
order by author_id asc