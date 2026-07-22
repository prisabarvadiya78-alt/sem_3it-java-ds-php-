
<html>
<head>
    <style>
        .box{
            width:400px;
            background:pink;
            padding:20px;
            margin:50px auto;
            border:1px solid black;
        }

        input[type=number]{
            width:180px;
            height:30px;
            margin:5px;
        }

        input[type=submit]{
            width:100px;
            height:35px;
            background:skyblue;
            margin:5px;
        }
    </style>
</head>
<body>

<div class="box">
<form action="" method="GET">

Enter Number 1 :
<input type="number" name="num1"><br>

Enter Number 2 :
<input type="number" name="num2"><br><br>

<input type="submit" name="add" value="Add">
<input type="submit" name="sub" value="Sub"><br>
<input type="submit" name="mul" value="Mul">
<input type="submit" name="div" value="Div">

</form>

<?php
if($_SERVER["REQUEST_METHOD"]=="GET")
{
    
    if(isset($_GET['num1']) && isset($_GET['num2']))
        {
          $a = $_GET['num1'];
          $b = $_GET['num2'];

    if(isset($_GET['add']))
        echo "<h3>Answer = ".($a+$b)."</h3>";

    if(isset($_GET['sub']))
        echo "<h3>Answer = ".($a-$b)."</h3>";

    if(isset($_GET['mul']))
        echo "<h3>Answer = ".($a*$b)."</h3>";

    if(isset($_GET['div']))
    {
        if($b!=0)
            echo "<h3>Answer = ".($a/$b)."</h3>";
        else
            echo "<h3>Division by Zero Not Allowed</h3>";
    }
}
}
?>

</div>

</body>
</html>