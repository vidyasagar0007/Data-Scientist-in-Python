-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: banking_database
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `banking_database`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `banking_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `banking_database`;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `account_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `branch_id` int NOT NULL,
  `account_number` varchar(20) NOT NULL,
  `account_type` varchar(30) NOT NULL,
  `balance` decimal(15,2) DEFAULT '0.00',
  `minimum_balance` decimal(15,2) DEFAULT '0.00',
  `opened_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `currency` varchar(10) DEFAULT 'INR',
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `account_number` (`account_number`),
  KEY `customer_id` (`customer_id`),
  KEY `branch_id` (`branch_id`),
  CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `accounts_ibfk_2` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,1,1,'ACT1001','Savings',55000.00,1000.00,'2018-01-15','Active','INR'),(2,2,3,'ACT1002','Current',125000.00,5000.00,'2019-03-20','Active','INR'),(3,3,5,'ACT1003','Savings',1200.00,1000.00,'2020-08-01','Active','INR'),(4,4,1,'ACT1004','Savings',0.00,1000.00,'2021-11-10','Closed','INR'),(5,5,3,'ACT1005','Fixed Deposit',500000.00,0.00,'2017-06-01','Active','INR');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beneficiaries`
--

DROP TABLE IF EXISTS `beneficiaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beneficiaries` (
  `beneficiary_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `beneficiary_name` varchar(100) NOT NULL,
  `account_number` varchar(30) NOT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `ifsc_code` varchar(20) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `added_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`beneficiary_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `beneficiaries_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beneficiaries`
--

LOCK TABLES `beneficiaries` WRITE;
/*!40000 ALTER TABLE `beneficiaries` DISABLE KEYS */;
INSERT INTO `beneficiaries` VALUES (1,1,'Rohit Singh','BEN10001','HDFC Bank','HDFC0005678','Rohit','2026-08-01','Active'),(2,2,'Neha Verma','BEN10002','ICICI Bank','ICIC0009101','Neha','2026-08-05','Active'),(3,3,'Aman Gupta','BEN10003','Axis Bank','AXIS0003344','Aman','2026-08-10','Active'),(4,4,'Karan Sharma','BEN10004','State Bank of India','SBIN0001234','Karan','2026-08-15','Active'),(5,5,'Sneha Patel','BEN10005','Canara Bank','CNRB0001122','Sneha','2026-08-20','Active');
/*!40000 ALTER TABLE `beneficiaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branches` (
  `branch_id` int NOT NULL,
  `branch_code` varchar(10) NOT NULL,
  `branch_name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `manager_name` varchar(100) DEFAULT NULL,
  `opening_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`branch_id`),
  UNIQUE KEY `branch_code` (`branch_code`),
  UNIQUE KEY `ifsc_code` (`ifsc_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
INSERT INTO `branches` VALUES (1,'BR001','SBI CP','New Delhi','Delhi','110001','CP','SBIN0001234','01123456789','R. Kumar','2015-06-12','Active'),(2,'BR002','HDFC Bandra','Mumbai','Maharashtra','400050','Linking Rd','HDFC0005678','02298765432','P. Sharma','2018-09-20','Closed'),(3,'BR003','ICICI Bank','Kolkata','West Bengal','700016','Park St','ICIC0009101','03344556677','A. Banerjee','2019-01-15','Active'),(4,'BR004','Canara Bank','Chennai','Tamil Nadu','600002','Anna Salai','CNRB0001122','04433221144','K. Raman','2020-11-05','Closed'),(5,'BR005','Axis Bank','Bengaluru','Karnataka','560001','MG Road','AXIS0003344','08022334455','S. Reddy','2021-03-18','Active');
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `card_transactions`
--

DROP TABLE IF EXISTS `card_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card_transactions` (
  `card_transaction_id` bigint NOT NULL,
  `card_id` int NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `merchant_name` varchar(100) DEFAULT NULL,
  `merchant_category` varchar(50) DEFAULT NULL,
  `transaction_date` datetime DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `transaction_status` varchar(20) DEFAULT NULL,
  `reference_number` varchar(50) DEFAULT NULL,
  `payment_channel` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`card_transaction_id`),
  KEY `card_id` (`card_id`),
  CONSTRAINT `card_transactions_ibfk_1` FOREIGN KEY (`card_id`) REFERENCES `cards` (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_transactions`
--

LOCK TABLES `card_transactions` WRITE;
/*!40000 ALTER TABLE `card_transactions` DISABLE KEYS */;
INSERT INTO `card_transactions` VALUES (1,1,2500.00,'Amazon','Online Shopping','2026-09-01 12:15:00','New Delhi','Success','CARDREF10001','Online'),(2,2,4500.00,'Flipkart','Online Shopping','2026-09-02 15:30:00','Mumbai','Success','CARDREF10002','Online'),(3,3,1200.00,'Swiggy','Food','2026-09-03 19:20:00','Lucknow','Success','CARDREF10003','Mobile App'),(4,4,3000.00,'Myntra','Shopping','2026-09-04 10:45:00','Bengaluru','Failed','CARDREF10004','Online'),(5,5,7500.00,'Reliance Digital','Electronics','2026-09-05 16:10:00','Kolkata','Success','CARDREF10005','POS');
/*!40000 ALTER TABLE `card_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards` (
  `card_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `account_id` int DEFAULT NULL,
  `card_number` varchar(20) NOT NULL,
  `card_type` varchar(20) DEFAULT NULL,
  `card_network` varchar(20) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `credit_limit` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  UNIQUE KEY `card_number` (`card_number`),
  KEY `customer_id` (`customer_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `cards_ibfk_2` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,1,1,'4567123412341001','Debit','Visa','2018-02-10','2028-02-29','Active',0.00),(2,2,2,'5234567890121002','Credit','Mastercard','2019-04-15','2029-04-30','Active',200000.00),(3,3,3,'4567123412341003','Debit','Visa','2020-09-10','2030-09-30','Active',0.00),(4,4,4,'5234567890121004','Debit','Mastercard','2021-12-05','2026-12-31','Blocked',0.00),(5,5,5,'4567123412341005','Debit','Visa','2017-07-15','2027-07-31','Active',0.00);
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` int NOT NULL,
  `customer_number` varchar(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `customer_since` date DEFAULT NULL,
  `customer_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `customer_number` (`customer_number`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'CUST001','Aarav','Sharma','aarav.sharma@email.com','9876543210','1990-05-14','Male','Connaught Place','New Delhi','Delhi','110001','2018-01-10','Active'),(2,'CUST002','Ananya','Patel','ananya.patel@email.com','9812345678','1995-09-22','Female','Bandra West','Mumbai','Maharashtra','400050','2019-03-15','Active'),(3,'CUST003','Rahul','Verma','rahul.verma@email.com','9745612308','1988-12-05','Male','Hazratganj','Lucknow','Uttar Pradesh','226001','2020-07-22','Closed'),(4,'CUST004','Priya','Nair','priya.nair@email.com','9632147850','1993-03-18','Female','MG Road','Bengaluru','Karnataka','560001','2021-11-05','Active'),(5,'CUST005','Amit','Banerjee','amit.b@email.com','9517534620','1985-07-30','Male','Park Street','Kolkata','West Bengal','700016','2017-05-19','Closed');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL,
  `employee_code` varchar(20) NOT NULL,
  `branch_id` int DEFAULT NULL,
  `employee_name` varchar(100) NOT NULL,
  `job_role` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `salary` decimal(12,2) DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `employee_code` (`employee_code`),
  UNIQUE KEY `email` (`email`),
  KEY `branch_id` (`branch_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'EMP001',1,'R. Kumar','Branch Manager','r.kumar@email.com','9876543210',95000.00,'2015-06-12','Active'),(2,'EMP002',1,'V. Sharma','Assistant Manager','v.sharma@email.com','9812345678',75000.00,'2017-03-15','Active'),(3,'EMP003',3,'A. Banerjee','Branch Manager','a.banerjee@email.com','9745612308',92000.00,'2019-01-15','Active'),(4,'EMP004',3,'S. Das','Cashier','s.das@email.com','9632147850',45000.00,'2021-08-10','Active'),(5,'EMP005',5,'S. Reddy','Branch Manager','s.reddy@email.com','9517534620',98000.00,'2021-03-18','Active');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` bigint NOT NULL,
  `account_id` int NOT NULL,
  `transaction_type` varchar(30) NOT NULL,
  `transaction_mode` varchar(30) NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `transaction_date` datetime NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `reference_number` varchar(50) DEFAULT NULL,
  `balance_after` decimal(15,2) DEFAULT NULL,
  `transaction_status` varchar(20) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  UNIQUE KEY `reference_number` (`reference_number`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,1,'Deposit','Cash',15000.00,'2026-09-01 10:30:00','Cash Deposit CP','REF89001',70000.00,'Success','New Delhi'),(2,2,'Withdrawal','ATM',5000.00,'2026-09-02 14:15:00','ATM Cash out','REF89002',120000.00,'Success','Mumbai'),(3,3,'Transfer','UPI',500.00,'2026-09-03 18:45:00','GPay to friend','REF89003',700.00,'Success','Bengaluru'),(4,5,'Interest','System',7500.00,'2026-09-05 00:00:00','FD Quarterly Interest','REF89004',507500.00,'Success','Kolkata'),(5,1,'Withdrawal','Net Banking',2000.00,'2026-09-06 11:20:00','Online shopping','REF89005',68000.00,'Failed','New Delhi');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transfers`
--

DROP TABLE IF EXISTS `transfers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transfers` (
  `transfer_id` bigint NOT NULL,
  `sender_account_id` int NOT NULL,
  `receiver_account_id` int NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `transfer_mode` varchar(30) DEFAULT NULL,
  `transfer_date` datetime DEFAULT NULL,
  `reference_number` varchar(50) DEFAULT NULL,
  `transfer_status` varchar(20) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`transfer_id`),
  UNIQUE KEY `reference_number` (`reference_number`),
  KEY `sender_account_id` (`sender_account_id`),
  KEY `receiver_account_id` (`receiver_account_id`),
  CONSTRAINT `transfers_ibfk_1` FOREIGN KEY (`sender_account_id`) REFERENCES `accounts` (`account_id`),
  CONSTRAINT `transfers_ibfk_2` FOREIGN KEY (`receiver_account_id`) REFERENCES `accounts` (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfers`
--

LOCK TABLES `transfers` WRITE;
/*!40000 ALTER TABLE `transfers` DISABLE KEYS */;
INSERT INTO `transfers` VALUES (1,1,2,5000.00,'NEFT','2026-09-01 11:00:00','TRF10001','Success','Transfer from savings to current account'),(2,2,3,10000.00,'IMPS','2026-09-02 13:30:00','TRF10002','Success','Fund transfer'),(3,3,4,1500.00,'UPI','2026-09-03 17:45:00','TRF10003','Success','UPI transfer'),(4,4,5,2500.00,'NEFT','2026-09-04 14:20:00','TRF10004','Failed','Transfer failed because account is closed'),(5,5,1,7500.00,'IMPS','2026-09-05 18:00:00','TRF10005','Success','Fund transfer');
/*!40000 ALTER TABLE `transfers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-10 15:14:22
