<?php

$a = ["test", 1, 2, 3, 6, 5];
echo "current: ".current($a);
echo "<br>";
echo "next: ".next($a);
echo "<br>";
echo "end: ".end($a);
echo "<br>";
echo "Previous: ".prev($a);
echo "<br>";
echo array_push($a,99,0,100,88);
echo "<br>";
echo array_pop($a);
echo "<br>";
print_r($a);
echo "<br>";
?>