# Header Spoofing

In the Html there is a long comment, and there is two phrase that are useful:  
"you must come from: "https://www.nsa.gov/" "  

This means we have to change the Referer of the Header  
There is several ways to do so  

- we can click on "Edit and Resend" the request  
And then add a value to the Header : 
**name = Referer and value = https://www.nsa.gov/**  

- Or we can use a pluggin: ModHeader, it will allow us to set the Referer we want once and it will always send the request we it.  

The second thing is "Let's use this browser : "ft_bornToSec". It will help you alot."  

The browser refers to what browser the request comes from, so User-Agent in the Header. So we have to change it, to do so we can use the same method as before and use the ModHeader, and just add a new name and value  
**User-Agent and ft_bornToSec**  

And we have the flag