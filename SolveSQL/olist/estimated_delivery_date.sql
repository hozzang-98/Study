SELECT 
  date(order_purchase_timestamp) as purchase_date,
  COUNT(DISTINCT CASE WHEN order_delivered_customer_date <= order_estimated_delivery_date THEN order_id ELSE NULL END) as success,
  COUNT(DISTINCT CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN order_id ELSE NULL END) as fail
FROM olist_orders_dataset
GROUP BY purchase_date
HAVING date(order_purchase_timestamp) like '2017-01%'