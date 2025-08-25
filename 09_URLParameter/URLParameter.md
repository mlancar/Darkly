# URLParameter

By inspecting the footer of the page, we found the following HTML:  
```html
<a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a>
<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>
<a href="index.php?page=redirect&amp;site=twitter" class="icon fa-facebook"></a>
```

This suggests that the website uses a redirect page that takes a site parameter to redirect users to different platforms.  
By modifying the site parameter in the URL, for example:  
```html
index.php?page=redirect&site=flag
```
… we are able to trigger a response that displays the flag.