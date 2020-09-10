<?php
try
{
	$bdd= new PDO('mysql:host=localhost;port=3306;dbname=website','root','samurai');
}
catch(Exception $e)
{
	die('Erreur : ' . $e->getMessage());

}

?>

<!DOCTYPE html>
<html>
	<head>
		<title>Accueil</title>
	</head>
	
	<body>
		<p align="center"><b>Entre ton pseudo et poste un message ci-dessous</b></p>
		<div align="center">
		<form name="1" action="accueil.php" method="GET">
			Pseudo : <input type="text" name="pseudo" value="anonymous" ></input><br/>
			Commentaire : <input type="text" rows="5" cols="33" name="commentaire"> </input><br/>
			<input type="submit" value="Envoyer" />
		</form>
		<form name="1" action="accueil.php" method="POST">
			<input type="hidden" id="custId" name="reset" value="1">
			<input type="submit" value="Reset la base de données" />
		</form>
		<br/><br/>
		
		<h2><strong><em>Minichat</em></strong></h2> </div>
		
<?php
	if($_POST['reset'] == 1){
		$bdd->exec("DELETE FROM message");
	}
	else{
		if(!$_GET['pseudo']){
			echo "Pseudo obligatoire.";
		}
		else{
			$pseud=$_GET['pseudo'];
			$com=$_GET['commentaire'];
			$bdd->exec("INSERT INTO message(pseudo,message) VALUES('$pseud','$com')");
			
			$req = $bdd->query('Select * from message ORDER BY ID DESC LIMIT 0,10');
			while($data=$req->fetch()){
				echo '<strong>' . $data['pseudo'] . '</strong> : ' . $data['message'] . '<br/><br/>';
			}
	
			$req->closeCursor();
		}
	}
?>
		
	</body>

<?php 
	$req->closeCursor();
?>
</html>
