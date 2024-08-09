-- Task: Create an index on the 'names' table to improve query performance
-- by indexing the first letter of the 'name' column.

CREATE INDEX idx_name_first ON names(name(1));
