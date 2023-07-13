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
-- Table structure for table `products_productthumbnail`
--

DROP TABLE IF EXISTS `products_productthumbnail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_productthumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `alt_text` varchar(300) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productthum_product_id_7c5839a3_fk_products_` (`product_id`),
  CONSTRAINT `products_productthum_product_id_7c5839a3_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productthumbnail`
--

LOCK TABLES `products_productthumbnail` WRITE;
/*!40000 ALTER TABLE `products_productthumbnail` DISABLE KEYS */;
INSERT INTO `products_productthumbnail` VALUES (1,'2020-01-28 15:30:19.213267','products/products/folding-carton/cover/folding-carton_01.jpg',NULL,1,25),(2,'2020-01-28 15:30:19.617666','products/products/folding-carton/cover/folding-carton_hover.jpg',NULL,1,25),(3,'2020-01-28 15:33:50.106146','products/products/ntype-custominsert/cover/ntype-custominsert_01.jpg',NULL,1,24),(4,'2020-01-28 15:33:50.418097','products/products/ntype-custominsert/cover/ntype-custominsert_hover.jpg',NULL,1,24),(5,'2020-01-28 15:34:24.286124','products/products/ctype/cover/ctype_01.jpg',NULL,1,23),(6,'2020-01-28 15:34:24.625870','products/products/ctype/cover/ctype_hover.jpg',NULL,1,23),(7,'2020-01-28 15:38:36.592459','products/products/ttype/cover/ttype_01.jpg',NULL,1,22),(8,'2020-01-28 15:38:36.841994','products/products/ttype/cover/ttype_hover.jpg',NULL,1,22),(9,'2020-01-28 15:39:03.390766','products/products/atype/cover/atype_01.jpg',NULL,1,21),(10,'2020-01-28 15:39:03.614793','products/products/atype/cover/atype_hover.jpg',NULL,1,21),(11,'2020-01-28 15:39:24.156850','products/products/ntype-mailer/cover/ntype-mailer_01.jpg',NULL,1,20),(12,'2020-01-28 15:39:24.379576','products/products/ntype-mailer/cover/ntype-mailer_hover.jpg',NULL,1,20),(13,'2020-01-28 15:40:42.856159','products/products/ntype-corrugated/cover/ntype-corrugated_01.jpg',NULL,1,19),(14,'2020-01-28 15:40:43.067395','products/products/ntype-corrugated/cover/ntype-corrugated_hover.jpg',NULL,1,19),(15,'2020-01-28 15:42:26.678656','products/products/subsection-bag/cover/subsection-bag_01.jpg',NULL,1,18),(16,'2020-01-28 15:42:26.945721','products/products/subsection-bag/cover/subsection-bag_hover.jpg',NULL,1,18),(17,'2020-01-28 15:42:46.710353','products/products/aluminum-pouche/cover/aluminum-pouche_01.jpg',NULL,1,17),(18,'2020-01-28 15:42:47.014238','products/products/aluminum-pouche/cover/aluminum-pouche_hover.jpg',NULL,1,17),(19,'2020-01-28 15:43:51.640776','products/products/zip-aluminum-stand/cover/zip-aluminum-stand_01.jpg',NULL,1,15),(20,'2020-01-28 15:43:51.865881','products/products/zip-aluminum-stand/cover/zip-aluminum-stand_hover.jpg',NULL,1,15),(21,'2020-01-28 15:44:19.134984','products/products/zip-aluminum-bag/cover/zip-aluminum-bag_01.jpg',NULL,1,13),(22,'2020-01-28 15:44:19.414898','products/products/zip-aluminum-bag/cover/zip-aluminum-bag_hover.jpg',NULL,1,13),(23,'2020-01-28 15:45:01.814742','products/products/tape-bag/cover/tape-bag_01.jpg',NULL,1,14),(24,'2020-01-28 15:45:02.361130','products/products/tape-bag/cover/tape-bag_hover.jpg',NULL,1,14),(25,'2020-01-28 15:46:15.616514','products/products/zip-aluminum-clear-bag/cover/zip-aluminum-clear-bag_01.jpg',NULL,1,12),(26,'2020-01-28 15:46:15.914937','products/products/zip-aluminum-clear-bag/cover/zip-aluminum-clear-bag_hover.jpg',NULL,1,12),(27,'2020-01-28 15:46:36.940544','products/products/aluminum-clear-bag/cover/aluminum-clear-bag_01.jpg',NULL,1,9),(28,'2020-01-28 15:46:37.191704','products/products/aluminum-clear-bag/cover/aluminum-clear-bag_hover.jpg',NULL,1,9),(29,'2020-01-28 15:47:05.487296','products/products/zip-clear-bag/cover/zip-clear-bag_01.jpg',NULL,1,8),(30,'2020-01-28 15:47:05.734255','products/products/zip-clear-bag/cover/zip-clear-bag_hover.jpg',NULL,1,8),(31,'2020-01-28 15:47:29.246487','products/products/zip-clear-pressbag/cover/zip-clear-pressbag_01.jpg',NULL,1,7),(32,'2020-01-28 15:47:29.549673','products/products/zip-clear-pressbag/cover/zip-clear-pressbag_hover.jpg',NULL,1,7),(33,'2020-01-28 15:47:52.924207','products/products/tape-opp-bag/cover/tape-opp-bag_01.jpg',NULL,1,1),(34,'2020-01-28 15:47:53.137827','products/products/tape-opp-bag/cover/tape-opp-bag_hover.jpg',NULL,1,1),(35,'2020-03-12 15:02:57.628513','products/products/base-original/cover/base_original_01.jpg',NULL,1,26),(36,'2020-03-12 15:02:57.630564','products/products/base-original/cover/base_original_04.jpg',NULL,1,26),(37,'2020-03-12 15:05:24.464763','products/products/base-atype-smalllot/cover/typea-small01.jpg',NULL,1,27),(39,'2020-03-12 15:06:57.907925','products/products/base-atype/cover/typea01.jpg',NULL,1,28),(40,'2020-03-12 15:06:57.910785','products/products/base-atype/cover/typea02.jpg',NULL,1,28),(41,'2020-03-12 15:07:51.530507','products/products/base-tape-opp-bag/cover/tape-opp-bag01.jpg',NULL,1,29),(42,'2020-03-12 15:07:51.534053','products/products/base-tape-opp-bag/cover/tape-opp-bag05.jpg',NULL,1,29),(43,'2020-03-12 15:09:35.446234','products/products/base-zip-bag/cover/zip-clear-bag_01.jpg',NULL,1,30),(44,'2020-03-12 15:09:35.449858','products/products/base-zip-bag/cover/zip-clear-bag_05.jpg',NULL,1,30),(46,'2020-05-18 17:43:46.101129','products/products/tape-opp-bag-small-lot/cover/tape-opp-bag-small-lot_01.jpg',NULL,1,31),(47,'2020-05-18 17:44:02.000182','products/products/tape-opp-bag-small-lot/cover/tape-opp-bag-small-lot_hover.jpg',NULL,1,31),(48,'2020-05-18 18:23:06.656946','products/products/zip-aluminum-clear-bag-small-lot/cover/zip-aluminum-clear-bag-small-lot_01.jpg',NULL,1,32),(49,'2020-05-18 18:23:11.979602','products/products/zip-aluminum-clear-bag-small-lot/cover/zip-aluminum-clear-bag-small-lot_hover.jpg',NULL,1,32),(52,'2020-05-18 18:47:10.807553','products/products/zip-clear-bag-small-lot/cover/zip-clear-bag-small-lot_01.jpg',NULL,1,33),(53,'2020-05-18 18:48:09.141369','products/products/zip-clear-bag-small-lot/cover/zip-clear-bag-small-lot_hover.jpg',NULL,1,33),(54,'2020-05-18 19:26:26.218283','products/products/zip-aluminum-stand-small-lot/cover/zip-aluminum-stand-small-lot_01.jpg',NULL,1,34),(55,'2020-05-18 19:26:33.557490','products/products/zip-aluminum-stand-small-lot/cover/zip-aluminum-stand-small-lot_hover.jpg',NULL,1,34),(56,'2020-05-18 20:59:19.869005','products/products/ntype-corrugated-small-lot/cover/ntype-corrugated-small-lot_01.jpg',NULL,1,35),(57,'2020-05-18 20:59:30.373226','products/products/ntype-corrugated-small-lot/cover/ntype-corrugated-small-lot_hover.jpg',NULL,1,35),(58,'2020-05-18 21:13:25.378370','products/products/ntype-mailer-small-lot/cover/ntype-mailer-small-lot_01.jpg',NULL,1,36),(59,'2020-05-18 21:13:30.127280','products/products/ntype-mailer-small-lot/cover/ntype-mailer-small-lot_hover.jpg',NULL,1,36),(60,'2020-05-18 21:48:07.310202','products/products/atype-small-lot/cover/atype-small-lot_01.jpg',NULL,1,37),(61,'2020-05-18 21:48:12.317386','products/products/atype-small-lot/cover/atype-small-lot_hover.jpg',NULL,1,37),(62,'2020-05-18 22:24:19.442641','products/products/ttype-small-lot/cover/ttype-small-lot_01.jpg',NULL,1,38),(63,'2020-05-18 22:24:26.974562','products/products/ttype-small-lot/cover/ttype-small-lot_hover.jpg',NULL,1,38),(64,'2020-05-24 03:03:32.663073','products/products/zip-aluminum-bag-small-lot/cover/zip-aluminum-bag-small-lot_01.jpg',NULL,1,39),(65,'2020-05-24 03:03:44.506565','products/products/zip-aluminum-bag-small-lot/cover/zip-aluminum-bag-small-lot_hover.jpg',NULL,1,39),(66,'2020-05-24 04:33:47.751359','products/products/tape-bag-small-lot/cover/tape-bag-small-lot_01.jpg',NULL,1,40),(67,'2020-05-24 04:35:08.755803','products/products/tape-bag-small-lot/cover/tape-bag-small-lot_hover.jpg',NULL,1,40);
/*!40000 ALTER TABLE `products_productthumbnail` ENABLE KEYS */;
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
