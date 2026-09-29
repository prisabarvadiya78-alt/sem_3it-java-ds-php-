<?php
$con = mysqli_connect("localhost", "root", "","university");

if (!$con) 
{
    die ("database connnection failed");
}
$id = $_GET['id'];
$qry = "select * from students WHERE id=$id";
$result=mysqli_query($con,$qry);
if (mysqli_num_rows($result) == 0)
    { 
        echo "record not available";
        exit();
    }
$row=mysqli_fetch_assoc($result);
?>
    
<form action="" method="POST">
    id: <input type="text" name="id" value="<?php echo $row['id']; ?>"><br><br>
    Name: <input type="text" name="name" value="<?php echo $row['name']; ?>"><br><br>
    dept: <input type="text" name="dept" value="<?php echo $row['dept']; ?>"><br><br>
    mob: <input type="text" name="mob" value="<?php echo $row['mob']; ?>"><br><br>
    date: <input type="date" name="dob" value="<?php echo $row['dob']; ?>"><br><br>
    <input type="submit" name="update" value="Update Record">
</form>

<?php
if(isset($_POST['update']))
    {
        $id=$_POST['id'];
        $name=$_POST['name'];
        $dept=$_POST['dept'];
        $mob=$_POST['mob'];
        $dob=$_POST['dob'];
       $qry = "UPDATE students SET name='$name', dept='$dept',mob=$mob,dob='$dob' WHERE id=$id"; 
       if(mysqli_affected_rows($con) > 0)
   {
        if(mysqli_query($con,$qry))
            {
                echo "record updated successfully";
            }
         else
            {
                echo "error updating record";
            }   
    }
    else
        {
            echo "error updating record";
        }
    }
?>