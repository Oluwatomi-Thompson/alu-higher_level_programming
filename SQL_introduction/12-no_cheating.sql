-- This script updates Bob's score to 10 in second_table
-- Uses only the name field (not ID) to identify the record

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
