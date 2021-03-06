<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["TTR_file"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $check = getimagesize($_FILES["TTR_file"]["tmp_name"]);
  if($check !== false) {
    echo "File is an image - " . $check["mime"] . ".";
    $uploadOk = 1;
  } else {
    echo "File is not an image.";
    $uploadOk = 0;
  }
}
$path_filename_ext = $target_dir."T1.jpg";
if (file_exists($path_filename_ext)) {
    echo "Sorry, file already exists.";
    }else{
    move_uploaded_file($_FILES["TTR_file"]["tmp_name"],$path_filename_ext);
    echo "Congratulations! File Uploaded Successfully.";
    }
?>