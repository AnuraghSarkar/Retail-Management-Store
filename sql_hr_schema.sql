-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: sql_hr
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `Product_ID` int NOT NULL,
  `Quantity` varchar(45) NOT NULL,
  `Price` int NOT NULL,
  KEY `Product_ID_idx` (`Product_ID`),
  CONSTRAINT `tbl_product_id` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (12,'190',11400),(20,'90',51000);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Customer_Name` varchar(45) NOT NULL,
  `Product_ID` int NOT NULL,
  `Quantity` int NOT NULL,
  `Payment_Method` varchar(45) NOT NULL,
  `Shipped_Date` varchar(45) NOT NULL,
  KEY `Product_ID_idx` (`Product_ID`),
  CONSTRAINT `Product_ID` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('Gaurab',14,4,'Cheque','14/08/2020'),('Nishan bhat',28,12,'Cheque','15/08/2020'),('Padam timalsina',5,12,'Cash','15/08/2020'),('Hj',23,90,'Cheque','18/08/2020'),('Shirsak',14,20,'Cheque','19/08/2020'),('Ram',14,20,'Cheque','19/08/2020'),('Abc',20,10,'Cash','28/08/2020'),('Exampl',20,90,'Cheque','30/08/2020');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `Employee_ID` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Contact` varchar(10) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`Employee_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Anuragh','Anuragh','1','56526','1aa@gmail.com'),(2,'Anuragh timalsina','Nishan','123123','456123','example@gmai.com');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `Product_ID` int NOT NULL,
  `Product_Category` varchar(45) NOT NULL,
  `Product_Name` varchar(45) NOT NULL,
  `Quantity_In` varchar(45) NOT NULL,
  `Product_Stock` int NOT NULL,
  `Amount` int NOT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Meat & Fish','Goat','Kilogram',100,1300),(2,'Meat & Fish','Goat','Half Kilogram',100,700),(3,'Meat & Fish','Chicken','Kilogram',100,500),(4,'Meat & Fish','Chicken','Half Kilogram',100,250),(5,'Meat & Fish','Turkey','Kilogram',100,1100),(6,'Meat & Fish','Turkey','Half Kilogram',100,550),(7,'Meat & Fish','Luncheon Pork','Kilogram',100,1000),(8,'Meat & Fish','Luncheon Pork','Half Kilogram',100,500),(9,'Grains & Bread','Pasta','Kilogram',100,500),(10,'Grains & Bread','Pasta','Half Kilogram',100,250),(11,'Grains & Bread','Rice','Kilogram',100,120),(12,'Grains & Bread','Rice','Half Kilogram',80,60),(13,'Grains & Bread','Bread','Kilogram',100,100),(14,'Grains & Bread','Bread','Half Kilogram',40,50),(15,'Grains & Bread','Breakfast Cereal','Kilogram',100,1200),(16,'Grains & Bread','Breakfast Cereal','Half Kilogram',100,600),(17,'Oil & Fat','Cooking Oil','Liter',78,250),(18,'Oil & Fat','Cooking Oil','Half Liter',100,125),(19,'Oil & Fat','Butter','Kilogram',20,1000),(20,'Oil & Fat','Butter','Half Kilogram',0,500),(21,'Oil & Fat','Cheese','Kilogram',100,1000),(22,'Oil & Fat','Cheese','Half Kilogram',100,500),(23,'Dairy & Eggs','Milk','Liter',100,120),(24,'Dairy & Eggs','Milk','Half Liter',100,60),(25,'Dairy & Eggs','Eggs','Full Crate',100,370),(26,'Dairy & Eggs','Eggs','Half Crate',100,185),(27,'Dairy & Eggs','Yogurt','Liter',100,220),(28,'Dairy & Eggs','Yogurt','Half Liter',100,110),(29,'Produce','Onion','Kilogram',100,240),(30,'Produce','Onion','Half Kilogram',100,120),(31,'Produce','Garlic','Kilogram',88,120),(32,'Produce','Garlic','Half Kilogram',100,60),(33,'Produce','Apple','Kilogram',100,250),(34,'Produce','Apple','Half Kilogram',100,125),(35,'Produce','Tomato','Kilogram',100,80),(36,'Produce','Tomato','Half Kilogram',100,40),(37,'Condiments','Salt','Kilogram',100,30),(38,'Condiments','Salt','Half Kilogram',100,20),(39,'Condiments','Pepper','Kilogram',100,900),(40,'Condiments','Pepper','Half Kilogram',100,450),(41,'Condiments','Honey','Kilogram',100,2850),(42,'Condiments','Honey','Half Kilogram',100,1500),(43,'Condiments','Vinegar','Kilogram',100,1200);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-31 19:07:28
