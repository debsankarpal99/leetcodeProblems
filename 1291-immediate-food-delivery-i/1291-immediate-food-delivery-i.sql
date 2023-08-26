SELECT round(count(case when order_date = customer_pref_delivery_date then 1 else null end)/count(*) * 100, 2) as immediate_percentage FROM Delivery

 