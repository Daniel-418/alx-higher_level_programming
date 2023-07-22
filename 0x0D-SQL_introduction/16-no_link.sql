-- lists all recores of the table second_table having no name
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
