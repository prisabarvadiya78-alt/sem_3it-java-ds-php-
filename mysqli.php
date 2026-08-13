<?php
$con = mysqli_connect("localhost", "root", "","test");
if (!$con)
     {
  
    echo "Connection is not done",mysqli_connect_error();
    
     } 
else
     {
    
        echo "The connection is done";
        echo "<br>";
        var_dump($con);
}
mysqli_close($con);
echo "<br>";

$conn = mysqli_connect("localhost", "root", "");
if (!$conn) 
{
    echo "connection is not done".mysqli_error();
} 
mysqli_select_db($conn,"mysql");
    echo "Database is selected";
if(mysqli_connect_errno())
    {
        echo "error number:".mysqli_connect_errno();
        echo "<br>";
        echo "error message:".mysqli_connect_errno();
    }
?>