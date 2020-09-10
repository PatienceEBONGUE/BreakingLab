<?php session_start(); 
		$bdd = new PDO('mysql:host=localhost;port=3306;dbname=website','root','samurai');

?>

<!DOCTYPE>

<html>

	<head>
		<title>Page</title>
	</head>
	
	<body>
		
		<h3> Modifier un commentaire </h3>
		<form action="update.php" method="post">
			Numéro du commentaire :<input type="text" name="num"/><br/>
			Nouveau commentaire : <input type="text" name="new"><br/>
			<input type="submit" value="Changer"/>
		</form>

		<br/>
		<h3>Supprimer un commentaire </h3>
		<form action="update.php" method="post">
			Numéro du commentaire : <input type="text" name="del"/><br/>
			<input type="submit" value="Delete"/>
		</form>

		<a href="accueil.php">Revenir à l'accueil</a><br/>
<?php
	if($_POST['num'] and $_POST['new']){
		echo "Changement effectué";	
		$req = $bdd->prepare('UPDATE Commentaires SET news = ? where ID = ?');
		$req->execute(array($_POST['new'],$_POST['num']));
	}
	
	if($_POST['del']){
		echo "Commentaire supprimé.";
		$req = $bdd->prepare('DELETE FROM Commentaires WHERE ID = ?');
		$req->execute(array($_POST['del']));
	}
	
	$req->closeCursor();
?>

	</body>

</html>
