<?php
 
/*
 * Following code will create a new product row
 * All product details are read from HTTP Post Request
 */
 
// array for JSON response
$response = array();
$myfile = fopen("testfile.txt", "a");
fwrite($myfile, $_POST['DATA']);

if (isset($_POST['DATA'])) {
 
    $name = $_POST['DATA'];
    $response["success"] = 1;
    $response["message"] = "Product successfully created.";
    $response["DATA"] = $name;
    echo json_encode($response);

} else {
    $response["success"] = 0;
    $response["message"] = "Required field(s) is missing";
 	$response["DATA"] = $name;
    echo json_encode($response);
}
?>