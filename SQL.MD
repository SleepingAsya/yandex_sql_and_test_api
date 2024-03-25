## SQL запрос

```sql
-- Задание 1
SELECT c.login, COUNT(o.track)
FROM "Couriers" AS c
FULL OUTER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
OR o."inDelivery" IS NULL
OR c.login IS NULL
GROUP BY c.login;

-- Задание 2
SELECT track,
       CASE
           WHEN "inDelivery" = true THEN 1
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           ELSE 0
       END
FROM "Orders";
```