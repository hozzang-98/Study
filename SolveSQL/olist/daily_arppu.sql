SELECT 
  date(TMP1.order_purchase_timestamp) as dt,
  COUNT(DISTINCT TMP1.order_id) as pu,
  SUM(TMP2.payment_value) as revenue_daily,
  round(SUM(TMP2.payment_value) / COUNT(DISTINCT TMP1.order_id), 2) as arppu
FROM olist_orders_dataset TMP1
INNER JOIN olist_order_payments_dataset TMP2
ON TMP1.order_id = TMP2.order_id
WHERE dt >= '2018-01-01'
GROUP BY dt
ORDER BY dt