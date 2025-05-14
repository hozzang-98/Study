SELECT seller_id, count(DISTINCT order_id) as orders
FROM olist_order_items_dataset
GROUP BY seller_id
HAVING orders >= 100;

SELECT min(date(order_purchase_timestamp)) as first_order_date, max(date(order_purchase_timestamp)) as last_order_date
FROM olist_orders_dataset