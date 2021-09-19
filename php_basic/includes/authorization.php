<?php
$login = 'login';
$password = 'password';

if ($login == $_POST['login'] && $password == $_POST['password']) {

    session_start();
    $_SESSION['login'] = $_POST['login'];
    $_SESSION['password'] = $_POST['password'];
    header($string = 'Location: ../index.php');
}