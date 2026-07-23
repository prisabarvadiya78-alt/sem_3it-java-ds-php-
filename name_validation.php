<?php
$name = "Priya";
if (preg_match("/^[a-zA-Z]+$/", $name))
{
    echo "Valid Name";
}
else
{
    echo "Invalid Name";
}
?>