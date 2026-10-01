<?php
$con = mysqli_connect("localhost", "root", "","university");
if (!$con)
{
    die("Connection failed");
}
if (isset($_GET['id']))
    {
        $id = $_GET['id'];
       $qry = "DELETE FROM students WHERE id = $id";

if (mysqli_query($con, $qry)) 
    {
        header("Location: disp.php");
        exit();
        
    }
else
{
    echo "Error in deleting record ";
}
}
else
    {
       header("Location: disp.php");
       exit();
    }
mysqli_close($con);
?>
