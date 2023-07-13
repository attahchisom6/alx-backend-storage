-- script that list all band with Glam rock as their main syle ordered by their longevity

select band_name, (IFNULL(split, 2022) - formed) as lifespan FROM metal_bands
where style = "Glam rock"
ORDER BY lifespan DESC;
