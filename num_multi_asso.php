<?php
//numeric array

$a=array(10,20,30);

echo $a[0]=50;
echo $a[1];
echo $a[2];
echo $a[1]=50;

echo "<br>";

$b=array("atmiya","university","rajkot");

echo $b[0];
echo $b[1];
echo $b[2];
echo "<br>";

//associative array
$c=array('name'=>"computer",'city'=>"rajkot");

foreach($c as $v)
{
    echo $v;
}
echo "<br>";
echo $c['name'];
echo $c['city'];
echo "<br>";
print_r($c);
echo "<br>";
var_dump($c);
echo "<br>";

//multidimesional array

$d=array(array(1,2,3),array("rajkot","atmiya","u"));
for($i=0; $i<count($d); $i++)
{
    for($j=0; $j<=count($d); $j++)
    {
        echo $d[$i][$j];
    }
}
?>