
<?php
#call by reference
echo "<br>";
function sum($x,$y)
{
   $z=$x+$y;
   return $z;
}
echo sum(10,20);
?>