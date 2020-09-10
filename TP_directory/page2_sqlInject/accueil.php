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
	<p>
<?php 
	$log=$_GET['login'];
	$pass=$_GET['pass'];
	$req = $bdd->query("Select Login, Password from Users where Login='$log' and Password='$pass'");
	$data=$req->fetch();
	
	if($data['Login'] AND $data['Password']){		// on vérifie si le login et le password sont bien dans la base de données
		echo 'Bienvenue ' . $data['Login'] . ' !<br/>'; 
	}
	else{
		header('Location: login.php?mdp=error');
	}	

?>	

	</p>
	<p align="center"><b>Entre un commentaire ci-dessous</b></p>
	<div align="center">
	<form name="1" action="accueil.php" method="POST">
		<input type="text" rows="5" cols="33" name="commentaire"> </input><br/>
		<input type="submit" value="Envoyer" />
	</form>

	<p>
	</div>		

	<form name="2" action="deconnexion.php?session=destroy" method="post">
		<input type="submit" value="Se déconnecter" />
	</form>
	</p>

<?php
	$r = $bdd->prepare('INSERT INTO Commentaires(login, news) VALUES(?, ?)');
	$r->execute(array($_SESSION['user'],$_POST['commentaire']));
	#$bdd->exec('INSERT INTO Commentaires(login, news) VALUES(\'shin\',\'test\')');
	if($_POST['commentaire']){
		echo 'Le commentaire a bien été rajouté.';
	}
?>
		<a href="update.php">Modifier un commentaire existant ?</a>

		</body>

<?php 
	$req->closeCursor();
	$r->closeCursor();	
?>
</html>
