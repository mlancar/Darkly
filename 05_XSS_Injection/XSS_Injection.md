# XSS Injection

On the feedback page (`/index.php?page=feedback`), there's a form with two fields: name and comment.  

Some JavaScript validations are performed on the client side.
By entering random values, we can quickly trigger the flag without fully understanding why.  

Further investigation reveals the likely goal of this exercise: to demonstrate an XSS (Cross-Site Scripting) vulnerability.  

HTML entered in the name or comment fields is interpreted by the browser, which can be used to gather information or execute arbitrary code.  

Example input:  
Name: <p>test</p>  