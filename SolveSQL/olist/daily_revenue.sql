SELECT 
  date(order_purchase_timestamp) as dt,
  round(sum(payment_value), 2) as revenue_daily
FROM olist_orders_dataset tmp1
INNER JOIN olist_order_payments_dataset tmp2
ON tmp1.order_id = tmp2.order_id
WHERE dt >= '2018-01-01'
GROUP BY dt
ORDER BY dt 