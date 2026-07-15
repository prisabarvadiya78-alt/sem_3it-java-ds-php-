<form action="" method="post">
    Username: <input type="text" name="name"><br>
    Password: <input type="password" name="pwd"><br>
    <input type="submit" name="submit" search="search">
</form>

<?php
if(isset($_POST['submit']))
     {
    $name = $_POST['name'];
    $pwd = $_POST['pwd'];
    echo $name ;
    echo $pwd;
}
?>