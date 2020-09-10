<?php
   define('DB_SERVER', 'localhost');
   define('DB_USERNAME', 'root');
   define('DB_PASSWORD', 'IMT-fipa-BreakingLab');
   define('DB_DATABASE', 'website');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
     //$db = new PDO('mysql:host=127.0.0.1;dbname=website', 'IMT-fipa-BreakingLab', '');

  session_start();
   if($_SERVER["REQUEST_METHOD"] == "POST") {
      // username and password sent from form

     // $myusername = mysqli_real_escape_string($db,$_POST['username']);
     // $mypassword = mysqli_real_escape_string($db,$_POST['password']);

     $myusername =$_POST['username'];
     $mypassword =$_POST['password'];

      $sql = "SELECT user FROM users WHERE username = '$myusername' and password = '$mypassword'";
      $result = mysqli_query($db,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      $active = $row['active'];

      $count = mysqli_num_rows($result);

      // If result matched $myusername and $mypassword, table row must be 1 row

      if($count == 1) {
         session_register("myusername");
         $_SESSION['login_user'] = $myusername;

         header("location: welcome.php");
      }else {
         $error = "Your Login Name or Password is invalid";
      }
   }
?>

