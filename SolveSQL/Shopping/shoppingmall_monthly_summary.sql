WITH sub_table as (
SELECT
  strftime ('%Y-%m', tmp1.order_date) as order_month,
  SUM(CASE WHEN tmp1.order_id not like 'C%' THEN tmp2.price*tmp2.quantity ELSE NULL END) as ordered_amount,
  SUM(CASE WHEN tmp1.order_id like 'C%' THEN tmp2.price*tmp2.quantity ELSE NULL END) as canceled_amount
FROM
  orders tmp1
  INNER JOIN order_items tmp2 ON tmp1.order_id = tmp2.order_id
GROUP BY order_month)

SELECT *, ordered_amount + canceled_amount as total_amount
FROM sub_table
ORDER BY order_month