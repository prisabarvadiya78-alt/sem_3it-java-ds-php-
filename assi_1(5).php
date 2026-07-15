<?php

$a=15;
$b=45;
$c=30;

if($a>$b && $a>$c)
{
    echo "Maximum Number = ".$a;
}
elseif($b>$a && $b>$c)
{
    echo "Maximum Number = ".$b;
}
else
{
    echo "Maximum Number = ".$c;
}

?>