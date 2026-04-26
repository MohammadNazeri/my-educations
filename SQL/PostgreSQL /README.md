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
Example Two tables like user and posts
Note: A foreign key is a column in one table that refers to a primary key in another table.
```
CREATE TABLE post(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  content TEXT,
  user_id INT, -- foreign key
  CONSTRAINT fk_user
    FOREIGN KEY(user_id)
      REFERENCES profile(id)
);
INSERT INTO post(name, content, user_id) VALUES('why I love corgis', 'omg I love them', 1);
INSERT INTO post(name, content, user_id) VALUES('why I love animal in general', 'omg I love themmmm', 1);
```
## Join
* a JOIN is used to combine rows from two or more tables based on a related column.
* A JOIN lets you pull related data from different tables into one result.

```
SELECT profile.*. post.id, post.name AS title, post.content, post.user_id FROM profile JOIN post ON post.user_id=profile.id
```
