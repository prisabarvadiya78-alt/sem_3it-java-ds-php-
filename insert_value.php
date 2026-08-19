<form action="" method="POST">
<input type="text" name="name">
<input type="text" name="city">
<input type="submit" name="submit">
</form>
<?php
$con=mysqli_connect("localhost","root","","department");
if(!$con)
    {
      die("connection is not done");

    }
if(isset($_POST['submit']))
    {
      $name=$_POST['name'];
      $city=$_POST['city'];
    }
$qry="insert into info(name,city) values('$name','$city')"; 
if(mysqli_query($con,$qry))
    {
        echo "insert";
    }  
?>