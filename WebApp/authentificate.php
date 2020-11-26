<?php

$query = "SELECT * FROM user WHERE username='admin' AND password='admin'";

$command = escapeshellcmd('python test.py '. $query);
$output = shell_exec($command);
echo $output;


?>