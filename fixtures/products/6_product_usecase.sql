-- MySQL dump 10.13  Distrib 8.0.18, for osx10.14 (x86_64)
--
-- Host: localhost    Database: canal
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `products_product_usecase`
--

DROP TABLE IF EXISTS `products_product_usecase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product_usecase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `productusecase_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_product_usecase_product_id_productusecas_1fe86301_uniq` (`product_id`,`productusecase_id`),
  KEY `products_product_use_productusecase_id_8065b6be_fk_products_` (`productusecase_id`),
  CONSTRAINT `products_product_use_product_id_3db6d7c4_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_product_use_productusecase_id_8065b6be_fk_products_` FOREIGN KEY (`productusecase_id`) REFERENCES `products_productusecase` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product_usecase`
--

LOCK TABLES `products_product_usecase` WRITE;
/*!40000 ALTER TABLE `products_product_usecase` DISABLE KEYS */;
INSERT INTO `products_product_usecase` VALUES (1,1,1),(11,7,1),(12,7,4),(13,8,1),(14,8,3),(15,8,4),(16,9,1),(17,9,4),(22,12,1),(23,12,4),(24,13,1),(25,13,4),(26,14,1),(27,14,4),(28,15,1),(29,15,3),(30,17,2),(31,17,4),(32,18,2),(33,19,1),(34,20,1),(35,20,3),(36,21,1),(37,21,4),(38,22,2),(39,22,3),(41,24,2),(42,24,3),(43,25,3);
/*!40000 ALTER TABLE `products_product_usecase` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-29 17:28:57
