# Database and SQL Query

Following, there is the answer for the Exercise 5.

```sql
SELECT customer_name, SUM(order_value) AS total_order_value
FROM orders
WHERE customer_name = $3
      AND order_date >= $1
      AND order_date <= $2
GROUP BY customer_name;
```

Where $1, $2 and $3 are the parameters for "start date", "end date" and "customer name", respectively.
An improvement should be suggested on changing the table structure, by adding or replacing the customer_name by
a customer ID.
Since it's common to exist people with equal names, and ID would avoid wrong results for homonyms.
