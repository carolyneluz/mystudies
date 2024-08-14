<?php
require_once 'db_connect.php';

if (isset($_GET['id'])) {
    $genre_id = intval($_GET['id']);
    $sql_books = "SELECT id, title, author, inventory FROM books WHERE genre_id = ?";
    $stmt = $connection->prepare($sql_books);
    $stmt->bind_param("i", $genre_id);
} else {
    $sql_books = "SELECT id, title, author, inventory FROM books";
    $stmt = $connection->prepare($sql_books);
}
$stmt->execute();
$result_books = $stmt->get_result();

$books = array();
if ($result_books->num_rows > 0) {
    while ($row_book = $result_books->fetch_assoc()) {
        $books[] = $row_book;
    }
}

$stmt->close();
$connection->close();

header('Content-Type: application/json');
echo json_encode($books);
?>
