<form action="" method="post">
    Username: <input type="text" name="name"><br>
    Password: <input type="password" name="pwd"><br>
    <input type="submit" name="submit" value="search">
</form>

<?php
$arr=array("jay","kangna","raj","kruti");
if(isset($_POST['submit']))
     {
    $name = $_POST['name'];
    if(in_array($name,$arr))
        {
            echo "Record Found";
        }
    else
        {
            echo "Record Not Found";
        }
}
?>