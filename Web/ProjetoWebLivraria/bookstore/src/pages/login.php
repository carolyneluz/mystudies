<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Sunflower Bookstore</title>
    <link rel="stylesheet" href="../css/auth_styles.css">
</head>
<body>
    <div class="container">
        <div class="login-form">
            <h2><img src="https://shorturl.at/JFtBP" alt="Imagem"></h2>
            <form action="../utils/login_process.php" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <button type="submit">Login</button>
            </form>
            <p>Don't have an account? <a href="register.php">Register here</a></p>
        </div>
    </div>
</body>
</html>
