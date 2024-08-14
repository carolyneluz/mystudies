<?php
require_once 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $book_id = intval($_POST['id']);
    $inventory = intval($_POST['inventory']);

    $query = $connection->prepare("UPDATE books SET inventory = ? WHERE id = ?");
    $query->bind_param("ii", $inventory, $book_id);
    if ($query->execute()) {
        echo "Inventory updated successfully.";
    } else {
        echo "Error updating inventory.";
    }
    $query->close();
}
$connection->close();
?>
