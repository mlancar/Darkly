# XSS Filter Evasion

On the home page, clicking on the NSA Prism image redirects the user to the page:  
 `/?page=media&src=nsa`  

This type of functionality is often vulnerable to **Cross-Site Scripting (XSS)** attacks if user-supplied parameters (like `src`) are not properly sanitized before being injected into the HTML.  

From the [OWASP XSS Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html), we can find multiple payload examples to test for XSS bypasses.  

In this specific case, the `src` parameter is expected to point to a media resource (e.g., an image). This means many standard JavaScript payloads will be blocked unless they appear to be a valid image source.  

We can still achieve an XSS payload by using this input :  
`/index.php?page=media&src=data:text/html,%3Cscript%3Ealert%28%22marine%22%29%3C%2Fscript%3E%20`

**Note :** the `<script>alert("marine")</script>` payload need to be URL-encoded.  

Since the application expects a media-type resource, we can use Base64 encoding to disguise our HTML payload as data:  

`/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgibWFyaW5lIik8L3NjcmlwdD4= `