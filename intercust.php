<?php
$con=mysqli_connect("db.soic.indiana.edu","i308s18_cfm2","Disney_World", "i308s18_cfm2");


if (! $con)
	{die("Failed to connect to MySQL: " .mysqli_connect_error() ); }
else 
	{ echo "Established Database Connection" ;}
	
$var_cname = $_POST['cname'];
$var_addr = $_POST['address'];
$var_phone = $_POST['phone'];
$sql = "INSERT INTO customer (name, address, phone) VALUES ('$var_cname', '$var_addr','$var_phone')";
if (mysqli_query($con, $sql)) {
echo "One record added!";
} else {
die('SQL Error: ' . mysqli_error($con));
}

?>
