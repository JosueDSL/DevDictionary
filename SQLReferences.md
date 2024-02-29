# SQL - References, Setup, Guide

## Data Types
*   **TEXT**: Variable-length character string with no maximum length specified.
*   **NUMBERIC**: Represents fix length values or boolean values
*   **INTEGER**: The classic INT you're already familiar with.
*   **FLOAT/DOUBLE**: Represents floating-point numbers, which include decimal points, such as 3.14, 2.5, etc.
*   **DECIMAL/NUMERIC**: Represents fixed-point numbers with a specified precision and scale, such as 10.50, 7.123, etc.
*   **CHAR**: Fixed-length character string, padded with spaces to the specified length.
*   **VARCHAR**: Variable-length character string, with a maximum length specified.
*   **DATE**: Represents a date value, without any time information.
*   **TIME**: Represents a time value, without any date information.
*   **DATETIME/TIMESTAMP**: Represents a date and time value.
*   **BOOLEAN**: Represents true or false values.
*   **BINARY**: Stores binary data, such as images or files.
*   **BLOB**: Stores large binary objects, such as images, audio files, etc.
*   **ENUM**: Represents a set of predefined values that a column can take.

## Constraints
- CHECK
- DEFAULT
- NOT NULL
- PRIMARY KEY
- UNIQUE
- ...

## Keywords
- WHERE
- IN
- AND
- OR
- LIKE - %a%
- 

## Formating
- .mode colums || tables || ...
- .headers yes || no
- 


## Commands

### INSERT 
insert new rows to the tables
```SQL
INSERT INTO TABLE_NAME (id, first_name, age) VALUES (1, "Josue", 21)

```
### SELECT
The select command allows us to query data as follows
```SQL
SELECT * FROM TABLE_NAME;
or
SELECT id, age, first_name FROM TABLE_NAME;
```

## UPDATE
Update the values of a table, this would update all the values of a table where the condition is meet
```SQL
UPDATE TABLE_NAME
    SET duration = 400
    WHERE origin = "CDMX"
    AND destination = "GDL";
```

### DELETE
Delete content from a table or entires tables **MUST ALWAYS USE WHERE!!!**
```SQL
DELETE TABLE_NAME
or
DELETE FROM TABLE_NAME WHERE id = 1;
```
### JOIN
Join different tables to query data from multiple tables to a single one
Join them by using the following sintax:
```SQL
JOIN TABLE_NAME ON TABLE_NAME.id = SECOND_TABLE.first_table.id;
```
By joining the common ids
```SQL
SELECT first, origin, destination
  FROM flights JOIN passengers
ON passengers.flight_id = flights.id;
## Table Creation
```SQL
CREATE TABLE TABLE_NAME (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    age INTEGER NOT NULL,

); -- Notate the semi-collen
``` 
## FUNCTIONS
* COUNT()
* AVERAGE()
* MAX()
* MIN()
* SUM()
* LIMIT()
* GROUP BY()
* ORDER BY()
* HAVING()

## CREATE INDEX
Increase search time by indexing the search
```SQL
CREATE INDEX name_index ON TABLE_NAME (case_scenario);
```

## SQL Injection
Always sustitute the actuall value for a `?` question mark followed by a the variable after the condition is checked.

