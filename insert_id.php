<form action="" method="post">
Name: <input type="text" name="name"> 
City: <input type="text" name="city">
<input type="submit" name="submit" value="Submit">
</form>
<?php
$con = mysqli_connect("localhost", "root", "", "department");
if (!$con)
{
    die("Connection failed");
}
if (isset($_POST['submit']))
{
    $name = $_POST['name'];
    $city = $_POST['city'];

    $qry = "insert into info (name, city) values ('$name', '$city')";
    if (mysqli_query($con, $qry))
    {
        $id = mysqli_insert_id($con);
        echo "Your record is inserted successfully";
        echo "<br>";
        echo "Inserted ID is " . $id;
    
    }
}
?>