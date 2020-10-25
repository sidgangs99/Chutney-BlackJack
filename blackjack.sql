-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2020 at 01:53 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blackjack`
--

-- --------------------------------------------------------

--
-- Table structure for table `computer_hand`
--

CREATE TABLE `computer_hand` (
  `id` int(10) NOT NULL,
  `card` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `deck`
--

CREATE TABLE `deck` (
  `id` int(10) NOT NULL,
  `card` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `deck`
--

INSERT INTO `deck` (`id`, `card`) VALUES
(5435, 'K'),
(5436, '4'),
(5437, '6'),
(5438, '9'),
(5439, '6'),
(5440, '3'),
(5441, '8'),
(5442, 'K'),
(5443, '2'),
(5444, 'K'),
(5445, '8'),
(5446, '2'),
(5447, '9'),
(5448, '3'),
(5449, 'Ace'),
(5450, 'J'),
(5451, '7'),
(5452, 'Ace'),
(5453, '4'),
(5454, 'Ace'),
(5455, '7'),
(5456, '7'),
(5457, '6'),
(5458, '8'),
(5459, '8'),
(5460, 'J'),
(5461, '4'),
(5462, '2'),
(5463, 'Q'),
(5464, '9'),
(5465, 'J'),
(5466, '3'),
(5467, '7'),
(5468, 'J'),
(5469, '3'),
(5470, '4'),
(5471, 'Q'),
(5472, '2'),
(5473, 'K'),
(5474, '9'),
(5475, 'Q'),
(5476, 'Ace');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `chips` int(10) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `chips`, `password`) VALUES
(1, 'q', 12, '7694f4a66316e53c8cdd9d9954bd611d'),
(3, 'a', 259, '0cc175b9c0f1b6a831c399e269772661'),
(6, 'Yath', 2000, '415290769594460e2e485922904f345d');

-- --------------------------------------------------------

--
-- Table structure for table `user_hand`
--

CREATE TABLE `user_hand` (
  `id` int(10) NOT NULL,
  `card` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_hand`
--

INSERT INTO `user_hand` (`id`, `card`) VALUES
(333, 'Q');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `computer_hand`
--
ALTER TABLE `computer_hand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_hand`
--
ALTER TABLE `user_hand`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `computer_hand`
--
ALTER TABLE `computer_hand`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=305;

--
-- AUTO_INCREMENT for table `deck`
--
ALTER TABLE `deck`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5477;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_hand`
--
ALTER TABLE `user_hand`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=334;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
