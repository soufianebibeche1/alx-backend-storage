-- 3-glam_rock.sql
-- Lists all bands with Glam rock as their main style, ranked by their longevity

SELECT
    band_name,
    IF(split = 0, 2022 - formed, split - formed) AS lifespan
FROM
    bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
