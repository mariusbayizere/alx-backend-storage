-- Task: Select the band_name column and the lifespan column (calculated as the difference
--between the split year and the formed year)

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
