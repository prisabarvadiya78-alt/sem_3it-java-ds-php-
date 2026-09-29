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
    
    if (mysqli_multi_query($con, $qry))
         {

        
                   $last_id = mysqli_insert_id($con);
                   echo "Inserted successfully! ID: " . $last_id . "<br><br>";

                   $result = mysqli_query($con, "SELECT * FROM students");
 
                   while ($row = mysqli_fetch_row($result)) 
        {
                echo "ID: " . $row[0] . "<br>";
                echo "Name: " . $row[1] . "<br>";
                echo "Dept: " . $row[2] . "<br>";
                echo "mob: " . $row[3] . "<br>"; 
                echo "dob: " . $row[4] . "<br><br>";
        }

        mysqli_free_result($result);
    } 
    else 
    {
        echo "Error: " . mysqli_error($con);
    }
}
?>