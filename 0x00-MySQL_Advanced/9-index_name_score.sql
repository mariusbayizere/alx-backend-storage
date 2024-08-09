-- Task: Create an index on the 'names' table to improve query performance
-- by indexing the first letter of the 'name' column and the 'score' column.

CREATE INDEX idx_name_first_score ON names(name(1), score);
