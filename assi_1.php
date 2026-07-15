<?php
echo "<table border='1' cellpadding='10'>";
for($i=1;$i<=5;$i++)
{
    echo "<tr>";
    for($j=1;$j<=5;$j++)
    {
        echo "<td>Row $i Col $j</td>";
    }
    echo "</tr>";
}
echo "</table>";
?>