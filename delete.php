<?php

$conn = mysqli_connect("localhost", "root", "", "student");

if (!$conn) {
    die("Connection failed");
}

if (isset($_GET['id'])) {

    $id = $_GET['id'];

    $sql = "DELETE FROM information WHERE id = $id";

    if (mysqli_query($conn, $sql)) {
        echo "Record deleted successfully";
    } else {
        echo "Error: " . mysqli_error($conn);
    }

} else {
    echo "ID not found";
}

?>