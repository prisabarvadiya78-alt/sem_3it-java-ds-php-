<?php
#default argument
echo "<br>";
function two($x,$y,$z=9)
{
    echo $x+$y+$z;
    return $z;
}
two(10,20);
echo "<br>";
two(10,20,9);


?>
