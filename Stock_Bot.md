# Stock Bot by Om Honrao @Om12



=====================================================

# This challenge comes under web category.

If the player see's the source code he can see a hint:- 
```
Hint: Along with other products the Flag is also available in the Products directory
```
So, now we know flag in in `Flag` and now if we send some message to the bot suppose `Monitor`, same time see where the bot is doing `POST` request using Dev Tools.i.e. press `Ctrl+shift+i`.

The player will see that bot does a POST request at `/Products/check.php?product=Monitor` this endpoint.

So, we can change this payload. We can change `product=` value to `Flag` .i.e. got to this link `https://st0ck-b0t.vishwactf.com/Products/check.php?product=Flag` and then press enter.

and Boom! you get flag!

# Flag :- VishwaCTF{b0T_kn0w5_7h3_s3cr3t}