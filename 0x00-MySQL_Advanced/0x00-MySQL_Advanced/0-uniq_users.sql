-- Task: Create a table named 'users' with the following fields:
-- id, email, name
-- This table will store user information with unique email addresses.

-- Script that creates a table 'users' with the following fields:
-- 1. id: An integer that serves as the primary key. It auto-increments with each new record.
-- 2. email: A varchar field with a maximum length of 255 characters. It must be unique and not null.
-- 3. name: A varchar field with a maximum length of 255 characters. It can be null

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
