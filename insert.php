<form action="" method="POST">
    name:<input type="text" name="name"><br><br>
    dept:<input type="text" name="dept"><br><br>
    mobile_no:<input type="text" name="mob"><br><br>
    dob:<input type="date" name="dob"><br><br>
    submit:<input type="submit" name="submit" value="submit"><br><br>
</form>

<?php
$con = mysqli_connect("localhost", "root", "","university");

if (!$con)
{
    die("connection is not done");
}

if (isset($_POST['submit'])) {

    $name = $_POST['name'];
    $dept = $_POST['dept'];
    $mob  = $_POST['mob'];
    $dob = $_POST['dob'];

    $qry = "INSERT INTO students(name, dept, mob, dob) VALUES('$name', '$dept', $mob,'$dob')";
    
    if (mysqli_query($con, $qry))
         {

        
             echo "insert";
}
?>