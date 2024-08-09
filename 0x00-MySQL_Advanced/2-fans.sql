-- Task: Select the origin column and the sum of the fans column (as nb_fans) from the 'metal_bands' table.
-- Group the results by origin and order them by nb_fans in descending order.

SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
