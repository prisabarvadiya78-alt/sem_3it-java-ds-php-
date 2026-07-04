<?php
$dept=array('name'=>"computer",'city'=>"rajkot",1,2,3);
  
echo $dept['name'];
echo "<br>";
echo $dept['city'];
echo "<br>";

var_dump($dept);
foreach($dept as $v)
{
  echo $v;
}
?>