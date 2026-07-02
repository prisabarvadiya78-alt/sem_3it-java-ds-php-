<?php
#nesting of function
echo "<br>";
function three($name)
{
   echo $name;
}
function four()
{
   echo "this is four";
   echo "<br>";
   three("this is three");
}
four();


?>