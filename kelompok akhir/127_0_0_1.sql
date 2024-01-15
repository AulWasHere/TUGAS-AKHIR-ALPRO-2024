-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Jan 2024 pada 18.09
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kelompok`
--
CREATE DATABASE IF NOT EXISTS `kelompok` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
USE `kelompok`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `history_deleted`
--

CREATE TABLE `history_deleted` (
  `id` int(11) NOT NULL,
  `nama_barang` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `jumlah` int(11) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data untuk tabel `history_deleted`
--

INSERT INTO `history_deleted` (`id`, `nama_barang`, `jumlah`, `harga`) VALUES
(1, 'awm', 12, 12000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `stok_barang`
--

CREATE TABLE `stok_barang` (
  `id` int(10) NOT NULL,
  `nama_barang` text NOT NULL,
  `jumlah` int(10) NOT NULL,
  `harga` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data untuk tabel `stok_barang`
--

INSERT INTO `stok_barang` (`id`, `nama_barang`, `jumlah`, `harga`) VALUES
(2, 'klo', 56656, 56000),
(3, 'yuc', 23, 120),
(4, '5', 12, 12000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `history_deleted`
--
ALTER TABLE `history_deleted`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `stok_barang`
--
ALTER TABLE `stok_barang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `stok_barang`
--
ALTER TABLE `stok_barang`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
