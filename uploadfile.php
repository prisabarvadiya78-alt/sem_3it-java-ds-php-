<form action="" method="POST" enctype="multipart/form-data">
    Upload File
    <input type="file" name="uploadfile">

    <input type="submit" name="upload" value="Upload">
</form>

<?php
$Target_path = "dir/";
$Target_path = $Target_path.basename($_FILES['uploadfile']['name']);

if(move_uploaded_file($_FILES['uploadfile']['tmp_name'], $Target_path))
{
    echo "File is uploaded";
    echo "<br>";
    echo $_FILES['uploadfile']['name'];
    echo "<br>";
    echo $_FILES['uploadfile']['type'];
    echo "<br>";
    echo $_FILES['uploadfile']['size'];
}
?>