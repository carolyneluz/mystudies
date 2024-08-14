-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 07/07/2024 às 21:47
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_library`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `publication_year` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  `inventory` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `books`
--

INSERT INTO `books` (`id`, `title`, `author`, `publication_year`, `genre_id`, `inventory`) VALUES
(1, '1984', 'George Orwell', 1949, 1, 5),
(2, 'Animal Farm', 'George Orwell', 1945, 1, 0),
(3, 'The Lord of the Rings', 'J.R.R. Tolkien', 1954, 3, 0),
(4, 'The Hobbit', 'J.R.R. Tolkien', 1937, 3, 0),
(5, 'Alice\'s Adventures in Wonderland', 'Lewis Carroll', 1865, 5, 0),
(6, 'Pride and Prejudice', 'Jane Austen', 1813, 5, 0),
(7, 'To Kill a Mockingbird', 'Harper Lee', 1960, 1, 0),
(8, 'Brave New World', 'Aldous Huxley', 1932, 4, 0),
(9, 'Fahrenheit 451', 'Ray Bradbury', 1953, 4, 0),
(11, 'Sapiens: A Brief History of Humankind ', 'Yuval Noah Harari', 2011, 2, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `genres`
--

CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(1, 'Fiction'),
(2, 'Non-Fiction'),
(3, 'Fantasy'),
(4, 'Science Fiction'),
(5, 'Classic Literature');

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `user_type` enum('COM','ADM') NOT NULL DEFAULT 'COM',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `user_type`, `created_at`) VALUES
(3, 'Carolyne', '$2y$10$d3.8jLv2FcKGYoeDMj2xiuhwPzUk2RIti.NzrWKgtHmMw.KTpjFnK', 'carolyne@mail.com', 'ADM', '2024-07-07 19:23:58');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `genre_id` (`genre_id`);

--
-- Índices de tabela `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
