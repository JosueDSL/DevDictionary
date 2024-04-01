# PostgreSQL

## Initial Setup Steps

### Instalation
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```
Ensure that the service is started:
`sudo systemctl start postgresql.service`

### Start PostgreSQL Server 
After installation, you need to start the PostgreSQL server. On most systems, you can do this using a command like:
`sudo service postgresql start`

### Roles - Create user
Switch over to the postgres account on your server by running the following command: 
```bash
sudo -i -u postgres
```
Then you can access the Postgres prompt by running:
```bash
psql
```
If you are logged in as the postgres account, you can create a new role by running the following command:
```bash
postgres@server:~$ createuser --interactive
```
If, instead, you prefer to use sudo for each command without switching from your normal account, run:
```bash
$ sudo -u postgres createuser --interactive
```
The script will prompt you with some choices and, based on your responses, execute the correct Postgres commands to create a user to your specifications.

### Alternative way to create the user
Once that you're in the psql prompt, you can create a new user using the CREATE ROLE command.
`CREATE ROLE user_name WITH LOGIN PASSWORD 'securepassword';`

**GRANT PRIVILEGES**
If you want to grant specific privileges to the user, you can do so using the GRANT command. For example, to grant all privileges on a specific database to the user "john", you can do:
`GRANT ALL PRIVILEGES ON DATABASE dbname TO user-name;`

### Creating a New Database
If you are logged in as the postgres account, you would type something like the following:
`createdb "DB_NAME";`

### Opening a Postgres Prompt with the New Role
To log in with ident based authentication, you’ll need a Linux user with the same name as your Postgres role and database.

If you don’t have a matching Linux user available, you can create one with the adduser command. You will have to do this from your non-root account with sudo privileges (meaning, not logged in as the postgres user):
`sudo adduser USER_NAME`
Once this new account is available, you can either switch over and connect to the database by running the following:
```bash
sudo -i -u USER_NAME
psql
```
Or, you can do this inline:
`sudo -u USER_NAME psql`

If you want your user to connect to a different database, you can do so by specifying the database like the following:
`psql -d postgres` postgres as an example

Once logged in, you can get check your current connection information by running:
`USERNAME=# \conninfo`

## Navigation and Interaction

- `\l` or `\list`: List all databases.
- `\c [database_name]` or `\connect [database_name]`: Connect to a specific database.
- `\dt`: List all tables in the current database.
- `\d [table_name]`: Show the structure of a specific table.
- `\du` or `\du+`: List all roles (users) in the current database.


## Transaction Control

- `BEGIN`: Start a new transaction block.
- `COMMIT`: Save the changes.
- `ROLLBACK`: Roll back the changes.

## Schema Management

- `CREATE DATABASE [database_name]`: Create a new database.
- `CREATE TABLE [table_name]`: Create a new table.
- `ALTER TABLE [table_name]`: Alter the structure of a table.
- `DROP DATABASE [database_name]`: Remove a database.
- `DROP TABLE [table_name]`: Remove a table.




## Miscellaneous

- `\timing`: Toggle timing of query execution.
- `\q` or `\quit`: Quit psql.