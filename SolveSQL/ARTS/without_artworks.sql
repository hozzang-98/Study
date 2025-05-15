SELECT
  tmp1.artist_id,
  tmp1.name
FROM
  artists tmp1
  LEFT JOIN artworks_artists tmp2 ON tmp1.artist_id = tmp2.artist_id
WHERE
  tmp1.death_year is not null
  and tmp2.artwork_id is null