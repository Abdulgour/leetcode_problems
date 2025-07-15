# Write your MySQL query statement below
    DELETE FROM person
WHERE id NOT IN (
    SELECT * FROM (
        SELECT MIN(id)
        FROM person
        GROUP BY email
    ) AS temp
);

