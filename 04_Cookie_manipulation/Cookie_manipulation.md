# Cookie manipulation

In the cookie section of this webpage we can see one cookie :  
- Name : `I_am_admin`
- Value :  `68934a3e9455fa72420237eb05902327`

The value obtained is hashed.  
Using a md5 decryption tool, we can retrieve the real value:  
> false

By encrypting `true` we can exploit this cookie and get the flag : 
> true -> b326b5062b2f0e69046810717534cb09
