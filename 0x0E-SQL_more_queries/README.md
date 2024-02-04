# 0x0E. SQL - More queries

- To create a new MySQL user, you can use the CREATE USER statement with the username, host, and password. For example:

```sql
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'Secure1pass!';
```

- To manage privileges for a user to a database or table, you can use the GRANT and REVOKE statements with the user, host, and privilege list. For example:

```sql
GRANT SELECT, INSERT, UPDATE ON database1.* TO 'bob'@'localhost';
REVOKE DELETE ON database1.table1 FROM 'bob'@'localhost';
```

- A PRIMARY KEY is a column or a combination of columns that uniquely identifies each row in a table. A primary key cannot contain NULL values and must be unique across the table. For example:

```sql
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE
);
```

- A FOREIGN KEY is a column or a combination of columns that references the primary key of another table. A foreign key establishes a relationship between two tables and enforces referential integrity. For example:

```sql
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

- NOT NULL and UNIQUE are two types of constraints that can be applied to columns in a table. A NOT NULL constraint prevents a column from having NULL values. A UNIQUE constraint ensures that a column or a combination of columns has no duplicate values. For example:

```sql
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  category VARCHAR(20) UNIQUE
);
```

- To retrieve data from multiple tables in one request, you can use the JOIN and UNION operators. A JOIN operator combines rows from two or more tables based on a common column or condition. A UNION operator combines the result sets of two or more SELECT statements with the same number and type of columns. For example:

```sql
-- Using JOIN
SELECT customers.name, orders.amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;

-- Using UNION
SELECT name, price FROM products
UNION
SELECT name, amount FROM orders;
```

- A subquery is a query within another query. A subquery can be used in various clauses of a SQL statement, such as SELECT, FROM, WHERE, HAVING, etc. A subquery can return a single value, a row, a column, or a table. For example:

```sql
-- Using subquery in SELECT clause
SELECT name, (SELECT AVG(price) FROM products) AS average_price
FROM products;

-- Using subquery in WHERE clause
SELECT name, price
FROM products
WHERE price > (SELECT MAX(price) FROM orders);

-- Using subquery in FROM clause
SELECT name, total
FROM (SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id) AS order_summary
JOIN customers ON order_summary.customer_id = customers.customer_id;
```
