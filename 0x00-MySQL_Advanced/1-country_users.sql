-- Task: Create a table named 'users' with the following fields:
-- id, email, name, and country (enumeration of 'US', 'CO', and 'TN').
-- This table will store user information with unique email addresses and specified country values.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
