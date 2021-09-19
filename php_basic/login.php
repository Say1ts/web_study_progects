<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<?php

    session_start();

    $login = 'login';
    $password = 'password';
    if ($_SESSION['login'] == $login && $_SESSION['password'] == $password) {
    header($string = 'Location: ../index.php');
}
?>
<body>
    <h1> Вход в аккаунт</h1>
    <form action="includes/authorization.php" method="post">
        Введите логин <input type="text" name="login"> <br>
        Введите пароль <input type="password" name="password"> <br>
        <button> Войти </button><br>
    </form>
    <a href="registration.php"> Регистрация</a>

</body>
</html>
