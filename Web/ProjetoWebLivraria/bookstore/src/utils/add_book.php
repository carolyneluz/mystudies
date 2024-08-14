<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    require_once '../utils/db_connect.php';

    $title = $_POST['title'];
    $author = $_POST['author'];
    $publication_year = $_POST['publication_year'];
    $genre_id = $_POST['genre_id'];
    $inventory = $_POST['inventory'];

    $query = $connection->prepare("INSERT INTO books (title, author, publication_year, genre_id, inventory) VALUES (?, ?, ?, ?, ?)");
    $query->bind_param("sssii", $title, $author, $publication_year, $genre_id, $inventory);

    $response = array();

    if ($query->execute()) {
        $response['status'] = 'success';
        $response['message'] = 'Book added successfully.';
        $response['book'] = array(
            'title' => $title,
            'author' => $author,
            'inventory' => $inventory
        );
    } else {
        $response['status'] = 'error';
        $response['message'] = 'Error adding book.';
    }

    echo json_encode($response);

    $query->close();
    $connection->close();
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Book</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <div class="header">
        <h1>Add New Book</h1>
        <div class="header-icons">
            <div class="genres-dropdown">
                <span><i class="fas fa-bars"></i> Genres</span>
                <div class="dropdown-content">
                    <?php include '../components/genres_dropdown.php'; ?>
                </div>
            </div>
            <div class="user-dropdown">
                <span><i class="fas fa-user"></i> <?php echo $_SESSION['username']; ?></span>
                <div class="dropdown-content">
                    <a href="../utils/logout_process.php">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <div class="form-container">
        <form id="addBookForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <label for="title">Title:</label><br>
            <input type="text" id="title" name="title" required><br><br>

            <label for="author">Author:</label><br>
            <input type="text" id="author" name="author" required><br><br>

            <label for="publication_year">Publication Year:</label><br>
            <input type="number" id="publication_year" name="publication_year"><br><br>

            <label for="genre_id">Genre ID:</label><br>
            <input type="number" id="genre_id" name="genre_id"><br><br>

            <label for="inventory">Inventory:</label><br>
            <input type="number" id="inventory" name="inventory" value="0" min="0"><br><br>

            <input type="submit" value="Add Book">
        </form>
    </div>

    <script>
        document.getElementById('addBookForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            var formData = new FormData(this); // Create FormData object from form
            var xmlhttp = new XMLHttpRequest();

            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var response = JSON.parse(this.responseText);
                    
                    if (response.status === 'success') {
                        alert(response.message);

                        // Optionally, you can update the book list on the index page here
                        // Example: showBooks(genre_id); // Call the function to update book list
                    } else {
                        alert(response.message);
                    }
                }
            };

            xmlhttp.open("POST", "<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>", true);
            xmlhttp.send(formData);
        });
    </script>
</body>
</html>
