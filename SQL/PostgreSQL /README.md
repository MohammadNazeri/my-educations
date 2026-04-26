# PostgreSQL 
* PostgreSQL (often called Postgres) is a powerful, open-source relational database management system
* Supports both structured data (tables) and semi-structured data (like JSON)
* In PostgreSQL, a schema is a namespace that groups related database objects (like tables and views) inside a database.

## Operations
* conventions: all keywords are uppercase and anythings related to tables are lowercase.
* CREATE TABLE [table name] ([columns]);
```
CREATE TABLE profile(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  password TEXT,
  age INT
);
```
Note: SERIAL is automatically adds 1
* INSERT INTO [table name] ([columns] VALUES ([values]);
```
INSERT INTO profile (email, name, age, password) VALUES ('tory@gmail.com', 'Troy', 26, 'asfdasdf');
```
Note: Use single quotes when writing text and Use double quotes for table names, column names, etc.

* SELECT * FROM [table name];
* SELECT column1,column2,etc FROM [table name];
* SELECT * FROM [table name] WHERE conditions;
```
SELECT * FROM WHERE age>20;
```
* UPDATE [table name] SET age=30 WHERE id=1;
* DELETE FROM [table name] WHERE id=2;

## Table Relationships
* Tables can have relationships with other tables. This is how we relate entities to on another.
* THere are 3 types of basic relationship:
  * one-one
  * one-many
  * many-many
