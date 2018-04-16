-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2018 at 09:45 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account table`
--

CREATE TABLE `account table` (
  `account_id` int(20) NOT NULL,
  `account_type` varchar(10) NOT NULL,
  `Amount` int(20) NOT NULL,
  `Interest_rate` float NOT NULL,
  `timecheck` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerid` int(20) NOT NULL,
  `account_id` int(20) NOT NULL,
  `account_type` int(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `maintable`
--

CREATE TABLE `maintable` (
  `sno` int(20) NOT NULL,
  `name` varchar(35) NOT NULL,
  `mail` varchar(35) NOT NULL,
  `password` varchar(35) NOT NULL,
  `checkin` int(25) NOT NULL,
  `customer id` int(20) NOT NULL,
  `aadhar` int(16) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `maintable`
--

INSERT INTO `maintable` (`sno`, `name`, `mail`, `password`, `checkin`, `customer id`, `aadhar`) VALUES
(1, 'praveen', 'prav@gmail.com', 'praveen', 0, 100001, 123456789);

-- --------------------------------------------------------

--
-- Table structure for table `transcation table`
--

CREATE TABLE `transcation table` (
  `transcation_id` int(20) NOT NULL,
  `account_id` int(20) NOT NULL,
  `amount` int(20) NOT NULL,
  `ToAccount` int(20) NOT NULL,
  `time` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `type-lookup`
--

CREATE TABLE `type-lookup` (
  `name` varchar(20) NOT NULL,
  `account_type` int(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `type-lookup`
--

INSERT INTO `type-lookup` (`name`, `account_type`) VALUES
('saving', 1),
('current', 2),
('loan', 3),
('fixed', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account table`
--
ALTER TABLE `account table`
  ADD PRIMARY KEY (`account_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerid`);

--
-- Indexes for table `maintable`
--
ALTER TABLE `maintable`
  ADD PRIMARY KEY (`sno`,`customer id`);

--
-- Indexes for table `transcation table`
--
ALTER TABLE `transcation table`
  ADD PRIMARY KEY (`transcation_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `maintable`
--
ALTER TABLE `maintable`
  MODIFY `sno` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `transcation table`
--
ALTER TABLE `transcation table`
  MODIFY `transcation_id` int(20) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
