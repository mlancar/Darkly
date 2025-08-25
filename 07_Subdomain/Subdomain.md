# Subdomain

From the previous challenge, we found the `/whatever` directory.  
This directory contains an `.htpasswd` file with the following content:  

```text
root:437394baff5aa33daa618be47b75cb49
```

This appears to be a hash for the root account.  
The hash can be easily cracked using an online MD5 decoder:  
```text
root:qwerty123@
```

So now we have valid credentials, but we still need to find the page where they can be used.  
By testing common subdomains or directories, we attempt to access the `admin/index.php` page.  
This page contains a login form.  
Entering the previously discovered credentials grants us access and reveals the flag :  

> The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
