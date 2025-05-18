WITH
  SUB_TABLE as (
    SELECT
      species,
      flipper_length_mm,
      avg(flipper_length_mm) OVER (
        PARTITION BY
          species
      ) as avg_flipper,
      body_mass_g,
      avg(body_mass_g) OVER (
        PARTITION BY
          species
      ) as avg_mass
    FROM
      penguins
  )
SELECT
  species,
  ROUND(
    sum(
      (flipper_length_mm - avg_flipper) * (body_mass_g - avg_mass)
    ) / (
      sqrt(sum(Power((flipper_length_mm - avg_flipper), 2))) * sqrt(sum(Power((body_mass_g - avg_mass), 2)))
    ),
    3
  ) as corr
FROM
  SUB_TABLE
GROUP BY
  species