<?php
#no argument simple program
function abc()
{
   echo "hello,php program!";
}
abc();



#call by value
echo "<br>";
function add($num)
{
   $num+=10;
   echo $num;
}
$p=2;
add($p);
echo "<br>";
echo $p; $z;



#call by reference
echo "<br>";
function sum($x,$y)
{
   $z=$x+$y;
   return $z;
}
echo sum(10,20);


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

#variable function
echo "<br>";
function name($test)
{
   echo $test;
}
$k="name";
$k("your name is kangna");


#array index
$students=array("prisa","prathna","kangna","kruti","nensi");
echo "students:<br>";
echo $students[0]."<br>";
echo $students[1]."<br>";
echo $students[2]."<br>";
echo $students[3]."<br>";
echo $students[4]."<br>";


#show type of value
$x=array(10,"atmiya",20.5);
echo $x[0];
echo $x[1];
echo $x[2];
echo "<br>";
print_r($x);
echo "<br>";
var_dump($x);


?>
