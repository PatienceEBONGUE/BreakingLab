<?php
try
{
	$bdd= new PDO('mysql:host=localhost;port=3306;dbname=website','root','samurai');
}
catch(Exception $e)
{
	die('Erreur : ' . $e->getMessage());

}

session_start();

?>

<!DOCTYPE html>
<html>
	<head>
		<title>Accueil</title>
	</head>
	
	<body>
	<p>
<?php 
	$req = $bdd->prepare('Select Login, Password from Users where Login = ? AND Password = ?');
	$req->execute(array($_POST['login'], $_POST['pass']));
	$data=$req->fetch();
	
	if($_SESSION['user']==false){
		if($data['Login'] == $_POST['login'] AND $data['Password'] == $_POST['pass']){
				$_SESSION['user']=$_POST['login'];
				echo 'Bienvenue ' . $_POST['login'] . ' !<br/>';
		}
		else{
			header('Location: login.php?mdp=error');
		}
	}
	else{
		echo 'Re-bonjour ' . $_SESSION['user'] . '<br/>';
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
