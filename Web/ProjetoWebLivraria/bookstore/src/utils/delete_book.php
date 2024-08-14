<?php
require_once 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $bookId = $_POST['id'];

    $query = $connection->prepare("DELETE FROM books WHERE id = ?");
    $query->bind_param("i", $bookId);
    
    if ($query->execute()) {
        echo "Book deleted successfully.";
    } else {
        echo "Error deleting book.";
    }
}
?>
