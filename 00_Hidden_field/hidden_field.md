# Hidden Field

By clicking on **sign in** on the Home page, we arrived on a page where we can login  
We have a message **"Sorry wrong answer"**  

We can click on **"I forgot my password"**, but there is nothing to put an email to recover a password  

So we can look at the html and the form tag and see an input type is hidden 
```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Then we can try to remove the hidden, and a field to put an email appears  

```html
<input type="" name="mail" value="webmaster@borntosec.com" maxlength="15">
```
We just have to remove the default email
```html
<input type="" name="mail" value="" maxlength="15">
```

Submitting this form will show the Flag