SELECT min(date(order_purchase_timestamp)) as first_order_date, max(date(order_purchase_timestamp)) as last_order_date
FROM olist_orders_dataset