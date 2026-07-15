<form action="" method="get">
    Username: <input type="text" name="name"><br>
    Password: <input type="password" name="pwd"><br>
    <input type="submit" name="submit">
</form>

<?php
if(isset($_GET['submit'])) {
    $name = $_GET['name'];
    $pwd = $_GET['pwd'];
    echo $name;
    echo $pwd;
}
?>