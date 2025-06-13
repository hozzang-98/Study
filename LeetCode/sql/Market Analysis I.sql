SELECT 
    T1.user_id as buyer_id,
    T1.join_date,
    COUNT(T2.order_id) as orders_in_2019
FROM Users T1
LEFT JOIN Orders T2
ON T1.user_id = T2.buyer_id
and YEAR(T2.order_date) = 2019
GROUP BY T1.user_id, T1.join_date