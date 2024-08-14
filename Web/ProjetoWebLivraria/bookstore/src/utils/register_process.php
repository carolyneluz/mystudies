<?php
session_start();
require_once 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $email = $_POST['email'];

    $query = $connection->prepare("SELECT * FROM users WHERE username = ? OR email = ?");
    $query->bind_param("ss", $username, $email);
    $query->execute();
    $result = $query->get_result();

    if ($result->num_rows > 0) {
        echo "Username or email already exists.";
    } else {
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        $insert_query = $connection->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
        $insert_query->bind_param("sss", $username, $hashed_password, $email);

        if ($insert_query->execute()) {
            echo "Registration successful. <a href='../pages/login.php'>Login here</a>";
        } else {
            echo "Error: " . $insert_query->error;
        }
    }
}
?>
