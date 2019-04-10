-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 10, 2019 at 10:07 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `sfusername` varchar(20) NOT NULL,
  `sfpassword` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`sfusername`, `sfpassword`) VALUES
('pmauser', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `FirstN` varchar(10) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `LastN` varchar(10) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Phone` int(8) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `comming_date` date NOT NULL,
  `upcomming_booking` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`FirstN`, `LastN`, `Gender`, `Phone`, `Email`, `username`, `password`, `comming_date`, `upcomming_booking`) VALUES
('Poon', 'man', 'M', 51105554, 'Pandaericassignment@gmail.com', 'pandaericpoom', 'Pandaeric0261', '2019-11-20', 'A02');

-- --------------------------------------------------------

--
-- Table structure for table `house`
--

CREATE TABLE `house` (
  `house_id` varchar(10) NOT NULL,
  `avaliable` varchar(10) NOT NULL,
  `bedroom` int(10) NOT NULL,
  `common_spaces` int(10) NOT NULL,
  `washroom` int(10) NOT NULL,
  `booking_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `house`
--

INSERT INTO `house` (`house_id`, `avaliable`, `bedroom`, `common_spaces`, `washroom`, `booking_no`) VALUES
('A01', 'now', 1, 1, 1, 0),
('A02', 'not', 1, 0, 1, 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
