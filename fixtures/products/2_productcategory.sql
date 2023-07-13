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
-- Table structure for table `products_productcategory`
--

DROP TABLE IF EXISTS `products_productcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_productcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `detail` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `parent_category_id` int(11) DEFAULT NULL,
  `extra_info` json DEFAULT NULL,
  `position` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `products_productcate_parent_category_id_a15b1c75_fk_products_` (`parent_category_id`),
  CONSTRAINT `products_productcate_parent_category_id_a15b1c75_fk_products_` FOREIGN KEY (`parent_category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategory`
--

LOCK TABLES `products_productcategory` WRITE;
/*!40000 ALTER TABLE `products_productcategory` DISABLE KEYS */;
INSERT INTO `products_productcategory` VALUES (1,'root','root','','','2019-12-02 18:24:05.658104',1,NULL,'{}',10000),(2,'平袋','flatbag','','products/extra/category/ic_nav_film.svg','2019-12-02 18:24:41.943643',1,1,'{\"image\": \"img/product_category/flatbag/category_flatbag_all.png\"}',10000),(3,'インナーバッグ','innerbag','透明・不透明な梱包用の袋','','2019-12-02 18:25:11.297198',1,2,'{\"image\": \"img/product_category/flatbag/category_flatbag_inner.png\"}',10000),(4,'スタンド','standbag','プロテインなどに使われる立体型の袋','','2019-12-02 18:25:30.902871',1,2,'{\"image\": \"img/product_category/flatbag/category_flatbag_stand.png\"}',10000),(5,'小分け袋','smallbag','サプリメントなどで使われる袋','','2019-12-02 18:25:46.034396',1,2,'{\"image\": \"img/product_category/flatbag/category_flatbag_smallbag.png\"}',10000),(6,'ダンボール','cardboard','','products/extra/category/ic_nav_cardboox.svg','2019-12-02 18:26:00.532246',1,1,'{\"image\": \"img/product_category/cardboard/category_cardbox_all.png\"}',10000),(7,'紙器','paperbox','','products/extra/category/ic_nav_paperbox.svg','2019-12-02 18:26:11.516111',1,1,'{\"image\": \"img/product_category/paperbox/category_paperbox_all.png\"}',10000),(8,'BASE','base','','','2020-03-12 14:58:57.279609',1,9,'{}',10000),(9,'外部連携','external','','products/extra/category/logo_mark.png','2020-03-12 15:05:49.493891',1,1,'{}',10000),(10,'小ロット印刷','small-lot-flatbag','少ない注文数でも高品質なパッケージを作成できます','','2020-04-16 01:46:21.472211',1,2,'{\"image\": \"img/product_category/flatbag/category_flatbag_smalllot.png\"}',1),(11,'小ロット印刷','small-lot-cardboard','少ない注文数でも高品質なパッケージを作成できます','','2020-04-16 16:29:18.489936',1,6,'{\"tags\": [\"100箱 ~ 注文\", \"白黒印刷のみ\", \"規制サイズ\"], \"image\": \"img/product_category/cardboard/category_cardbox_smalllot.png\"}',1),(12,'メール便対応','mailbox','ゆうパック・クリックポスト対応のダンボール','','2020-04-16 16:36:22.992595',1,6,'{\"image\": \"img/product_category/cardboard/category_cardbox_mail.png\"}',10000),(13,'配送用','shipping-cardboard','宅配などで使われるオーソドックスな形','','2020-04-16 16:38:11.034451',1,6,'{\"image\": \"img/product_category/cardboard/category_cardbox_delivery.png\"}',10000),(14,'梱包/化粧箱','packaging-box','内箱としても使えるダンボール','','2020-04-16 16:39:44.390874',1,6,'{\"image\": \"img/product_category/cardboard/category_cardbox_packing.png\"}',10000);
/*!40000 ALTER TABLE `products_productcategory` ENABLE KEYS */;
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
