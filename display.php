<table border="1">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>dept</th>
        <th>mob</th>
        <th>dob</th>
        <th>delete</th>
        <th>update</th>
    </tr>

<?php
$con = mysqli_connect("localhost", "root", "","university");

if (!$con)
{
    exit();
}
$qry = "SELECT * FROM students";
$result = mysqli_query($con, $qry);

if (mysqli_num_rows($result) > 0) 
    {

    $total_fields = mysqli_num_fields($result);
    $field_info = mysqli_fetch_field($result);
    while ($row = mysqli_fetch_assoc($result)) 
    {
        echo "<tr>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['name'] . "</td>";
        echo "<td>" . $row['dept'] . "</td>";
        echo "<td>" . $row['mob'] . "</td>";
        echo "<td>" . $row['dob'] . "</td>";
        
        echo "<td><a href='delete.php?id=" . $row['id'] . "'>delete</a></td>";
        echo "<td><a href='update.php?id=" . $row['id'] . "'>update</a></td>";
        echo "</tr>";
    }

}
echo "</table>";
?>