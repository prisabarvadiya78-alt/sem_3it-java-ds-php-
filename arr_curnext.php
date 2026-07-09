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


$arr=array("orange","apple","grapes","kiwi");
$fruit=array_shift($arr);
print_r($arr);
echo "<br>";

$arr2=array("green","blue");
$frt=array_unshift($arr2,"black");
print_r($arr2);
echo "<br>";

$arr3=array("orange","red","black","green");
$result=array_merge($arr2,$arr3);
print_r($result);
?>