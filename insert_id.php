<form action="" method="POST">  
Name:<input type="text" name="name"><br><br>
Dept:<input type="text" name="dept"><br><br>
Mob:<input type="text" name="mob"><br><br>
Dob:<input type="date" name="dob"><br><br>
<input type="submit" name="submit" value="submit">
</form>
<?php
$con=mysqli_connect("localhost","root","","university");
if(!$con)
    {
        die("connection failed");
    }
if(isset($_POST['submit']))
    {
        $name=$_POST['name'];
        $dept=$_POST['dept'];
        $mob=$_POST['mob'];
        $dob=$_POST['dob'];
        
        $qry="insert into students(name,dept,mob,dob) values('$name','$dept',$mob,'$dob')";
        if(mysqli_query($con,$qry))
        {
          $id=mysqli_insert_id($con);
          echo "record is inserted successfully";
          echo "<br>";
          echo "insert ID is".$id;
          
        }
    }
?>