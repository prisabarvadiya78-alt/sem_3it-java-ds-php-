<?php

$amount=2500;

if($amount>2000)
{
    $discount=$amount*15/100;
}
elseif($amount>1000)
{
    $discount=$amount*10/100;
}
elseif($amount>500)
{
    $discount=$amount*5/100;
}
else
{
    $discount=0;
}

$final=$amount-$discount;

echo "Purchase Amount : ".$amount."<br>";
echo "Discount : ".$discount."<br>";
echo "Final Bill : ".$final;

?>