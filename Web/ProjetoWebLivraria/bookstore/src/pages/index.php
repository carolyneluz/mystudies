<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

$user_type = $_SESSION['user_type'];
$username = $_SESSION['username']; // Pega o nome do usuário da sessão
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sunflower Bookstore</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        .header-icons {
            display: flex;
            align-items: center;
        }
        .header-icons span, .cart-icon a {
            margin: 0 10px;
            text-decoration: none;
        }
        .header-icons i {
            color: inherit; /* Faz com que os ícones herdem a cor do elemento pai */
        }
        .cart-icon a {
            color: white; /* Define a cor do ícone do carrinho como branco */
        }
        .cart-icon a:hover {
            color: #ccc; /* Cor ao passar o mouse sobre o ícone do carrinho */
        }
        .cart-counter {
            background-color: #007bff;
            color: white;
            border-radius: 50%;
            padding: 4px 8px;
            font-size: 12px;
            margin-left: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Welcome to <span class="title-text">Sunflower Bookstore</span></h1>
        <div class="header-icons">
            <?php if ($user_type === 'ADM'): ?>
            <div class="inventory-dropdown">
                <span><i class="fas fa-boxes"></i> Inventory</span>
                <div class="dropdown-content">
                    <a href="#" onclick="manageInventory()">Manage Inventory</a>
                    <a href="../utils/add_book.php">Add New Item</a> <!-- Link para adicionar novo livro -->
                </div>
            </div>
            <?php endif; ?>
            <div class="genres-dropdown">
                <span><i class="fas fa-bars"></i> Genres</span>
                <div class="dropdown-content">
                    <?php include '../components/genres_dropdown.php'; ?>
                </div>
            </div>
            <div class="cart-icon">
                <a href="../pages/index.php"><i class="fas fa-shopping-cart"></i> Cart <span id="cartCount" class="cart-counter">0</span></a>
            </div>
            <div class="user-dropdown">
                <span><i class="fas fa-user"></i> <?php echo $_SESSION['username']; ?></span>
                <div class="dropdown-content">
                    <a href="../utils/logout_process.php">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <div id="bookList"></div>

    <script>
        var cartCount = 0; // Inicializa o contador de itens no carrinho
        function showBooks(genre_id) {
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var books = JSON.parse(this.responseText);
                    var bookList = document.getElementById("bookList");
                    bookList.innerHTML = "";
                    books.forEach(function(book) {
                        var bookItem = document.createElement("div");
                        bookItem.className = "book-item";
                        bookItem.innerHTML = `<span>${book.title} by ${book.author}</span>
                                              <button onclick="addToCart(${book.id})"><i class="fas fa-shopping-cart"></i> Add to Cart</button>`;
                        bookList.appendChild(bookItem);
                    });
                }
            };
            xmlhttp.open("GET", "../utils/get_books.php?id=" + genre_id, true);
            xmlhttp.send();
        }

        function addToCart(bookId) {
            cartCount++; // Incrementa o contador
            document.getElementById("cartCount").textContent = cartCount; // Atualiza a exibição do contador
            alert("Book with ID " + bookId + " added to cart!");
        }

        function manageInventory() {
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var books = JSON.parse(this.responseText);
                    var bookList = document.getElementById("bookList");
                    bookList.innerHTML = "";
                    books.forEach(function(book) {
                        var bookItem = document.createElement("div");
                        bookItem.className = "book-item";
                        bookItem.innerHTML = `<span>${book.title} by ${book.author}</span>
                                              <input type="number" id="inventory_${book.id}" value="${book.inventory}" min="0">
                                              <button onclick="updateInventory(${book.id})">Update</button>
                                              <button onclick="deleteBook(${book.id})">Delete</button>`;
                        bookList.appendChild(bookItem);
                    });
                }
            };
            xmlhttp.open("GET", "../utils/get_books.php", true); // Adjust the URL as needed
            xmlhttp.send();
        }

        function updateInventory(bookId) {
            var inventoryValue = document.getElementById('inventory_' + bookId).value;
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open("POST", "../utils/update_inventory.php", true);
            xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    alert("Inventory updated for book ID " + bookId);
                }
            };
            xmlhttp.send("id=" + bookId + "&inventory=" + inventoryValue);
        }

        function deleteBook(bookId) {
            if (confirm("Are you sure you want to delete this book?")) {
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.open("POST", "../utils/delete_book.php", true);
                xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xmlhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        alert("Book with ID " + bookId + " deleted.");
                        manageInventory();
                    }
                };
                xmlhttp.send("id=" + bookId);
            }
        }
    </script>
</body>
</html>
