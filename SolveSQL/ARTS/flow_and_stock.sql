WITH YEARLY_CNT AS (
  SELECT
    strftime('%Y', acquisition_date) AS "Acquisition year",
    COUNT(artwork_id) AS "New acquisitions this year (Flow)"
  FROM artworks
  WHERE acquisition_date IS NOT NULL
  GROUP BY "Acquisition year"
)

SELECT 
  *,
  SUM("New acquisitions this year (Flow)") OVER (ORDER BY "Acquisition year") AS "Total collection size (Stock)"
FROM YEARLY_CNT;