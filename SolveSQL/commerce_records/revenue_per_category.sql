WITH subcate_sales as (
SELECT category, sub_category, round(sum(sales),2) as sales_sub_category
FROM records
GROUP BY category, sub_category),

cate_sales as (
SELECT category, round(sum(sales),2) as sales_category
FROM records
GROUP BY category),

total as (
  SELECT round(sum(sales),2) as sales_total FROM records
)

SELECT 
  T1.category, 
  T2.sub_category, 
  T2.sales_sub_category, 
  T1.sales_category, 
  T3.sales_total, 
  round(T2.sales_sub_category/T1.sales_category*100,2) as pct_in_category,
  round(T2.sales_sub_category/T3.sales_total*100,2) as pct_in_total
FROM cate_sales T1
INNER JOIN subcate_sales T2 ON T1.category = T2.category
CROSS JOIN total T3;