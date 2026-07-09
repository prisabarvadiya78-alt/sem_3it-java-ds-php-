<?php

$university = array("test",1,2,3,4,5);

echo "Original Array:<br>";
print_r($university);
echo "<br>";

sort($university);
echo "sort():<br>";
print_r($university);
echo "<br>";

rsort($university);
echo "rsort():<br>";
print_r($university);
echo "<br>";


asort($university);
echo "asort():<br>";
print_r($university);
echo "<br>";

arsort($university);
echo "arsort():<br>";
print_r($university);
echo "<br>";

?>