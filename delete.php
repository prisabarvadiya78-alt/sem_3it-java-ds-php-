<?php
$con = mysqli_connect("localhost", "root", "","university");

if (!$con) 
{
    exit();
}
$id = $_GET['id'];
$qry = "DELETE FROM students WHERE id =$id";

if (mysqli_query($con, $qry)) 
    {
        echo "record is delete";
    } 


else
{
   echo "error in deleting";
}

?>