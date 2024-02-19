-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: gpt
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.20.04.1

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(80) DEFAULT NULL,
  `business_type` varchar(80) DEFAULT NULL,
  `access_key` varchar(255) DEFAULT NULL,
  `recharge_amount` decimal(10,2) DEFAULT '0.00',
  `expiration_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `last_login_time` datetime DEFAULT NULL,
  `chat_count` int NOT NULL DEFAULT '0',
  `client_reference_id` int DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `phone` varchar(80) DEFAULT NULL,
  `reserved_1` varchar(80) DEFAULT NULL,
  `reserved_2` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `access_key` (`access_key`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (3,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NKZZmCMTeU4V8Iq1VpRo27R',6000.00,'2024-06-18 04:21:40','2023-06-19 04:21:40',0,NULL,NULL,NULL,NULL,NULL),(17,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NLlsxCMTeU4V8Iq0JzyqIva',6000.00,'2024-06-21 11:42:48','2023-06-22 11:42:48',0,NULL,NULL,NULL,NULL,NULL),(20,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NLyqoCMTeU4V8Iq0RQA5TGE',6000.00,'2024-06-22 01:32:29','2023-06-23 01:32:29',0,NULL,NULL,NULL,NULL,NULL),(25,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NMnhbCMTeU4V8Iq02PVh5BY',6000.00,'2024-06-24 07:50:56','2023-06-25 07:50:56',9,NULL,NULL,NULL,NULL,NULL),(28,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NN5hhCMTeU4V8Iq1zQDewtq',6000.00,'2024-06-25 03:03:57','2023-06-26 03:03:57',0,NULL,NULL,NULL,NULL,NULL),(29,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNBMcCMTeU4V8Iq1gOQn9DE',6000.00,'2024-06-25 09:06:40','2023-06-26 09:06:40',0,NULL,NULL,NULL,NULL,NULL),(32,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNX6ZCMTeU4V8Iq02Fkv8D9',6000.00,'2024-06-26 08:19:58','2023-06-27 08:19:58',11,NULL,NULL,NULL,NULL,NULL),(33,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNr50CMTeU4V8Iq1PmCQoA5',6000.00,'2024-06-27 05:39:33','2023-06-28 05:39:33',0,NULL,NULL,NULL,NULL,NULL),(34,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNr4jCMTeU4V8Iq1Ohzqsky',6000.00,'2024-06-27 05:42:33','2023-06-28 05:42:33',0,NULL,NULL,NULL,NULL,NULL),(37,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NpPBtCMTeU4V8Iq0o1NLDNF',20000.00,'2024-09-12 13:33:02','2023-09-13 00:46:18',0,NULL,NULL,NULL,NULL,NULL),(39,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3O5P65CMTeU4V8Iq0yExGzjR',20000.00,'2024-10-26 03:52:56','2023-10-27 03:52:56',0,NULL,NULL,NULL,NULL,NULL),(40,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NG9fCCMTeU4V8Iq8K9ebIaJ',6000.00,'2024-06-27 05:22:02','2023-06-27 05:22:02',32,NULL,NULL,NULL,NULL,NULL),(41,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NXyRjCMTeU4V8Iq0dfEuQJ7',20000.00,'2024-07-26 12:22:02','2023-07-26 12:22:02',0,NULL,NULL,NULL,NULL,NULL),(42,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NfeaNCMTeU4V8Iq0frdmvXl',20000.00,'2024-08-16 12:22:02','2023-08-16 12:22:02',5,NULL,NULL,NULL,NULL,NULL),(43,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NvAs2CMTeU4V8Iq0l9DQvtk',20000.00,'2024-09-28 12:00:00','2023-09-28 12:00:00',0,NULL,NULL,NULL,NULL,NULL),(44,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3OSgZfCMTeU4V8Iq0vpaujo0',20000.00,'2025-01-02 10:00:00','2024-01-02 10:00:00',0,NULL,NULL,NULL,NULL,NULL),(45,'prod_PNGG48oMxPNetE','basic_chat','pi_3OYgQ6CMTeU4V8Iq0Xbfghyk',3000.00,'2024-02-14 03:01:47','2024-01-15 03:01:47',12,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` varchar(80) DEFAULT NULL,
  `business_type` varchar(80) DEFAULT NULL,
  `subscription_type` varchar(80) DEFAULT NULL,
  `unit_fee` decimal(10,2) DEFAULT '0.00',
  `unit_validity_time` int DEFAULT '0',
  `reserved_1` varchar(80) DEFAULT NULL,
  `reserved_2` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('prod_O2DnzwF8ZK5VJ0','basic_chat','trial',400.00,86400,NULL,NULL),('prod_O1fiOSsJRrZUjU','basic_chat','per_year',20000.00,31536000,NULL,NULL),('prod_PNGG48oMxPNetE','basic_chat','per_month',3000.00,2592000,NULL,NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `chat_count_setting` int DEFAULT '50'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES (120);
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-18  8:09:10