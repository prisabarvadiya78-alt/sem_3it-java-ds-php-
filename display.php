

<table border="1">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>city</th>
    </tr>

<?php
$com = mysqli_connect("localhost", "root", "", "department");

if (!$com)
{
    die("not");
}

$query = "select * from info";
$result = mysqli_query($com, $query);

if (mysqli_num_rows($result) > 0)
{
    while ($row = mysqli_fetch_assoc($result))
    {
        echo "<tr>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['name'] . "</td>";
        echo "<td>" . $row['city'] . "</td>";
        echo "</tr>";
    }
}

echo "</table>";
?>