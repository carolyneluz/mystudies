<?php
// Conexão com o banco de dados e consulta dos gêneros
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_library";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Falha na conexão com o banco de dados: " . $conn->connect_error);
}

$sql_genres = "SELECT id, name FROM genres";
$result_genres = $conn->query($sql_genres);

if ($result_genres->num_rows > 0) {
    while ($row_genre = $result_genres->fetch_assoc()) {
        $genre_id = $row_genre['id'];
        $genre_name = $row_genre['name'];
        echo "<a href='javascript:void(0);' onclick='showBooks($genre_id)'>$genre_name</a>";
    }
} else {
    echo "No genres found.";
}

$conn->close();
?>
