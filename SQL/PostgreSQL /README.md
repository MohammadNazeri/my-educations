# PostgreSQL 
* PostgreSQL (often called Postgres) is a powerful, open-source relational database management system
* Supports both structured data (tables) and semi-structured data (like JSON)
* In PostgreSQL, a schema is a namespace that groups related database objects (like tables and views) inside a database.

## Operations
* conventions: all keywords are uppercase and anythings related to tables are lowercase.
* CREATE TABLE [name]([columns]);
```
CREATE TABLE profile(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  password TEXT,
  age INT
);
```
