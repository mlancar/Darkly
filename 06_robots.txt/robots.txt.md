# robots.txt

If we visit the URL `/robots.txt`, we can read the contents of the file:  
```html
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

This means all user-agents (i.e., web crawlers) are disallowed from accessing the `/whatever/` and `/.hidden/` directories.  

Navigating to the `/.hidden/` directory, we discover multiple subdirectories, each containing a README file — and sometimes even more nested subdirectories, also containing README files.  

By writing a Python script, we can recursively retrieve all the README files and check if any of them differ from the others.  

There are 18279 README files in total. All of them are exactly 34 bytes, except for one, which is 90 bytes.  


```bash
$> find . -type f -exec du -b {} + | sort -n | uniq -c
[...]
1 34	./README_9998
1 34	./README_9999
1 90	./README_2585

$> cat ./README_2585
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```
