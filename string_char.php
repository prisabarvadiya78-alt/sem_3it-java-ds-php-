<?php
echo "this is test file";
echo "<br>";

echo chr(97);
echo "<br>";

echo ord("a");
echo "<br>";

echo strtolower("ATMIYA UNIVERSITY RAJKOT");
echo"<br>";

echo strtoupper("atmiya");
echo "<br>";

echo strlen("atmiya ");
echo "<br>";

$t = "  atmiya university";
echo strlen($t);
echo "<br>";

$r=trim($t);
echo strlen($r);
echo "<br>";

//ltrim or rtrim
$p=" atmiya  ";
echo strlen($p);
echo "<br>";

$k=rtrim($p);
echo strlen($k);
echo "<br>";
echo $k;
echo "<br>";

$u=ltrim($p);   
echo strlen($u);
echo "<br>";
echo $u;
echo "<br>";


echo strrev("prisa");
echo "<br>";

$e=explode("s","this is my class");
print_r($e);
echo "<br>";


$arr=array("this", "is", "my", "class");
$s=implode(" ",$arr);
print_r($s);
echo "<br>";


echo md5("atmiya");
echo "<br>";

echo "substr():<br>";
echo substr("virani collage", 0, 5);
echo "<br>";

echo "strcmp():<br>";
echo strcmp("atmiya", "atmiya");
echo "<br>";

echo "strpos():<br>";
echo strpos("Hello atmiya", "atmiya");
echo "<br>";


echo "str_replace():<br>";
echo str_replace("Nishtha", "Riya", "Hello Nishtha");
echo "<br>";

echo "join():<br>";
$a = array("PHP","Java","HTML");
echo join(" ", $a);
echo "<br>";

echo "ucfirst():<br>";
echo ucfirst("prathna");
echo "<br>";


echo "ucwords():<br>";
echo ucwords("rajkot atmiya");
echo "<br>";


echo "substr_compare():<br>";
echo substr_compare("Hello World", "World", 6);
echo "<br>";


echo "substr_count():<br>";
echo substr_count("PHP PHP Java PHP", "PHP");
echo "<br>";

?>