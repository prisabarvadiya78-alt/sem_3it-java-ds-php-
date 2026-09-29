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
        if (mysqli_affected_rows($con) > 0)
    {
        echo "record is delete";
    } 
    else
    {
        echo "record is not available";
    }
}
else
{
   echo "error in deleting";
}

?>