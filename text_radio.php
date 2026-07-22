
<html>
<body>
     <form action="" method="GET">
        
        <label>Enter Text:</label><br>
        <input type="text" name="text" required><br><br>

        <label>Select Font:</label><br>
        <input type="radio" name="font" value="Arial" checked> Arial<br>
        <input type="radio" name="font" value="Courier New"> Courier New<br>
        <input type="radio" name="font" value="Times New Roman"> Times New Roman<br><br>

        <label>Select Color:</label><br>
        <input type="color" name="color" value="#000000"><br><br>
        <input type="submit" name="submit" value="Display Text">
    </form>

    <hr>

    
    <?php
    if (isset($_GET['submit'])) {
        $text = $_GET['text'];
        $font = $_GET['font'];
        $color = $_GET['color'];

        echo "<p style='font-family: $font; color: $color; font-size: 24px;'>$text</p>";
    }
    ?>
</body>
</html>