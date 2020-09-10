<?php session_start();?>

<!DOCTYPE>

<html>

	<head>
		<title>Page</title>
	</head>

	<body>
<?php	
	session_destroy();
	header('Location: login.php');
?>



	</body>

</html>
