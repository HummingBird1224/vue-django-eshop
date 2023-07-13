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
-- Table structure for table `products_product_tags`
--

DROP TABLE IF EXISTS `products_product_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `producttag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_product_tags_product_id_producttag_id_993adb5c_uniq` (`product_id`,`producttag_id`),
  KEY `products_product_tag_producttag_id_a60afbb7_fk_products_` (`producttag_id`),
  CONSTRAINT `products_product_tag_producttag_id_a60afbb7_fk_products_` FOREIGN KEY (`producttag_id`) REFERENCES `products_producttag` (`id`),
  CONSTRAINT `products_product_tags_product_id_f82cb4be_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product_tags`
--

LOCK TABLES `products_product_tags` WRITE;
/*!40000 ALTER TABLE `products_product_tags` DISABLE KEYS */;
INSERT INTO `products_product_tags` VALUES (2,1,2),(19,8,2),(57,9,4),(58,12,4),(59,14,4),(80,17,4),(55,18,4),(61,23,4),(62,24,4),(83,32,2),(81,39,5),(82,40,5);
/*!40000 ALTER TABLE `products_product_tags` ENABLE KEYS */;
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
