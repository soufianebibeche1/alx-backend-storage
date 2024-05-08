-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name,
       CASE
           WHEN formed = 'N/A' OR split = 'N/A' THEN 0
           ELSE (2022 - CAST(formed AS UNSIGNED)) - (2022 - CAST(split AS UNSIGNED))
       END AS lifespan
FROM bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
