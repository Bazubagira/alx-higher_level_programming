-- lists the number of records with the same score
-- displays this data sorted by number in descending order

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
