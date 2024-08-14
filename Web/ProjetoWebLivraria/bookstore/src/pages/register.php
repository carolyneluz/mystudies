<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Sunflower Bookstore</title>
    <link rel="stylesheet" href="../css/auth_styles.css">
</head>
<body>
    <div class="container">
        <div class="register-form">
            <h2>Sunflower Bookstore</h2>
            <form action="../utils/register_process.php" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Register</button>
            </form>
        </div>
    </div>
</body>
</html>
