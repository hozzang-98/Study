SELECT
  ROUND(
    COUNT(CASE WHEN credit LIKE '%gift%' THEN artwork_id END) * 100.0 / COUNT(artwork_id),
    3
  ) AS ratio
FROM artworks;