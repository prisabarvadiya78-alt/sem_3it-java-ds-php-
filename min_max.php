
<html>
<body>
    <form action="" method="post">
        Num 1: <input type="number" name="n1"><br>
        Num 2: <input type="number" name="n2"><br>
        Num 3: <input type="number" name="n3"><br>
        <input type="submit" name="check" value="Check">
    </form>

    <?php
    if (isset($_POST['check'])) {
        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];
        $n3 = $_POST['n3'];

        echo "Maximum: ".max($n1, $n2, $n3)."<br>";
        echo "Minimum: ".min($n1, $n2, $n3);
    }
    ?>
</body>
</html>