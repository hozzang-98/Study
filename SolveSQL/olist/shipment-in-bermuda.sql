SELECT
  date(order_delivered_carrier_date) as delivered_carrier_date,
  count(DISTINCT order_id) as orders
FROM olist_orders_dataset
WHERE order_delivered_carrier_date like '2017-01%'
and order_delivered_customer_date is NULL
GROUP BY delivered_carrier_date
ORDER BY delivered_carrier_date