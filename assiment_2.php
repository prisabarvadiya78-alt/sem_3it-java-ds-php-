
<?php
#1.simple function
function calculate($a, $b) 
{
    echo "<br>";
    echo "Add: " . ($a + $b);
    echo "<br>";
    echo "Subtract: " . ($a - $b);
    echo "<br>";
    echo "Multiply: " . ($a * $b);
     echo "<br>";
    echo "Divide: " . ($b != 0 ? $a / $b : "Cannot divide by zero");
     echo "<br>";
}
calculate(10, 5);
echo "<br>";

#2.function with arguments and return values
function calculateRectangleArea($l, $w)
{
    $area = $l * $w;
    return "A rectangle of length $l and width $w has an area of $area.";
}
echo calculateRectangleArea(40, 5);
echo "<br><br>";


#3.function with arguments,no return value
function RectangleArea($l, $w)
{
    $area = $l * $w;
    echo "A rectangle of length $l and width $w has an area of $area.";
}
RectangleArea(100, 5);
echo "<br><br>";

#4.function with arguments
function checkVotingEligibility($age) {
    if ($age >= 18) {
        echo "You are eligible to vote.";
    } else {
        echo "You are not eligible to vote.";
    }
}

checkVotingEligibility(22); 
echo "<br>";
checkVotingEligibility(15);
echo "<br><br>";



#array:1.indexed array
$a = array(0, 1, 2, 3, 4);
echo $a[3]; 
echo "<br><br>";

//6.assosative array
$a = array(
    "zero"  => 0, 
    "one"   => 1, 
    "two"   => 2, 
    "three" => 3, 
    "four"  => 4
);
echo $a["three"]; 
echo "<br><br>";



#7.assocative array
$location = array(
    "Japan" => "Tokyo",
    "Mexico" => "Mexico City",
    "USA" => "New York City",
    "India" => "Mumbai",
    "Korea" => "Seoul",
    "China" => "Shanghai",
    "Nigeria" => "Lagos",
    "Argentina" => "Buenos Aires",
    "Egypt" => "Cairo",
    "England" => "London"
);

foreach ($location as $country => $city)
{
    echo "$city is in $country.<br>";
}
echo "<br><br>";


#8.indexed/Numeric array
$colleges = array('Atmiya', 'Christ', 'DDIT', 'ROLLWALA', 'Marwadi', 'RK');

foreach ($colleges as $college) {
    echo $college . "<br>";
}


#9.Normal Array
$color = array('white', 'green', 'red');
echo implode(', ', $color) . "<br><br>";
echo "<ul>";
foreach ($color as $c)
{
    echo "<li>$c</li>";
}
echo "</ul>";
echo "<br><br>";

#10. MultiDimensional Array Declaration
$marks = array(
    "Bipin" => array(
        "Maths" => 45,
        "Physics" => 40,
        "Chemistry" => 42
    ),
    "Ravi" => array(
        "Maths" => 40,
        "Physics" => 40,
        "Chemistry" => 40
    ),
    "amit" => array(
        "Maths" => 50,
        "Physics" => 45,
        "Chemistry" => 48
    )
);

// Given printing statements from question
echo "Marks for Bipin in Maths : ";
echo $marks['Bipin']['Maths']."<br>";

echo "Marks for Bhavik in Physics : ";
echo $marks['Ravi']['Physics']."<br>";

echo "Marks for Amit in Chemistry : ";
echo $marks['amit']['Chemistry']."<br>";

echo "<pre>";

print_r($marks);

echo "</pre>";

?>
