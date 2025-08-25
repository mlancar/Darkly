# Form

On the survey page (`/?page=survey`), there is a table displaying grades for different subjects.  

Each grade can be changed by selecting a new value from a dropdown menu.  

By modifying the `value` attribute of one of the `<option>` elements to a random or unexpected value, we can trigger unexpected behavior.  
This results in the flag being revealed.  

```html
<option value="200">2</option>
```
