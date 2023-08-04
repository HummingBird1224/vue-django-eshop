/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 8.0.32 : Database - canal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`canal` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `canal`;

/*Table structure for table `account_emailaddress` */

DROP TABLE IF EXISTS `account_emailaddress`;

CREATE TABLE `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE,
  KEY `account_emailaddress_user_id_2c513194_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `account_emailaddress` */

insert  into `account_emailaddress`(`id`,`email`,`verified`,`primary`,`user_id`) values 
(1,'elen12241735@outlook.com',0,1,2);

/*Table structure for table `account_emailconfirmation` */

DROP TABLE IF EXISTS `account_emailconfirmation`;

CREATE TABLE `account_emailconfirmation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `key` (`key`) USING BTREE,
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`) USING BTREE,
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `account_emailconfirmation` */

/*Table structure for table `accounts_billingaddress` */

DROP TABLE IF EXISTS `accounts_billingaddress`;

CREATE TABLE `accounts_billingaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `postal_code` varchar(12) NOT NULL,
  `prefecture` varchar(12) NOT NULL,
  `city` varchar(120) NOT NULL,
  `building` varchar(120) DEFAULT NULL,
  `tel` varchar(36) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `last_used` datetime(6) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `accounts_billingaddress_user_id_14c3fa39_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `accounts_billingaddress_user_id_14c3fa39_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `accounts_billingaddress` */

/*Table structure for table `accounts_deliveryaddress` */

DROP TABLE IF EXISTS `accounts_deliveryaddress`;

CREATE TABLE `accounts_deliveryaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `postal_code` varchar(12) NOT NULL,
  `prefecture` varchar(12) NOT NULL,
  `city` varchar(120) NOT NULL,
  `building` varchar(120) DEFAULT NULL,
  `tel` varchar(36) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `last_used` datetime(6) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `accounts_deliveryaddress_user_id_1e996adf_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `accounts_deliveryaddress_user_id_1e996adf_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `accounts_deliveryaddress` */

/*Table structure for table `accounts_payjpinfo` */

DROP TABLE IF EXISTS `accounts_payjpinfo`;

CREATE TABLE `accounts_payjpinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` varchar(64) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`) USING BTREE,
  CONSTRAINT `accounts_payjpinfo_user_id_0b11da35_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `accounts_payjpinfo` */

insert  into `accounts_payjpinfo`(`id`,`customer_id`,`user_id`) values 
(1,'cus_44b5bf0d774e0b533f1d4231279f',1),
(2,'cus_625b1809770c0893b657df96492c',2);

/*Table structure for table `accounts_user` */

DROP TABLE IF EXISTS `accounts_user`;

CREATE TABLE `accounts_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `extra_info` longtext,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `accounts_user` */

insert  into `accounts_user`(`id`,`password`,`last_login`,`email`,`company_name`,`name`,`date_joined`,`updated_at`,`is_active`,`is_admin`,`url`,`extra_info`) values 
(1,'pbkdf2_sha256$216000$0WIPrMmCcD81$XqKdCM6e2ilYthrGcaXCAA749yPGwPBHAX+HsdAIslQ=','2023-06-23 00:46:56.800390','test@example.com','example','test','2023-04-26 08:09:16.472486','2023-04-26 08:09:17.254351',1,1,NULL,NULL),
(2,'pbkdf2_sha256$216000$qIlJW35OIwPL$1QMcr1DvzG3G5t5tbHNxXHq4gP7S14TBg4JHq+5OxRM=',NULL,'elen12241735@outlook.com',NULL,'aaa','2023-06-10 16:22:57.150170','2023-06-10 16:22:57.150170',1,1,NULL,'{\"campaign\": null}');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=205 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add content type',4,'add_contenttype'),
(14,'Can change content type',4,'change_contenttype'),
(15,'Can delete content type',4,'delete_contenttype'),
(16,'Can view content type',4,'view_contenttype'),
(17,'Can add session',5,'add_session'),
(18,'Can change session',5,'change_session'),
(19,'Can delete session',5,'delete_session'),
(20,'Can view session',5,'view_session'),
(21,'Can add site',6,'add_site'),
(22,'Can change site',6,'change_site'),
(23,'Can delete site',6,'delete_site'),
(24,'Can view site',6,'view_site'),
(25,'Can add email address',7,'add_emailaddress'),
(26,'Can change email address',7,'change_emailaddress'),
(27,'Can delete email address',7,'delete_emailaddress'),
(28,'Can view email address',7,'view_emailaddress'),
(29,'Can add email confirmation',8,'add_emailconfirmation'),
(30,'Can change email confirmation',8,'change_emailconfirmation'),
(31,'Can delete email confirmation',8,'delete_emailconfirmation'),
(32,'Can view email confirmation',8,'view_emailconfirmation'),
(33,'Can add social account',9,'add_socialaccount'),
(34,'Can change social account',9,'change_socialaccount'),
(35,'Can delete social account',9,'delete_socialaccount'),
(36,'Can view social account',9,'view_socialaccount'),
(37,'Can add social application',10,'add_socialapp'),
(38,'Can change social application',10,'change_socialapp'),
(39,'Can delete social application',10,'delete_socialapp'),
(40,'Can view social application',10,'view_socialapp'),
(41,'Can add social application token',11,'add_socialtoken'),
(42,'Can change social application token',11,'change_socialtoken'),
(43,'Can delete social application token',11,'delete_socialtoken'),
(44,'Can view social application token',11,'view_socialtoken'),
(45,'Can add SES Stat',12,'add_sesstat'),
(46,'Can change SES Stat',12,'change_sesstat'),
(47,'Can delete SES Stat',12,'delete_sesstat'),
(48,'Can view SES Stat',12,'view_sesstat'),
(49,'Can add user',13,'add_user'),
(50,'Can change user',13,'change_user'),
(51,'Can delete user',13,'delete_user'),
(52,'Can view user',13,'view_user'),
(53,'Can add pay jp info',14,'add_payjpinfo'),
(54,'Can change pay jp info',14,'change_payjpinfo'),
(55,'Can delete pay jp info',14,'delete_payjpinfo'),
(56,'Can view pay jp info',14,'view_payjpinfo'),
(57,'Can add delivery address',15,'add_deliveryaddress'),
(58,'Can change delivery address',15,'change_deliveryaddress'),
(59,'Can delete delivery address',15,'delete_deliveryaddress'),
(60,'Can view delivery address',15,'view_deliveryaddress'),
(61,'Can add billing address',16,'add_billingaddress'),
(62,'Can change billing address',16,'change_billingaddress'),
(63,'Can delete billing address',16,'delete_billingaddress'),
(64,'Can view billing address',16,'view_billingaddress'),
(65,'Can add transaction',17,'add_transaction'),
(66,'Can change transaction',17,'change_transaction'),
(67,'Can delete transaction',17,'delete_transaction'),
(68,'Can view transaction',17,'view_transaction'),
(69,'Can add cart',18,'add_cart'),
(70,'Can change cart',18,'change_cart'),
(71,'Can delete cart',18,'delete_cart'),
(72,'Can view cart',18,'view_cart'),
(73,'Can add cart item',19,'add_cartitem'),
(74,'Can change cart item',19,'change_cartitem'),
(75,'Can delete cart item',19,'delete_cartitem'),
(76,'Can view cart item',19,'view_cartitem'),
(77,'Can add order',20,'add_order'),
(78,'Can change order',20,'change_order'),
(79,'Can delete order',20,'delete_order'),
(80,'Can view order',20,'view_order'),
(81,'Can add order item',21,'add_orderitem'),
(82,'Can change order item',21,'change_orderitem'),
(83,'Can delete order item',21,'delete_orderitem'),
(84,'Can view order item',21,'view_orderitem'),
(85,'Can add provisional order item design',22,'add_provisionalorderitemdesign'),
(86,'Can change provisional order item design',22,'change_provisionalorderitemdesign'),
(87,'Can delete provisional order item design',22,'delete_provisionalorderitemdesign'),
(88,'Can view provisional order item design',22,'view_provisionalorderitemdesign'),
(89,'Can add order item design',23,'add_orderitemdesign'),
(90,'Can change order item design',23,'change_orderitemdesign'),
(91,'Can delete order item design',23,'delete_orderitemdesign'),
(92,'Can view order item design',23,'view_orderitemdesign'),
(93,'Can add order item delivery',24,'add_orderitemdelivery'),
(94,'Can change order item delivery',24,'change_orderitemdelivery'),
(95,'Can delete order item delivery',24,'delete_orderitemdelivery'),
(96,'Can view order item delivery',24,'view_orderitemdelivery'),
(97,'Can add order delivery address',25,'add_orderdeliveryaddress'),
(98,'Can change order delivery address',25,'change_orderdeliveryaddress'),
(99,'Can delete order delivery address',25,'delete_orderdeliveryaddress'),
(100,'Can view order delivery address',25,'view_orderdeliveryaddress'),
(101,'Can add order billing address',26,'add_orderbillingaddress'),
(102,'Can change order billing address',26,'change_orderbillingaddress'),
(103,'Can delete order billing address',26,'delete_orderbillingaddress'),
(104,'Can view order billing address',26,'view_orderbillingaddress'),
(105,'Can add log order item state update',27,'add_logorderitemstateupdate'),
(106,'Can change log order item state update',27,'change_logorderitemstateupdate'),
(107,'Can delete log order item state update',27,'delete_logorderitemstateupdate'),
(108,'Can view log order item state update',27,'view_logorderitemstateupdate'),
(109,'Can add product',28,'add_product'),
(110,'Can change product',28,'change_product'),
(111,'Can delete product',28,'delete_product'),
(112,'Can view product',28,'view_product'),
(113,'Can add product tag',29,'add_producttag'),
(114,'Can change product tag',29,'change_producttag'),
(115,'Can delete product tag',29,'delete_producttag'),
(116,'Can view product tag',29,'view_producttag'),
(117,'Can add product usecase',30,'add_productusecase'),
(118,'Can change product usecase',30,'change_productusecase'),
(119,'Can delete product usecase',30,'delete_productusecase'),
(120,'Can view product usecase',30,'view_productusecase'),
(121,'Can add product image',31,'add_productimage'),
(122,'Can change product image',31,'change_productimage'),
(123,'Can delete product image',31,'delete_productimage'),
(124,'Can view product image',31,'view_productimage'),
(125,'Can add product category',32,'add_productcategory'),
(126,'Can change product category',32,'change_productcategory'),
(127,'Can delete product category',32,'delete_productcategory'),
(128,'Can view product category',32,'view_productcategory'),
(129,'Can add product price',33,'add_productprice'),
(130,'Can change product price',33,'change_productprice'),
(131,'Can delete product price',33,'delete_productprice'),
(132,'Can view product price',33,'view_productprice'),
(133,'Can add product category tag',34,'add_productcategorytag'),
(134,'Can change product category tag',34,'change_productcategorytag'),
(135,'Can delete product category tag',34,'delete_productcategorytag'),
(136,'Can view product category tag',34,'view_productcategorytag'),
(137,'Can add product info',35,'add_productinfo'),
(138,'Can change product info',35,'change_productinfo'),
(139,'Can delete product info',35,'delete_productinfo'),
(140,'Can view product info',35,'view_productinfo'),
(141,'Can add product option',36,'add_productoption'),
(142,'Can change product option',36,'change_productoption'),
(143,'Can delete product option',36,'delete_productoption'),
(144,'Can view product option',36,'view_productoption'),
(145,'Can add product option condition',37,'add_productoptioncondition'),
(146,'Can change product option condition',37,'change_productoptioncondition'),
(147,'Can delete product option condition',37,'delete_productoptioncondition'),
(148,'Can view product option condition',37,'view_productoptioncondition'),
(149,'Can add product option item',38,'add_productoptionitem'),
(150,'Can change product option item',38,'change_productoptionitem'),
(151,'Can delete product option item',38,'delete_productoptionitem'),
(152,'Can view product option item',38,'view_productoptionitem'),
(153,'Can add easy draft',39,'add_easydraft'),
(154,'Can change easy draft',39,'change_easydraft'),
(155,'Can delete easy draft',39,'delete_easydraft'),
(156,'Can view easy draft',39,'view_easydraft'),
(157,'Can add easy draft print area',40,'add_easydraftprintarea'),
(158,'Can change easy draft print area',40,'change_easydraftprintarea'),
(159,'Can delete easy draft print area',40,'delete_easydraftprintarea'),
(160,'Can view easy draft print area',40,'view_easydraftprintarea'),
(161,'Can add product example image',41,'add_productexampleimage'),
(162,'Can change product example image',41,'change_productexampleimage'),
(163,'Can delete product example image',41,'delete_productexampleimage'),
(164,'Can view product example image',41,'view_productexampleimage'),
(165,'Can add notice',42,'add_notice'),
(166,'Can change notice',42,'change_notice'),
(167,'Can delete notice',42,'delete_notice'),
(168,'Can view notice',42,'view_notice'),
(169,'Can add notice category',43,'add_noticecategory'),
(170,'Can change notice category',43,'change_noticecategory'),
(171,'Can delete notice category',43,'delete_noticecategory'),
(172,'Can view notice category',43,'view_noticecategory'),
(173,'Can add notice post',44,'add_noticepost'),
(174,'Can change notice post',44,'change_noticepost'),
(175,'Can delete notice post',44,'delete_noticepost'),
(176,'Can view notice post',44,'view_noticepost'),
(177,'Can add notice read',45,'add_noticeread'),
(178,'Can change notice read',45,'change_noticeread'),
(179,'Can delete notice read',45,'delete_noticeread'),
(180,'Can view notice read',45,'view_noticeread'),
(181,'Can add notice reminder',46,'add_noticereminder'),
(182,'Can change notice reminder',46,'change_noticereminder'),
(183,'Can delete notice reminder',46,'delete_noticereminder'),
(184,'Can view notice reminder',46,'view_noticereminder'),
(185,'Can add my design',47,'add_mydesign'),
(186,'Can change my design',47,'change_mydesign'),
(187,'Can delete my design',47,'delete_mydesign'),
(188,'Can view my design',47,'view_mydesign'),
(189,'Can add my design design',48,'add_mydesigndesign'),
(190,'Can change my design design',48,'change_mydesigndesign'),
(191,'Can delete my design design',48,'delete_mydesigndesign'),
(192,'Can view my design design',48,'view_mydesigndesign'),
(193,'Can add case study category',50,'add_casestudycategory'),
(194,'Can change case study category',50,'change_casestudycategory'),
(195,'Can delete case study category',50,'delete_casestudycategory'),
(196,'Can view case study category',50,'view_casestudycategory'),
(197,'Can add case study',49,'add_casestudy'),
(198,'Can change case study',49,'change_casestudy'),
(199,'Can delete case study',49,'delete_casestudy'),
(200,'Can view case study',49,'view_casestudy'),
(201,'Can add case study image',51,'add_casestudyimage'),
(202,'Can change case study image',51,'change_casestudyimage'),
(203,'Can delete case study image',51,'delete_casestudyimage'),
(204,'Can view case study image',51,'view_casestudyimage');

/*Table structure for table `billing_transaction` */

DROP TABLE IF EXISTS `billing_transaction`;

CREATE TABLE `billing_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(120) NOT NULL,
  `extra_info` longtext,
  `amount` decimal(10,0) NOT NULL,
  `card` varchar(64) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `success` tinyint(1) NOT NULL,
  `is_captured` tinyint(1) NOT NULL,
  `order_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  `type` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `billing_transaction_order_id_d731e333_fk_orders_order_id` (`order_id`) USING BTREE,
  KEY `billing_transaction_user_id_7662ced1_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `billing_transaction_order_id_d731e333_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `billing_transaction_user_id_7662ced1_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `billing_transaction` */

/*Table structure for table `carts_cart` */

DROP TABLE IF EXISTS `carts_cart`;

CREATE TABLE `carts_cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cart_id` varchar(250) NOT NULL,
  `last_changed` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_ordered` tinyint(1) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `carts_cart_user_id_bd0756c7_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `carts_cart_user_id_bd0756c7_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `carts_cart` */

insert  into `carts_cart`(`id`,`cart_id`,`last_changed`,`created_at`,`is_ordered`,`user_id`) values 
(1,'','2023-04-26 08:07:46.005303','2023-04-26 08:07:46.005303',0,NULL),
(2,'','2023-05-02 00:36:40.571742','2023-05-02 00:36:40.571742',0,NULL),
(3,'','2023-05-17 18:39:09.667290','2023-05-17 18:39:09.667290',0,NULL),
(4,'','2023-05-19 08:27:24.392021','2023-05-19 08:27:24.392021',0,NULL),
(5,'','2023-06-02 09:49:39.469560','2023-06-02 09:49:39.469560',0,NULL),
(6,'','2023-06-02 10:03:38.059296','2023-06-02 10:03:38.059296',0,NULL),
(7,'','2023-06-02 16:37:16.952517','2023-06-02 16:37:16.952517',0,NULL),
(8,'','2023-06-02 16:56:44.013178','2023-06-02 16:56:44.013178',0,1),
(9,'','2023-06-02 17:11:25.808151','2023-06-02 17:11:25.808151',0,NULL),
(10,'','2023-06-05 15:25:40.674228','2023-06-05 15:25:40.674228',0,NULL),
(11,'','2023-06-05 18:56:21.395374','2023-06-05 18:56:21.395374',0,NULL),
(14,'','2023-06-12 11:05:26.008508','2023-06-12 11:05:26.008508',0,NULL),
(15,'','2023-06-16 11:50:54.380581','2023-06-16 11:50:54.380581',0,NULL),
(16,'','2023-06-23 00:46:40.588332','2023-06-23 00:46:40.588332',0,NULL);

/*Table structure for table `carts_cartitem` */

DROP TABLE IF EXISTS `carts_cartitem`;

CREATE TABLE `carts_cartitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `prices` longtext,
  `extra_info` longtext,
  `created_at` datetime(6) NOT NULL,
  `in_cart` tinyint(1) NOT NULL,
  `cart_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `carts_cartitem_cart_id_9cb0a756_fk_carts_cart_id` (`cart_id`) USING BTREE,
  KEY `carts_cartitem_product_id_acd010e4_fk_products_product_id` (`product_id`) USING BTREE,
  CONSTRAINT `carts_cartitem_cart_id_9cb0a756_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `carts_cartitem_product_id_acd010e4_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `carts_cartitem` */

/*Table structure for table `casestudies_casestudy` */

DROP TABLE IF EXISTS `casestudies_casestudy`;

CREATE TABLE `casestudies_casestudy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `client` varchar(255) NOT NULL,
  `slug` varchar(120) NOT NULL,
  `text` longtext,
  `position` smallint unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `slug` (`slug`) USING BTREE,
  KEY `casestudies_casestudy_product_id_bf534ccf_fk_products_product_id` (`product_id`) USING BTREE,
  CONSTRAINT `casestudies_casestudy_product_id_bf534ccf_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy` */

insert  into `casestudies_casestudy`(`id`,`title`,`client`,`slug`,`text`,`position`,`is_active`,`product_id`) values 
(1,'タイトル','顧客名','tape-opp-bag','',1,1,1),
(3,'fdgsfdg','rtrwetw','gdgfds','rtrwetrew',1,1,7),
(4,'title1','elen','title-1','text1',5,1,2),
(5,'figma','euri','figma-design','aaaaaaaaaaaaaaerrrrrrrrrrr',19,1,1),
(7,'paper box case study','Danaka','blue-paper-box','',2,1,4),
(8,'aluminum bag','dora','casestudy-aluminum-bag','',1,1,6),
(9,'12','12','slug-12','',1,1,6),
(12,'4','41','slug-41','',1,1,6),
(13,'aaa','sss','aaa','111111111',1,1,5),
(14,'title12','aaa','title-12','ddddddddddddddd',1,1,1),
(15,'qqq','www','qqq','',1,1,6),
(16,'1234','1234','33333','',1,1,4),
(17,'2345','2345','11-222','',1,1,4),
(18,'3456','3456','multiple-images','',1,1,4),
(19,'test1','danaka','test-1','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',1,1,2),
(21,'test again','danaka','test-again','',1,1,1),
(22,'555','555','555','',1,1,5),
(23,'uuu','uuu','uuu','',1,1,4);

/*Table structure for table `casestudies_casestudy_material` */

DROP TABLE IF EXISTS `casestudies_casestudy_material`;

CREATE TABLE `casestudies_casestudy_material` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_ma_casestudy_id_casestudyca_24ad61a8_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_0e09b23f_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_5e6cece7_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_0e09b23f_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_material` */

insert  into `casestudies_casestudy_material`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(2,1,7),
(3,3,18),
(4,4,7),
(5,5,7),
(6,7,18),
(7,8,22),
(8,9,7),
(10,12,7),
(11,13,22),
(12,14,18),
(13,15,18),
(14,16,22),
(15,17,22),
(16,18,22),
(17,19,7),
(19,21,7),
(20,22,22),
(21,23,18);

/*Table structure for table `casestudies_casestudy_printing_method` */

DROP TABLE IF EXISTS `casestudies_casestudy_printing_method`;

CREATE TABLE `casestudies_casestudy_printing_method` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_pr_casestudy_id_casestudyca_1849e811_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_13f3ecf3_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_eb31dbfb_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_13f3ecf3_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_printing_method` */

insert  into `casestudies_casestudy_printing_method`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(1,1,2),
(2,3,17),
(3,4,17),
(4,5,2),
(5,7,2),
(6,8,2),
(7,9,2),
(9,12,2),
(10,13,17),
(11,14,17),
(12,15,2),
(13,16,17),
(14,17,17),
(15,18,17),
(16,19,2),
(18,21,17),
(19,22,17),
(20,23,17);

/*Table structure for table `casestudies_casestudy_processing` */

DROP TABLE IF EXISTS `casestudies_casestudy_processing`;

CREATE TABLE `casestudies_casestudy_processing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_pr_casestudy_id_casestudyca_9f7b7103_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_9db4d9d6_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_e5bea0a7_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_9db4d9d6_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_processing` */

insert  into `casestudies_casestudy_processing`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(2,1,11),
(3,3,20),
(4,4,11),
(5,5,20),
(6,7,20),
(7,8,24),
(8,9,20),
(10,12,11),
(11,13,24),
(12,14,20),
(13,15,20),
(14,16,24),
(15,17,24),
(16,18,24),
(17,19,20),
(19,21,11),
(20,22,20),
(21,23,20);

/*Table structure for table `casestudies_casestudy_product_category` */

DROP TABLE IF EXISTS `casestudies_casestudy_product_category`;

CREATE TABLE `casestudies_casestudy_product_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_pr_casestudy_id_productcate_94214858_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_productcategory_id_a314139d_fk_products_` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_eaec3f0b_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_49112f15_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_product_category` */

insert  into `casestudies_casestudy_product_category`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(1,1,40),
(3,3,41),
(4,4,41),
(5,5,40),
(7,7,41),
(8,8,41),
(9,9,40),
(12,12,40),
(13,13,41),
(14,14,40),
(15,15,40),
(16,16,40),
(17,17,41),
(18,18,40),
(19,19,41),
(21,21,41),
(22,22,41),
(23,23,41);

/*Table structure for table `casestudies_casestudy_shape` */

DROP TABLE IF EXISTS `casestudies_casestudy_shape`;

CREATE TABLE `casestudies_casestudy_shape` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_sh_casestudy_id_casestudyca_688dc8c7_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_e1a92c03_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_98f572a0_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_e1a92c03_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_shape` */

insert  into `casestudies_casestudy_shape`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(2,1,5),
(4,3,16),
(5,4,16),
(6,5,5),
(7,7,5),
(8,8,16),
(9,9,32),
(10,12,16),
(11,13,5),
(12,14,32),
(13,15,32),
(14,16,23),
(15,17,23),
(16,18,23),
(17,19,16),
(19,21,5),
(20,22,16),
(21,23,32);

/*Table structure for table `casestudies_casestudy_sustainability` */

DROP TABLE IF EXISTS `casestudies_casestudy_sustainability`;

CREATE TABLE `casestudies_casestudy_sustainability` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_su_casestudy_id_casestudyca_f788dd1f_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_44e0e82e_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_3d5be461_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_44e0e82e_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_sustainability` */

insert  into `casestudies_casestudy_sustainability`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(1,1,13),
(2,3,13),
(3,4,13),
(4,5,21),
(5,7,21),
(6,8,13),
(7,9,13),
(9,12,13),
(10,13,21),
(11,14,13),
(12,15,21),
(13,16,21),
(14,17,21),
(15,18,21),
(16,19,13),
(18,21,21),
(19,22,21),
(20,23,21);

/*Table structure for table `casestudies_casestudy_usage` */

DROP TABLE IF EXISTS `casestudies_casestudy_usage`;

CREATE TABLE `casestudies_casestudy_usage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `casestudy_id` int NOT NULL,
  `casestudycategory_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `casestudies_casestudy_us_casestudy_id_casestudyca_27670756_uniq` (`casestudy_id`,`casestudycategory_id`) USING BTREE,
  KEY `casestudies_casestud_casestudycategory_id_6b2b40a4_fk_casestudi` (`casestudycategory_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_casestudy_id_55606dd1_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestud_casestudycategory_id_6b2b40a4_fk_casestudi` FOREIGN KEY (`casestudycategory_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudy_usage` */

insert  into `casestudies_casestudy_usage`(`id`,`casestudy_id`,`casestudycategory_id`) values 
(2,1,9),
(3,3,19),
(4,4,9),
(5,5,19),
(6,7,19),
(7,8,25),
(8,9,9),
(10,12,9),
(11,13,19),
(12,14,19),
(13,15,19),
(14,16,25),
(15,17,25),
(16,18,25),
(17,19,35),
(19,21,19),
(20,22,35),
(21,23,25);

/*Table structure for table `casestudies_casestudycategory` */

DROP TABLE IF EXISTS `casestudies_casestudycategory`;

CREATE TABLE `casestudies_casestudycategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(120) NOT NULL,
  `overview` longtext,
  `icon` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `URL` varchar(200) DEFAULT NULL,
  `position` smallint unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `category_id` int DEFAULT NULL,
  `text` longtext,
  `advantage` longtext,
  `disadvantage` longtext,
  `explanatory_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `slug` (`slug`) USING BTREE,
  KEY `casestudies_casestud_category_id_9bf68aa8_fk_casestudi` (`category_id`) USING BTREE,
  CONSTRAINT `casestudies_casestud_category_id_9bf68aa8_fk_casestudi` FOREIGN KEY (`category_id`) REFERENCES `casestudies_casestudycategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `casestudies_casestudycategory` */

insert  into `casestudies_casestudycategory`(`id`,`name`,`slug`,`overview`,`icon`,`image`,`URL`,`position`,`is_active`,`category_id`,`text`,`advantage`,`disadvantage`,`explanatory_image`) values 
(1,'印刷方法','printing_method','印刷方法','casestudies/casestudy_category/icons/items/digital_print.jpg','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(2,'デジタル印刷','digital_print','デジタル印刷','casestudies/casestudy_category/icons/items/digital_print.jpg','',NULL,1,1,1,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります','casestudies/casestudy_category/explanations/items/Screenshot_21.png'),
(3,'root','root','','','',NULL,1,1,NULL,NULL,NULL,NULL,NULL),
(4,'形状','shape','','casestudies/casestudy_category/icons/items/shape_02.png','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(5,'形状-1','shape-1','','casestudies/casestudy_category/icons/items/shape_02.png','',NULL,1,1,4,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります','casestudies/casestudy_category/explanations/items/Screenshot_21.png'),
(6,'材質','material','','casestudies/casestudy_category/icons/items/material_2.png','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(7,'材質-1','mat-1','','casestudies/casestudy_category/icons/items/material_1.png','',NULL,1,1,6,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(8,'用途','usage','','casestudies/casestudy_category/icons/items/usage_1.jpg','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(9,'用途-1','usage-1','','casestudies/casestudy_category/icons/items/usage_1.jpg','',NULL,1,1,8,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(10,'加工','processing','','casestudies/casestudy_category/icons/items/print_area_02.jpg','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(11,'加工-1','proc-1','','casestudies/casestudy_category/icons/items/print_area_02.jpg','',NULL,1,1,10,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(12,'環境配慮','sustainability','','casestudies/casestudy_category/icons/items/sus_1.png','',NULL,1,1,3,NULL,NULL,NULL,NULL),
(13,'環境配慮-1','sus-1','','casestudies/casestudy_category/icons/items/sus_1.png','',NULL,1,1,12,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(16,'形状-2','shape-2','','casestudies/casestudy_category/icons/items/shape_03.png','casestudies/casestudy_category/images/items/full.jpg','http://shpae.canal.ink',2,1,4,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(17,'フェクソ印刷','fexo_printing','','casestudies/casestudy_category/icons/items/fexo_print.jpg','casestudies/casestudy_category/images/items/5mm.jpg','http://print.canal.ink',1,1,1,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(18,'材質-2','mat-2','','casestudies/casestudy_category/icons/items/material_3.png','casestudies/casestudy_category/images/items/normal.jpg','http://material.canal.ink',1,1,6,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(19,'用途-2','usage-2','','casestudies/casestudy_category/icons/items/usage_2.jpg','casestudies/casestudy_category/images/items/zip_clear_pressbag_example.jpg','http://usage.canal.ink',1,1,8,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(20,'加工-2','proc-2','','casestudies/casestudy_category/icons/items/print_area_02.jpg','casestudies/casestudy_category/images/items/tape-opp-bag_design_template.jpg','http://processing.canal.ink',1,1,10,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(21,'環境配慮-2','sus-2','','casestudies/casestudy_category/icons/items/sus_2.png','casestudies/casestudy_category/images/items/template.png','http://sus.canal.ink',1,1,12,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(22,'金属','mat-1-metal',NULL,'casestudies/casestudy_category/icons/items/material_2.png','casestudies/casestudy_category/images/items/aluminum-bag.jpg',NULL,1,1,7,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(23,'ジッパー','shape-2-zipper',NULL,NULL,'casestudies/casestudy_category/images/items/zip_bag.jpg',NULL,1,1,16,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(24,'手作りの','proc-2-hand-made',NULL,NULL,NULL,NULL,1,1,20,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(25,'食べ物','usage-1-food',NULL,'casestudies/casestudy_category/icons/items/usage_3.jpg',NULL,NULL,1,1,9,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(32,'形状-3','shape-3','','casestudies/casestudy_category/icons/items/shape_04.png','',NULL,1,1,4,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',NULL),
(35,'用途-3','usage-3','','casestudies/casestudy_category/icons/items/usage_3.jpg','',NULL,1,1,8,'区切り文字を省略した場合、返される配列にはインデックス [0] の文字列全体が含まれます。\r\n\r\n区切り文字が \"\" の場合、返される配列は単一文字の配列になります。','Python はさまざまなプラットフォーム (Windows、Mac、Linux、Raspberry Pi など) で動作します。\r\nPython は英語に似た単純な構文を持っています。\r\nPython には、開発者が他のプログラミング言語よりも少ない行数でプログラムを作成できる構文があります。','Python はインタープリター システム上で実行されます。つまり、コードは記述されるとすぐに実行できます。これは、プロトタイピングを非常に迅速に行うことができることを意味します。\r\nPython は、手続き型の方法、オブジェクト指向の方法、または関数型の方法で処理できます。',''),
(39,'商品区分','product_category','11111111111','casestudies/casestudy_category/icons/items/interview.png','',NULL,0,1,3,'1111111111','','',''),
(40,'商品区分-1','procat-1','','casestudies/casestudy_category/icons/items/icon_flat_bag.png','',NULL,1,1,39,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','大量ロットが自慢\r\n特色インクを使用することで、PantoneやDICでの色指定が可能\r\n環境不可の少ない水性インクが選択可能','初回生産時に板が必要\r\n細かい文字や薄い先端の印刷には適さない\r\n色数ごとに版が必要\r\n色数の制限がある\r\n位置が難しいため色と色の重なりが難しい\r\nソリッド印刷の場合、ピンホールが出ることがあります',''),
(41,'商品区分-2','procat-2','','casestudies/casestudy_category/icons/items/icon_cardboard_MVn6HYU.png','',NULL,1,1,39,'フレキソ印刷は、段ボール、紙、フィルム、プラスチックなどの表面に経済的に大量印刷するのに理想的です。 フレキソ印刷は大胆です 複雑でないデザインに最適ですが、機器や印刷オペレータに応じて解像度の高いグラフィックを生成するできます。\r\nフレキソ印刷は、フラッドコーティングされたカラーロゴ、テキスト印刷、高コントラストグラフィックに最適です。 色は PantoneおよびGCMIのサンプルに合わせることができます。 プロセス印刷（CMYK）はフレキソ印刷でも可能ですが、細かいディテール 写真を含むデザインの場合、大量（10,000ユニット以上）の場合はオフセット印刷、少量（1,000ユニット未満）の場合はデジタル として良い結果を得ることができます。','','','casestudies/casestudy_category/explanations/items/Screenshot_21_dprW9FV.png');

/*Table structure for table `casestudies_casestudyimage` */

DROP TABLE IF EXISTS `casestudies_casestudyimage`;

CREATE TABLE `casestudies_casestudyimage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `position` smallint unsigned NOT NULL,
  `casestudy_id` int NOT NULL,
  `is_hover_image` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `casestudies_casestud_casestudy_id_153299fa_fk_casestudi` (`casestudy_id`),
  CONSTRAINT `casestudies_casestud_casestudy_id_153299fa_fk_casestudi` FOREIGN KEY (`casestudy_id`) REFERENCES `casestudies_casestudy` (`id`),
  CONSTRAINT `casestudies_casestudyimage_chk_1` CHECK ((`position` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `casestudies_casestudyimage` */

insert  into `casestudies_casestudyimage`(`id`,`image`,`position`,`casestudy_id`,`is_hover_image`) values 
(1,'casestudies/casestudy/container_ship.png',1,16,0),
(2,'casestudies/casestudy/img_top_right.png',1,16,1),
(3,'casestudies/casestudy/img_top_right3.png',1,19,0),
(4,'casestudies/casestudy/img_top_right_OzZsdd7.png',1,19,1),
(5,'casestudies/casestudy/8.jpg',1,21,0),
(6,'casestudies/casestudy/1.jpg',1,21,1),
(7,'casestudies/casestudy/3.jpg',1,1,0),
(8,'casestudies/casestudy/4.jpg',1,1,1),
(9,'casestudies/casestudy/5.jpg',1,3,0),
(10,'casestudies/casestudy/11.jpg',1,3,0),
(11,'casestudies/casestudy/8.jpg',1,3,1),
(12,'casestudies/casestudy/16.jpg',1,4,0),
(13,'casestudies/casestudy/7.jpg',1,4,1),
(14,'casestudies/casestudy/4.jpg',1,4,0),
(15,'casestudies/casestudy/3.jpg',1,4,0),
(16,'casestudies/casestudy/14.jpg',1,5,0),
(17,'casestudies/casestudy/cat_flatbag.jpg',1,5,1),
(18,'casestudies/casestudy/container_ship.png',1,7,0),
(19,'casestudies/casestudy/Screenshot_11.png',1,7,1),
(20,'casestudies/casestudy/aluminum-bag.jpg',1,8,0),
(21,'casestudies/casestudy/aluminum-pouche_04.jpg',1,8,1),
(22,'casestudies/casestudy/img_top_right.png',1,9,0),
(23,'casestudies/casestudy/img_top_right3.png',1,9,1),
(24,'casestudies/casestudy/multi.jpg',1,12,0),
(25,'casestudies/casestudy/11.jpg',1,12,1),
(26,'casestudies/casestudy/related_2.png',1,13,0),
(27,'casestudies/casestudy/aluminum-pouche_04.jpg',1,13,1),
(28,'casestudies/casestudy/7.jpg',1,14,0),
(29,'casestudies/casestudy/3.jpg',1,14,1),
(30,'casestudies/casestudy/1.jpg',1,15,0),
(31,'casestudies/casestudy/8.jpg',1,15,1),
(32,'casestudies/casestudy/aluminum-pouche_02.jpg',1,18,0),
(33,'casestudies/casestudy/aluminum-pouche_04.jpg',1,18,1),
(34,'casestudies/casestudy/cat_flatbag.jpg',1,17,0),
(35,'casestudies/casestudy/aluminum-pouche_02.jpg',1,17,1),
(36,'casestudies/casestudy/15.jpg',1,22,0),
(37,'casestudies/casestudy/6.jpg',1,22,1),
(38,'casestudies/casestudy/handle-craft-paperbag.png',1,23,0),
(39,'casestudies/casestudy/handle-white-paperbag.png',1,23,1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values 
(1,'2023-04-27 02:17:50.859656','1','平袋',1,'[{\"added\": {}}]',32,1),
(2,'2023-04-27 02:18:36.264067','2','平袋 > インナーバッグ',1,'[{\"added\": {}}]',32,1),
(3,'2023-04-27 02:19:39.586373','1','テープ付きOPP袋: tape-opp-bag',1,'[{\"added\": {}}]',28,1),
(4,'2023-04-27 02:21:26.789491','1','CaseStudy object (1)',1,'[{\"added\": {}}]',49,1),
(5,'2023-04-27 02:23:59.885029','1','CaseStudyCategory object (1)',1,'[{\"added\": {}}]',50,1),
(6,'2023-04-27 02:24:35.699077','2','CaseStudyCategory object (2)',1,'[{\"added\": {}}]',50,1),
(7,'2023-04-27 02:28:30.104602','1','CaseStudyCategory object (1)',1,'[{\"added\": {}}]',50,1),
(8,'2023-04-27 02:34:36.369716','2','印刷方法 > デジタル印刷',1,'[{\"added\": {}}]',50,1),
(9,'2023-04-27 02:35:50.736692','1','CaseStudy object (1)',1,'[{\"added\": {}}]',49,1),
(10,'2023-04-27 11:09:27.102284','3','root',1,'[{\"added\": {}}]',50,1),
(11,'2023-04-27 11:09:37.001791','1','root > 印刷方法',2,'[{\"changed\": {\"fields\": [\"\\u30ab\\u30c6\\u30b4\\u30ea\"]}}]',50,1),
(12,'2023-04-27 11:10:18.573966','4','root > 形状',1,'[{\"added\": {}}]',50,1),
(13,'2023-04-27 11:10:33.522302','5','root > 形状 > 形状-1',1,'[{\"added\": {}}]',50,1),
(14,'2023-04-27 11:11:05.885221','6','root > 材質',1,'[{\"added\": {}}]',50,1),
(15,'2023-04-27 11:11:18.330605','7','root > 材質 > 材質-1',1,'[{\"added\": {}}]',50,1),
(16,'2023-04-27 11:11:40.374135','1','CaseStudy object (1)',2,'[{\"changed\": {\"fields\": [\"\\u5f62\\u72b6\", \"\\u6750\\u8cea\"]}}]',49,1),
(17,'2023-04-27 11:12:20.318524','8','root > 用途',1,'[{\"added\": {}}]',50,1),
(18,'2023-04-27 11:13:13.541852','9','root > 用途 > 用途-1',1,'[{\"added\": {}}]',50,1),
(19,'2023-04-27 11:14:18.853231','10','root > 加工',1,'[{\"added\": {}}]',50,1),
(20,'2023-04-27 11:14:32.500763','11','root > 加工 > 加工-1',1,'[{\"added\": {}}]',50,1),
(21,'2023-04-27 11:14:52.621188','12','root > 環境配慮',1,'[{\"added\": {}}]',50,1),
(22,'2023-04-27 11:15:11.005704','13','root > 環境配慮 > 環境配慮-1',1,'[{\"added\": {}}]',50,1),
(23,'2023-04-27 11:15:42.093288','1','CaseStudy object (1)',2,'[{\"changed\": {\"fields\": [\"\\u7528\\u9014\", \"\\u52a0\\u5de5\", \"\\u74b0\\u5883\\u914d\\u616e\"]}}]',49,1),
(24,'2023-04-27 12:20:28.541580','2','テープ付きOPP袋: flatbag',1,'[{\"added\": {}}]',28,1),
(25,'2023-04-27 16:48:53.679401','3','root',1,'[{\"added\": {}}]',32,1),
(26,'2023-04-27 16:49:00.532146','1','root > 平袋',2,'[{\"changed\": {\"fields\": [\"Parent category\"]}}]',32,1),
(27,'2023-05-17 18:41:15.957098','14','印刷方法 > デジタル印刷 > sadsa',1,'[{\"added\": {}}]',50,1),
(28,'2023-05-17 18:50:07.032405','3','CaseStudy object (3)',1,'[{\"added\": {}}]',49,1),
(29,'2023-05-17 20:26:17.124909','15','印刷方法 > デジタル印刷 > casestudycategory1',1,'[{\"added\": {}}]',50,1),
(30,'2023-05-17 20:55:41.284516','4','CaseStudy object (4)',1,'[{\"added\": {}}]',49,1),
(31,'2023-05-18 01:50:50.186212','5','CaseStudy object (5)',1,'[{\"added\": {}}]',49,1),
(32,'2023-05-18 07:39:56.561812','1','paper tag',1,'[{\"added\": {}}]',34,1),
(33,'2023-05-18 07:40:04.766099','4','root > paper bag',1,'[{\"added\": {}}]',32,1),
(34,'2023-05-18 07:42:52.778297','5','root > paper bag > blue paper box',1,'[{\"added\": {}}]',32,1),
(35,'2023-05-18 07:51:07.812891','14','印刷方法 > デジタル印刷 > sadsa',3,'',50,1),
(36,'2023-05-18 07:51:07.819905','15','印刷方法 > デジタル印刷 > casestudycategory1',3,'',50,1),
(37,'2023-05-18 07:57:41.434991','16','形状 > 形状-2',1,'[{\"added\": {}}]',50,1),
(38,'2023-05-18 07:59:11.232854','17','印刷方法 > manual print',1,'[{\"added\": {}}]',50,1),
(39,'2023-05-18 07:59:55.090973','18','材質 > 材質-2',1,'[{\"added\": {}}]',50,1),
(40,'2023-05-18 08:00:40.617624','19','用途 > 用途-2',1,'[{\"added\": {}}]',50,1),
(41,'2023-05-18 08:01:49.635084','20','加工 > 加工-2',1,'[{\"added\": {}}]',50,1),
(42,'2023-05-18 08:02:53.242983','21','環境配慮 > 環境配慮-2',1,'[{\"added\": {}}]',50,1),
(43,'2023-05-18 09:16:33.069175','7','CaseStudy object (7)',1,'[{\"added\": {}}]',49,1),
(44,'2023-05-18 09:23:46.203059','2','cardboard tag',1,'[{\"added\": {}}]',34,1),
(45,'2023-05-18 09:23:50.655512','6','root > cardboard',1,'[{\"added\": {}}]',32,1),
(46,'2023-05-18 09:24:41.020485','7','root > cardboard > mouse cardboard',1,'[{\"added\": {}}]',32,1),
(47,'2023-05-18 10:14:19.832872','8','CaseStudy object (8)',1,'[{\"added\": {}}]',49,1),
(48,'2023-06-02 16:43:08.624067','27','サイズ',1,'[{\"added\": {}}]',50,1),
(49,'2023-06-02 16:52:25.099911','28','サイズ > 1',1,'[{\"added\": {}}]',50,1),
(50,'2023-06-02 16:55:28.618548','29','サイズ > 1',1,'[{\"added\": {}}]',50,1),
(51,'2023-06-02 16:56:36.009194','9','CaseStudy object (9)',1,'[{\"added\": {}}]',49,1),
(52,'2023-06-02 17:01:51.033764','30','材質 > 材質-1 > 1',1,'[{\"added\": {}}]',50,1),
(53,'2023-06-02 17:03:06.558998','10','CaseStudy object (10)',1,'[{\"added\": {}}]',49,1),
(54,'2023-06-02 17:12:30.036715','31','形状 > 3',1,'[{\"added\": {}}]',50,1),
(55,'2023-06-02 17:14:48.233850','32','形状 > 3',1,'[{\"added\": {}}]',50,1),
(56,'2023-06-02 17:15:42.206753','12','CaseStudy object (12)',1,'[{\"added\": {}}]',49,1),
(57,'2023-06-06 14:03:06.224298','33','形状 > ffff',1,'[{\"added\": {}}]',50,1),
(58,'2023-06-06 14:30:58.171719','33','形状 > ffff',3,'',50,1),
(59,'2023-06-07 08:38:58.396477','35','用途 > 用途-3',1,'[{\"added\": {}}]',50,1),
(60,'2023-06-07 08:40:08.108131','34','',3,'',50,1),
(61,'2023-06-22 10:24:52.116646','13','CaseStudy object (13)',1,'[{\"added\": {}}]',49,1),
(62,'2023-06-22 11:11:00.335343','36','商品区分',1,'[{\"added\": {}}]',50,1),
(63,'2023-06-22 11:14:05.577089','37','商品区分 > 商品区分-1',1,'[{\"added\": {}}]',50,1),
(64,'2023-06-22 11:15:33.879453','38','商品区分 > 商品区分-2',1,'[{\"added\": {}}]',50,1),
(65,'2023-06-22 12:49:56.643655','14','CaseStudy object (14)',1,'[{\"added\": {}}]',49,1),
(66,'2023-06-22 20:15:15.336994','15','CaseStudy object (15)',1,'[{\"added\": {}}]',49,1),
(67,'2023-06-22 21:50:18.515503','16','CaseStudy object (16)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (1)\"}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (2)\"}}]',49,1),
(68,'2023-06-22 21:50:36.529246','17','CaseStudy object (17)',1,'[{\"added\": {}}]',49,1),
(69,'2023-06-22 21:50:57.868581','18','CaseStudy object (18)',1,'[{\"added\": {}}]',49,1),
(70,'2023-06-22 22:07:53.462379','19','CaseStudy object (19)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (3)\"}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (4)\"}}]',49,1),
(71,'2023-06-22 22:08:02.729483','20','CaseStudy object (20)',1,'[{\"added\": {}}]',49,1),
(72,'2023-06-22 22:09:41.207656','21','CaseStudy object (21)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (5)\"}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (6)\"}}]',49,1),
(73,'2023-06-23 00:48:11.578692','22','CaseStudy object (22)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (36)\"}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (37)\"}}]',49,1),
(74,'2023-06-23 09:10:23.876948','39','商品区分',1,'[{\"added\": {}}]',50,1),
(75,'2023-06-23 09:12:43.007623','40','商品区分 > 商品区分-1',1,'[{\"added\": {}}]',50,1),
(76,'2023-06-23 09:14:07.773109','41','商品区分 > 商品区分-2',1,'[{\"added\": {}}]',50,1),
(77,'2023-06-23 09:15:32.973907','23','CaseStudy object (23)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (38)\"}}, {\"added\": {\"name\": \"case study image\", \"object\": \"CaseStudyImage object (39)\"}}]',49,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(7,'account','emailaddress'),
(8,'account','emailconfirmation'),
(16,'accounts','billingaddress'),
(15,'accounts','deliveryaddress'),
(14,'accounts','payjpinfo'),
(13,'accounts','user'),
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(17,'billing','transaction'),
(18,'carts','cart'),
(19,'carts','cartitem'),
(49,'casestudies','casestudy'),
(50,'casestudies','casestudycategory'),
(51,'casestudies','casestudyimage'),
(4,'contenttypes','contenttype'),
(12,'django_ses','sesstat'),
(47,'mydesign','mydesign'),
(48,'mydesign','mydesigndesign'),
(42,'notices','notice'),
(43,'notices','noticecategory'),
(44,'notices','noticepost'),
(45,'notices','noticeread'),
(46,'notices','noticereminder'),
(27,'orders','logorderitemstateupdate'),
(20,'orders','order'),
(26,'orders','orderbillingaddress'),
(25,'orders','orderdeliveryaddress'),
(21,'orders','orderitem'),
(24,'orders','orderitemdelivery'),
(23,'orders','orderitemdesign'),
(22,'orders','provisionalorderitemdesign'),
(39,'products','easydraft'),
(40,'products','easydraftprintarea'),
(28,'products','product'),
(32,'products','productcategory'),
(34,'products','productcategorytag'),
(41,'products','productexampleimage'),
(31,'products','productimage'),
(35,'products','productinfo'),
(36,'products','productoption'),
(37,'products','productoptioncondition'),
(38,'products','productoptionitem'),
(33,'products','productprice'),
(29,'products','producttag'),
(30,'products','productusecase'),
(5,'sessions','session'),
(6,'sites','site'),
(9,'socialaccount','socialaccount'),
(10,'socialaccount','socialapp'),
(11,'socialaccount','socialtoken');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'accounts','0001_initial','2023-04-26 08:07:10.220695'),
(2,'account','0001_initial','2023-04-26 08:07:10.575288'),
(3,'account','0002_email_max_length','2023-04-26 08:07:10.721454'),
(4,'accounts','0002_user_url','2023-04-26 08:07:10.736414'),
(5,'accounts','0003_user_extra_info','2023-04-26 08:07:10.760142'),
(6,'accounts','0004_auto_20200326_1746','2023-04-26 08:07:10.866455'),
(7,'accounts','0005_auto_20200402_1208','2023-04-26 08:07:10.901383'),
(8,'accounts','0006_auto_20200402_1634','2023-04-26 08:07:10.925324'),
(9,'accounts','0007_auto_20210402_1615','2023-04-26 08:07:10.941282'),
(10,'contenttypes','0001_initial','2023-04-26 08:07:10.999094'),
(11,'admin','0001_initial','2023-04-26 08:07:11.036367'),
(12,'admin','0002_logentry_remove_auto_add','2023-04-26 08:07:11.171974'),
(13,'admin','0003_logentry_add_action_flag_choices','2023-04-26 08:07:11.179952'),
(14,'contenttypes','0002_remove_content_type_name','2023-04-26 08:07:11.244779'),
(15,'auth','0001_initial','2023-04-26 08:07:11.335808'),
(16,'auth','0002_alter_permission_name_max_length','2023-04-26 08:07:11.629076'),
(17,'auth','0003_alter_user_email_max_length','2023-04-26 08:07:11.635060'),
(18,'auth','0004_alter_user_username_opts','2023-04-26 08:07:11.641072'),
(19,'auth','0005_alter_user_last_login_null','2023-04-26 08:07:11.646059'),
(20,'auth','0006_require_contenttypes_0002','2023-04-26 08:07:11.650021'),
(21,'auth','0007_alter_validators_add_error_messages','2023-04-26 08:07:11.656004'),
(22,'auth','0008_alter_user_username_max_length','2023-04-26 08:07:11.661988'),
(23,'auth','0009_alter_user_last_name_max_length','2023-04-26 08:07:11.669967'),
(24,'auth','0010_alter_group_name_max_length','2023-04-26 08:07:11.686921'),
(25,'auth','0011_update_proxy_permissions','2023-04-26 08:07:11.695921'),
(26,'auth','0012_alter_user_first_name_max_length','2023-04-26 08:07:11.702903'),
(27,'products','0001_initial','2023-04-26 08:07:12.085163'),
(28,'orders','0001_initial','2023-04-26 08:07:12.888615'),
(29,'billing','0001_initial','2023-04-26 08:07:13.579307'),
(30,'billing','0002_transaction_type','2023-04-26 08:07:13.724401'),
(31,'carts','0001_initial','2023-04-26 08:07:13.809076'),
(32,'django_ses','0001_initial','2023-04-26 08:07:14.072068'),
(33,'products','0002_auto_20200410_1527','2023-04-26 08:07:14.130769'),
(34,'products','0003_auto_20200526_2053','2023-04-26 08:07:14.157554'),
(35,'products','0004_auto_20200601_1052','2023-04-26 08:07:14.165533'),
(36,'products','0005_remove_product_price_params','2023-04-26 08:07:14.183484'),
(37,'products','0005_auto_20200611_1629','2023-04-26 08:07:14.193457'),
(38,'products','0006_merge_20200616_1620','2023-04-26 08:07:14.197447'),
(39,'products','0007_productprice','2023-04-26 08:07:14.242327'),
(40,'products','0008_productcategorytag','2023-04-26 08:07:14.341146'),
(41,'products','0009_productcategory_tags','2023-04-26 08:07:14.387253'),
(42,'products','0010_auto_20200826_1540','2023-04-26 08:07:14.719263'),
(43,'products','0011_productcategorytag_position','2023-04-26 08:07:14.745740'),
(44,'products','0012_auto_20200920_1945','2023-04-26 08:07:14.752722'),
(45,'products','0013_product_unit','2023-04-26 08:07:14.774662'),
(46,'products','0014_product_is_reorderable','2023-04-26 08:07:14.802588'),
(47,'products','0015_auto_20201019_1805','2023-04-26 08:07:15.659818'),
(48,'products','0016_auto_20201127_1411','2023-04-26 08:07:15.933714'),
(49,'products','0017_productoption_image','2023-04-26 08:07:15.955658'),
(50,'products','0018_productoptioncondition_option','2023-04-26 08:07:16.043661'),
(51,'products','0019_easydraft_easydraftprintarea','2023-04-26 08:07:16.176748'),
(52,'products','0020_auto_20201215_1840','2023-04-26 08:07:16.334966'),
(53,'products','0021_auto_20201215_1850','2023-04-26 08:07:16.406975'),
(54,'products','0022_auto_20201222_1651','2023-04-26 08:07:16.449936'),
(55,'products','0023_auto_20210113_1700','2023-04-26 08:07:16.468885'),
(56,'mydesign','0001_initial','2023-04-26 08:07:16.523914'),
(57,'mydesign','0002_mydesigndesign','2023-04-26 08:07:16.709184'),
(58,'orders','0002_order_shipping_total','2023-04-26 08:07:16.797670'),
(59,'orders','0003_auto_20200402_1208','2023-04-26 08:07:16.843547'),
(60,'orders','0004_logorderitemstateupdate','2023-04-26 08:07:16.899398'),
(61,'orders','0005_orderitem_product_slug','2023-04-26 08:07:17.100911'),
(62,'orders','0006_auto_20210331_1409','2023-04-26 08:07:17.285050'),
(63,'notices','0001_initial','2023-04-26 08:07:17.571994'),
(64,'notices','0002_auto_20210512_0917','2023-04-26 08:07:17.985626'),
(65,'orders','0007_auto_20230331_1050','2023-04-26 08:07:18.043472'),
(66,'products','0024_productprice_sample_unit_price','2023-04-26 08:07:18.066184'),
(67,'products','0025_auto_20210302_2211','2023-04-26 08:07:18.204054'),
(68,'products','0026_productprice_sample_lot','2023-04-26 08:07:18.230982'),
(69,'products','0027_product_is_custom_product','2023-04-26 08:07:18.261163'),
(70,'products','0028_productinfo_contact_url','2023-04-26 08:07:18.283811'),
(71,'products','0029_productinfo_can_order_on_site','2023-04-26 08:07:18.313641'),
(72,'products','0030_productexampleimage','2023-04-26 08:07:18.367277'),
(73,'sessions','0001_initial','2023-04-26 08:07:18.455012'),
(74,'sites','0001_initial','2023-04-26 08:07:18.502705'),
(75,'sites','0002_alter_domain_unique','2023-04-26 08:07:18.526614'),
(76,'socialaccount','0001_initial','2023-04-26 08:07:18.728327'),
(77,'socialaccount','0002_token_max_lengths','2023-04-26 08:07:19.104164'),
(78,'socialaccount','0003_extra_data_default_dict','2023-04-26 08:07:19.117129'),
(79,'products','0031_auto_20230426_1735','2023-04-27 02:06:28.259986'),
(81,'casestudies','0001_initial','2023-04-27 02:27:30.951185'),
(82,'casestudies','0002_auto_20230428_0400','2023-04-28 04:00:34.411878'),
(83,'accounts','0008_auto_20230606_1720','2023-06-06 17:20:44.339109'),
(84,'billing','0003_auto_20230606_1720','2023-06-06 17:20:44.363113'),
(85,'carts','0002_auto_20230606_1720','2023-06-06 17:20:44.413067'),
(86,'casestudies','0003_auto_20230606_1720','2023-06-06 17:20:44.480028'),
(87,'mydesign','0003_auto_20230606_1720','2023-06-06 17:20:44.538995'),
(88,'orders','0008_auto_20230606_1720','2023-06-06 17:20:44.616950'),
(89,'casestudies','0004_auto_20230622_1101','2023-06-22 15:29:42.434558'),
(90,'casestudies','0005_auto_20230622_2144','2023-06-22 21:45:19.398831'),
(91,'casestudies','0006_casestudyimage_is_hover_image','2023-06-22 22:05:05.482110');

/*Table structure for table `django_ses_sesstat` */

DROP TABLE IF EXISTS `django_ses_sesstat`;

CREATE TABLE `django_ses_sesstat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `delivery_attempts` int unsigned NOT NULL,
  `bounces` int unsigned NOT NULL,
  `complaints` int unsigned NOT NULL,
  `rejects` int unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `date` (`date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_ses_sesstat` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('2qnck3rzw5561putzcx2x7n42mqqbnhb','.eJxVjDEOgzAMRe_iuYoSF-KEsTtnQE7sNrQVSAGmqndvkVhY_3vvfyBzXaHDCwy8rWXYFq3DKNCBg9OWOL902oE8eXrMJs_TWsdkdsUcdDH9LPq-He7poPBS_jVF31yZ0DmXbAgUKSpKm20U3zBHVKHcIjM5sY1tQ1Cn1qPSPSF7C98fdqg5lw:1ptdA9:wZOMWxFSmycOOgl0Qk3y230rdbBbzBZHrhYwXSwnpPQ','2023-05-16 00:42:33.336525'),
('39qijuis0io367mpvl4zw9jzflpmpll9','.eJxVjEEOwiAQRe8ya0MACwNduu8ZmoEZpWrahNKV8e7apJtu_3vvfyBTbdDjBUbaWhm3Veo4MfRg4LQlyi-Zd8BPmh-Lysvc6pTUrqiDrmpYWN63wz0dFFrLv8bouyuhNcYkHQJGjGLZZR3Zd0TRCmN2lggN6067EMSI9lbwnix5Dd8fegQ5nA:1q55uy:kyWrXQtMtlw7I9bpTdPfvUOYeawGS0fv9AZJoaWMFSA','2023-06-16 16:38:16.698862'),
('3c5b8mmawuyt6wbo6lxq9viktz30qq2m','eyJjYXJ0Ijo0fQ:1pztaG:I6TDDF4jqoUa2bTKR3JRXCP0MTYGHnoiE-cAO8NVHBA','2023-06-02 08:27:24.414040'),
('3z54r1br3tp604d5mpmpidovnbiugdhu','.eJxVjDEOgzAMRe_iuYriFOKEsTtnQE7sNrQVSAGmqndvkVhY_3vvfyBzXaFDvMDA21qGbdE6jAIdIJy2xPml0w7kydNjNnme1jomsyvmoIvpZ9H37XBPB4WX8q8p-ubK5BAx2RAoUlQnbbZRfMMcnQrl1jETim1sG4KiWu-U7smxt_D9AZm9Occ:1q6SHV:IlodDLSMQmk6XZaoHSBbGanrQGCpJve9mttW88GKzxQ','2023-06-20 10:43:09.542245'),
('6vsd7aqtb5wkylw7eml85m0t28h2wpnc','.eJxVjEEOwiAQRe8ya0OAUga6dO8ZyMCMtmraBNqV8e7apJtu_3vvf6BQXWHoLpBoW8e0NalpYhjAwGnLVF4y74CfND8WVZZ5rVNWu6IO2tRtYXlfD_d0MFIb_zVG7zpCa4zJOgSMGMVyX3Rk74iiFcbSWyI0rJ3uQxAj2lvBe7bkNXx_d1Q5mA:1pzKBm:dkeCChOnZwF4oYMA259gX7pIeGjCmVvtKnEpL0qgKLE','2023-05-31 18:39:46.549482'),
('6ykhmoeoxkl1y0z99gbhy9i7rs6fr3me','eyJjYXJ0Ijo1fQ:1q4zXX:LjYuls373zNUg8oPD8f0pAylChxd2xsdne69-WnDGI8','2023-06-16 09:49:39.499545'),
('88wmlbna3c458rav4mtd2dklh8p01h8b','.eJxVjDEOgzAMRe_iuYriNMQJY3fOgJzYLbQVSASmqndvkVhY_3vvf6DwskKL_gI9b-vQb1WXfhRoAeG0ZS4vnXYgT54esynztC5jNrtiDlpNN4u-b4d7Ohi4Dv-aUvBXJoeI2cZIiZI6aYpNEjxzcipUGsdMKNbbJkZFtcEp3bPjYOH7A5vBOco:1q8zO1:hK5gJVdaFS2wl0oTPaHreD7horHzUd8VQmoC6RlkHdw','2023-06-27 10:28:21.874473'),
('8s9t3x6ie3pot8qtrnbmmtdhcik0sv9j','.eJxVjDEOgzAMRe_iuYriFOKEsTtnQE7sNrQVSAGmqndvkVhY_3vvfyBzXaFDf4GBt7UM26J1GAU6QDhtifNLpx3Ik6fHbPI8rXVMZlfMQRfTz6Lv2-GeDgov5V9T9M2VySFisiFQpKhO2myj-IY5OhXKrWMmFNvYNgRFtd4p3ZNjb-H7A50ZOcw:1qCT4q:9XHUdcUgQf-7WoMdMHFAqh96Q3wWL15W2Tox6ktUISs','2023-07-07 00:46:56.809382'),
('99e35gzf80st2dbj8gvlik41f5p8uij5','.eJxVjMsOwiAQRf-FdUMAWx5duvcbyMCMFjXQQJtojP-uTbrQ7T3nnhfzsC6TXxtVn5CNTLLudwsQb5Q3gFfIl8JjyUtNgW8K32njp4J0P-7uX2CCNn3fxun-AEZJKYOw1jjjSOEQhUPdAzhFaOKgAIxE0YvBWpIktCJzDgq02KKNWksle3rMqT7ZKDoWoS5stO8PiutA2g:1q7zVT:nToTkDTpcKayietPCk9_OA2c5HlpG5vVYfExTZ_ehpc','2023-06-24 16:23:55.864188'),
('d655fodfxmf376rrhr86lyxqt1zcbweo','.eJxVjMsOwiAQRf-FdUMAWx5duvcbyMCMFjXQQJtojP-uTbrQ7T3nnhfzsC6TXxtVn5CNTLLudwsQb5Q3gFfIl8JjyUtNgW8K32njp4J0P-7uX2CCNn3fxun-AEZJKYOw1jjjSOEQhUPdAzhFaOKgAIxE0YvBWpIktCJzDgq02KKNWksle3rMqT7ZKDoWoS5stO8PiutA2g:1q79gj:gOXm6XJW4ACkW-T_9YY73lNrQwrMh9nj3yw8gVaKdJ0','2023-06-22 09:04:05.205875'),
('jn11k50c56mo2em0ivr9sufkbrvzq7np','eyJjYXJ0Ijo2fQ:1q4zl4:y0b33IITosx-3Dk89kKmpSk6CtR1itJt2W2Kkb11b1A','2023-06-16 10:03:38.070293'),
('nko8elrj7ne3k10bagi07sucg6kova79','.eJxVjEEOwiAQRe8ya0MACwNduu8ZmoEZpWrahNKV8e7apJtu_3vvfyBTbdDHC4y0tTJuq9RxYujBwGlLlF8y74CfND8WlZe51SmpXVEHXdWwsLxvh3s6KLSWf43Rd1dCa4xJOgSMGMWyyzqy74iiFcbsLBEa1p12IYgR7a3gPVnyGr4_e1w5ng:1q56RC:OwV9R9a2s5EH0nCORXusZwuzGsuYu7xQ9UK8XhTcy-4','2023-06-16 17:11:34.952278'),
('nrqv3kfmk9mdhynj0vif6eqrqipjd6el','eyJjYXJ0IjoxMH0:1q6ADM:1b0GwouqnDJUQBgqdkrRNys-D2A5rq6ob2vNlfOoteo','2023-06-19 15:25:40.686220'),
('u1dbdpdfhlt3jxnvummmwp9d3ib8ofs5','.eJxVjEsOwjAMBe_iNYrikMRJl-x7hsqJDS2gVupnhbg7VOqm2zcz7wOV5xUaDBfoeFv7blt07gaBBhBOW-H60nEH8uTxMZk6jes8FLMr5qCLaSfR9-1wTwc9L_2_phz9lckhYrEpUaasTkK1WaJnzk6FanDMhGK9DSkpqo1O6V4cRwvfH5xtOcs:1qCD3R:0Pb9u-IlVco4lF9j3LeyJ4pSB8tBP4ivFliWP-DOWgY','2023-07-06 07:40:25.544782'),
('varuj6d8v8b26zwm9mvw4at5rz8ade2f','.eJxVjEEOwiAQRe_C2hAYKQNduvcMzcCMUjVtQunKeHfbpAvd_vf-e6uB1laGdZE6jKx6ZdXpd0uUnzLtgB803Wed56nVMeld0Qdd9HVmeV0O9y9QaCnbG6N3Z0Kw1iYTAkaMAtxlE9k7ogjCmDsgQsvGmS4EsWI8CN4SkDdbNFNtqg-fL7IcOZ0:1q56Cq:_grPRUqplxo7UoJsGiG7SB_wk82XjItTLIL-4nM7tco','2023-06-16 16:56:44.022172'),
('xbls4d1kbe9hs0tfla3ykatmgb9nfmh5','.eJxVjDEOAiEQRe9CbQggMGBp7xnIwIyyaiBZdivj3XWTLbT9773_EgnXpaZ18JwmEiehxeF3y1ge3DZAd2y3LktvyzxluSlyp0NeOvHzvLt_BxVH_dYQvT0iGK11ViFAhMiGXFGRvEWMhgmKM4igSVnlQmDNyhuGazbolXh_ALeLNxE:1q55va:-vTp84NDgWqzjv8hbjF5C-YUHyIx76Zd8MhSPj4foms','2023-06-16 16:38:54.442402'),
('zqb0k9kpw1p07wa2mccc8khfb6mdepiv','.eJxVjDEOgzAMRe_iuYriFOKEsTtnQE7sNrQVSAGmqndvkVhY_3vvfyBzXaHDCwy8rWXYFq3DKNABwmlLnF867UCePD1mk-dprWMyu2IOuph-Fn3fDvd0UHgp_5qib65MDhGTDYEiRXXSZhvFN8zRqVBuHTOh2Ma2ISiq9U7pnhx7C98fdfw5lg:1prZHf:YQcX7BSCUTyRulVTeGH0F8-A8FbmK89oEZgL20dFT5c','2023-05-10 08:09:47.509476');

/*Table structure for table `django_site` */

DROP TABLE IF EXISTS `django_site`;

CREATE TABLE `django_site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `django_site` */

insert  into `django_site`(`id`,`domain`,`name`) values 
(3,'example.com','example.com');

/*Table structure for table `mydesign_mydesign` */

DROP TABLE IF EXISTS `mydesign_mydesign`;

CREATE TABLE `mydesign_mydesign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(120) DEFAULT NULL,
  `name` varchar(360) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `size` longtext,
  `image` varchar(100) DEFAULT NULL,
  `read_only_options` longtext,
  `ordered_num` int unsigned NOT NULL,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `mydesign_mydesign_product_id_d0a5ce2f_fk_products_product_id` (`product_id`) USING BTREE,
  KEY `mydesign_mydesign_user_id_5469a04e_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `mydesign_mydesign_product_id_d0a5ce2f_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `mydesign_mydesign_user_id_5469a04e_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `mydesign_mydesign` */

/*Table structure for table `mydesign_mydesigndesign` */

DROP TABLE IF EXISTS `mydesign_mydesigndesign`;

CREATE TABLE `mydesign_mydesigndesign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `mydesign_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `mydesign_id` (`mydesign_id`) USING BTREE,
  CONSTRAINT `mydesign_mydesigndes_mydesign_id_fd7e902c_fk_mydesign_` FOREIGN KEY (`mydesign_id`) REFERENCES `mydesign_mydesign` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `mydesign_mydesigndesign` */

/*Table structure for table `notices_notice` */

DROP TABLE IF EXISTS `notices_notice`;

CREATE TABLE `notices_notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `notices_notice_category_id_006338bc_fk_notices_noticecategory_id` (`category_id`) USING BTREE,
  CONSTRAINT `notices_notice_category_id_006338bc_fk_notices_noticecategory_id` FOREIGN KEY (`category_id`) REFERENCES `notices_noticecategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `notices_notice` */

/*Table structure for table `notices_noticecategory` */

DROP TABLE IF EXISTS `notices_noticecategory`;

CREATE TABLE `notices_noticecategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `icon_path` varchar(100) DEFAULT NULL,
  `post_attachable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `notices_noticecategory_slug_e3b59d54` (`slug`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `notices_noticecategory` */

insert  into `notices_noticecategory`(`id`,`name`,`message`,`slug`,`icon_path`,`post_attachable`) values 
(1,'notice about products','新しい商品に関するお知らせがあります。','notice_product','img/notices/category/icons/notice_product.svg',1),
(2,'data import reminder','デザインの入稿が完了していない商品があります。','notice_upload','img/notices/category/icons/notice_upload.svg',0),
(3,'notice about design comfirmation','入稿したデザインが承認されました。','notice_confirmation','img/notices/category/icons/notice_confirmation.svg',0),
(4,'bank transfer reminder','振込が完了していない商品があります。','notice_bank','img/notices/category/icons/notice_bank.svg',0),
(5,'notice about shipping','商品が発送されました。','notice_delivery','img/notices/category/icons/notice_delivery.svg',0),
(6,'other notice','その他のお知らせがあります。','notice_info','img/notices/category/icons/notice_info.svg',1);

/*Table structure for table `notices_noticepost` */

DROP TABLE IF EXISTS `notices_noticepost`;

CREATE TABLE `notices_noticepost` (
  `notice_ptr_id` int NOT NULL,
  `post_title` varchar(120) NOT NULL,
  `text` longtext NOT NULL,
  `last_edited_at` datetime(6) NOT NULL,
  `published_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`notice_ptr_id`) USING BTREE,
  CONSTRAINT `notices_noticepost_notice_ptr_id_24ac7526_fk_notices_notice_id` FOREIGN KEY (`notice_ptr_id`) REFERENCES `notices_notice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `notices_noticepost` */

/*Table structure for table `notices_noticeread` */

DROP TABLE IF EXISTS `notices_noticeread`;

CREATE TABLE `notices_noticeread` (
  `id` int NOT NULL AUTO_INCREMENT,
  `read_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `notices_id` int NOT NULL,
  `users_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `notices_noticeread_notices_id_043e935a_fk_notices_notice_id` (`notices_id`) USING BTREE,
  KEY `notices_noticeread_users_id_d102a35b_fk_accounts_user_id` (`users_id`) USING BTREE,
  CONSTRAINT `notices_noticeread_notices_id_043e935a_fk_notices_notice_id` FOREIGN KEY (`notices_id`) REFERENCES `notices_notice` (`id`),
  CONSTRAINT `notices_noticeread_users_id_d102a35b_fk_accounts_user_id` FOREIGN KEY (`users_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `notices_noticeread` */

/*Table structure for table `notices_noticereminder` */

DROP TABLE IF EXISTS `notices_noticereminder`;

CREATE TABLE `notices_noticereminder` (
  `notice_ptr_id` int NOT NULL,
  `orderitem_id` int NOT NULL,
  PRIMARY KEY (`notice_ptr_id`) USING BTREE,
  KEY `notices_noticeremind_orderitem_id_9e6b6296_fk_orders_or` (`orderitem_id`) USING BTREE,
  CONSTRAINT `notices_noticeremind_notice_ptr_id_124f3e6f_fk_notices_n` FOREIGN KEY (`notice_ptr_id`) REFERENCES `notices_notice` (`id`),
  CONSTRAINT `notices_noticeremind_orderitem_id_9e6b6296_fk_orders_or` FOREIGN KEY (`orderitem_id`) REFERENCES `orders_orderitem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `notices_noticereminder` */

/*Table structure for table `orders_logorderitemstateupdate` */

DROP TABLE IF EXISTS `orders_logorderitemstateupdate`;

CREATE TABLE `orders_logorderitemstateupdate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prev_val` varchar(514) NOT NULL,
  `val` varchar(514) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `item_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `orders_logorderitems_item_id_a50a2b4f_fk_orders_or` (`item_id`) USING BTREE,
  KEY `orders_logorderitems_user_id_43b186dd_fk_accounts_` (`user_id`) USING BTREE,
  CONSTRAINT `orders_logorderitems_item_id_a50a2b4f_fk_orders_or` FOREIGN KEY (`item_id`) REFERENCES `orders_orderitem` (`id`),
  CONSTRAINT `orders_logorderitems_user_id_43b186dd_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_logorderitemstateupdate` */

/*Table structure for table `orders_order` */

DROP TABLE IF EXISTS `orders_order`;

CREATE TABLE `orders_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(32) NOT NULL,
  `ref_code` varchar(120) NOT NULL,
  `product_total` decimal(10,0) NOT NULL,
  `plate_total` decimal(10,0) NOT NULL,
  `mold_total` decimal(10,0) NOT NULL,
  `tax_total` decimal(10,0) NOT NULL,
  `total` decimal(10,0) NOT NULL,
  `currency` varchar(7) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_charged` tinyint(1) NOT NULL,
  `showed_confirmation` tinyint(1) NOT NULL,
  `extra_info` longtext,
  `stored_request` longtext NOT NULL,
  `user_id` int DEFAULT NULL,
  `shipping_total` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `ref_code` (`ref_code`) USING BTREE,
  KEY `orders_order_user_id_e9b59eb1_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `orders_order_user_id_e9b59eb1_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_order` */

/*Table structure for table `orders_orderbillingaddress` */

DROP TABLE IF EXISTS `orders_orderbillingaddress`;

CREATE TABLE `orders_orderbillingaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(120) DEFAULT NULL,
  `last_name` varchar(120) DEFAULT NULL,
  `postal_code` varchar(12) DEFAULT NULL,
  `prefecture` varchar(12) DEFAULT NULL,
  `city` varchar(120) DEFAULT NULL,
  `building` varchar(120) DEFAULT NULL,
  `tel` varchar(36) DEFAULT NULL,
  `order_id` int NOT NULL,
  `name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `order_id` (`order_id`) USING BTREE,
  CONSTRAINT `orders_orderbillingaddress_order_id_2e2e471a_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_orderbillingaddress` */

/*Table structure for table `orders_orderdeliveryaddress` */

DROP TABLE IF EXISTS `orders_orderdeliveryaddress`;

CREATE TABLE `orders_orderdeliveryaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(120) DEFAULT NULL,
  `last_name` varchar(120) DEFAULT NULL,
  `postal_code` varchar(12) DEFAULT NULL,
  `prefecture` varchar(12) DEFAULT NULL,
  `city` varchar(120) DEFAULT NULL,
  `building` varchar(120) DEFAULT NULL,
  `tel` varchar(36) DEFAULT NULL,
  `order_id` int NOT NULL,
  `name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `order_id` (`order_id`) USING BTREE,
  CONSTRAINT `orders_orderdeliveryaddress_order_id_746ba8b4_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_orderdeliveryaddress` */

/*Table structure for table `orders_orderitem` */

DROP TABLE IF EXISTS `orders_orderitem`;

CREATE TABLE `orders_orderitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ref_code` varchar(120) NOT NULL,
  `product_name` varchar(350) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `prices` longtext,
  `extra_info` longtext,
  `created_at` datetime(6) NOT NULL,
  `payment` varchar(32) NOT NULL,
  `order_id` int NOT NULL,
  `product_id` int DEFAULT NULL,
  `product_slug` varchar(350) DEFAULT NULL,
  `draftprompt_edited_at` datetime(6) DEFAULT NULL,
  `payprompt_edited_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `ref_code` (`ref_code`) USING BTREE,
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`) USING BTREE,
  KEY `orders_orderitem_product_id_afe4254a_fk_products_product_id` (`product_id`) USING BTREE,
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderitem_product_id_afe4254a_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_orderitem` */

/*Table structure for table `orders_orderitemdelivery` */

DROP TABLE IF EXISTS `orders_orderitemdelivery`;

CREATE TABLE `orders_orderitemdelivery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(64) NOT NULL,
  `company` varchar(120) DEFAULT NULL,
  `tracking_code` varchar(120) DEFAULT NULL,
  `shipping_date` date DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `extra_info` longtext,
  `first_name` varchar(120) DEFAULT NULL,
  `last_name` varchar(120) DEFAULT NULL,
  `postal_code` varchar(12) DEFAULT NULL,
  `prefecture` varchar(12) DEFAULT NULL,
  `city` varchar(120) DEFAULT NULL,
  `building` varchar(120) DEFAULT NULL,
  `tel` varchar(36) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address_id` int DEFAULT NULL,
  `item_id` int NOT NULL,
  `name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `item_id` (`item_id`) USING BTREE,
  KEY `orders_orderitemdeli_address_id_b16ed35f_fk_accounts_` (`address_id`) USING BTREE,
  CONSTRAINT `orders_orderitemdeli_address_id_b16ed35f_fk_accounts_` FOREIGN KEY (`address_id`) REFERENCES `accounts_deliveryaddress` (`id`),
  CONSTRAINT `orders_orderitemdelivery_item_id_ca68033f_fk_orders_orderitem_id` FOREIGN KEY (`item_id`) REFERENCES `orders_orderitem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_orderitemdelivery` */

/*Table structure for table `orders_orderitemdesign` */

DROP TABLE IF EXISTS `orders_orderitemdesign`;

CREATE TABLE `orders_orderitemdesign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` varchar(100) DEFAULT NULL,
  `comment` longtext,
  `state` varchar(64) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `item_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `item_id` (`item_id`) USING BTREE,
  CONSTRAINT `orders_orderitemdesign_item_id_5af79a6d_fk_orders_orderitem_id` FOREIGN KEY (`item_id`) REFERENCES `orders_orderitem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_orderitemdesign` */

/*Table structure for table `orders_provisionalorderitemdesign` */

DROP TABLE IF EXISTS `orders_provisionalorderitemdesign`;

CREATE TABLE `orders_provisionalorderitemdesign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `item_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `item_id` (`item_id`) USING BTREE,
  CONSTRAINT `orders_provisionalor_item_id_88753c34_fk_orders_or` FOREIGN KEY (`item_id`) REFERENCES `orders_orderitem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `orders_provisionalorderitemdesign` */

/*Table structure for table `products_easydraft` */

DROP TABLE IF EXISTS `products_easydraft`;

CREATE TABLE `products_easydraft` (
  `id` int NOT NULL AUTO_INCREMENT,
  `slug` varchar(120) NOT NULL,
  `pdf_height` int unsigned NOT NULL,
  `pdf_width` int unsigned NOT NULL,
  `image_height` int unsigned NOT NULL,
  `image_width` int unsigned NOT NULL,
  `product_id` int NOT NULL,
  `pdf_background_color` varchar(32) DEFAULT NULL,
  `pdf_border_color` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_easydraft_product_id_8c1fdffe_fk_products_product_id` (`product_id`) USING BTREE,
  KEY `products_easydraft_slug_e95a5740` (`slug`) USING BTREE,
  CONSTRAINT `products_easydraft_product_id_8c1fdffe_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_easydraft` */

/*Table structure for table `products_easydraftprintarea` */

DROP TABLE IF EXISTS `products_easydraftprintarea`;

CREATE TABLE `products_easydraftprintarea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `area_id` varchar(64) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `is_printable` tinyint(1) NOT NULL,
  `image_pos_start_x` int DEFAULT NULL,
  `image_pos_start_y` int DEFAULT NULL,
  `image_pos_end_x` int DEFAULT NULL,
  `image_pos_end_y` int DEFAULT NULL,
  `pdf_pos_start_x` int DEFAULT NULL,
  `pdf_pos_start_y` int DEFAULT NULL,
  `pdf_pos_end_x` int DEFAULT NULL,
  `pdf_pos_end_y` int DEFAULT NULL,
  `easydraft_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_easydraftpr_easydraft_id_fb2aa2c3_fk_products_` (`easydraft_id`) USING BTREE,
  CONSTRAINT `products_easydraftpr_easydraft_id_fb2aa2c3_fk_products_` FOREIGN KEY (`easydraft_id`) REFERENCES `products_easydraft` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_easydraftprintarea` */

/*Table structure for table `products_product` */

DROP TABLE IF EXISTS `products_product`;

CREATE TABLE `products_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `slug` varchar(120) NOT NULL,
  `overview` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `category_id` int DEFAULT NULL,
  `unit` varchar(12) DEFAULT NULL,
  `is_custom_product` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `slug` (`slug`) USING BTREE,
  KEY `products_product_category_id_9b594869_fk_products_` (`category_id`) USING BTREE,
  CONSTRAINT `products_product_category_id_9b594869_fk_products_` FOREIGN KEY (`category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_product` */

insert  into `products_product`(`id`,`name`,`slug`,`overview`,`created_at`,`updated_at`,`is_active`,`category_id`,`unit`,`is_custom_product`) values 
(1,'テープ付きOPP袋','tape-opp-bag','','2023-04-27 02:19:39.580388','2023-04-27 02:19:39.580388',1,2,NULL,0),
(2,'テープ付きOPP袋','flatbag','','2023-04-27 12:20:28.537592','2023-04-27 12:20:28.537592',1,2,NULL,0),
(4,'青い紙箱','paper-box',NULL,'2023-05-18 09:10:56.000000','2023-05-18 09:11:02.000000',1,4,NULL,1),
(5,'ジッパーバッグ','zipper-bag',NULL,'2023-05-18 09:56:38.000000','2023-05-18 09:56:40.000000',1,8,NULL,1),
(6,'アルミ袋','aluminum-bag',NULL,'2023-05-18 09:59:28.000000','2023-05-18 09:59:30.000000',1,1,NULL,1),
(7,'段ボール','cardboard',NULL,'2023-05-19 02:49:55.000000','2023-05-19 02:49:57.000000',1,7,NULL,1);

/*Table structure for table `products_product_tags` */

DROP TABLE IF EXISTS `products_product_tags`;

CREATE TABLE `products_product_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `producttag_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `products_product_tags_product_id_producttag_id_993adb5c_uniq` (`product_id`,`producttag_id`) USING BTREE,
  KEY `products_product_tag_producttag_id_a60afbb7_fk_products_` (`producttag_id`) USING BTREE,
  CONSTRAINT `products_product_tag_producttag_id_a60afbb7_fk_products_` FOREIGN KEY (`producttag_id`) REFERENCES `products_producttag` (`id`),
  CONSTRAINT `products_product_tags_product_id_f82cb4be_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_product_tags` */

/*Table structure for table `products_product_usecase` */

DROP TABLE IF EXISTS `products_product_usecase`;

CREATE TABLE `products_product_usecase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `productusecase_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `products_product_usecase_product_id_productusecas_1fe86301_uniq` (`product_id`,`productusecase_id`) USING BTREE,
  KEY `products_product_use_productusecase_id_8065b6be_fk_products_` (`productusecase_id`) USING BTREE,
  CONSTRAINT `products_product_use_product_id_3db6d7c4_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_product_use_productusecase_id_8065b6be_fk_products_` FOREIGN KEY (`productusecase_id`) REFERENCES `products_productusecase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_product_usecase` */

/*Table structure for table `products_productcategory` */

DROP TABLE IF EXISTS `products_productcategory`;

CREATE TABLE `products_productcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `slug` varchar(120) NOT NULL,
  `detail` longtext,
  `icon` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `parent_category_id` int DEFAULT NULL,
  `extra_info` longtext,
  `position` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `slug` (`slug`) USING BTREE,
  KEY `products_productcate_parent_category_id_a15b1c75_fk_products_` (`parent_category_id`) USING BTREE,
  CONSTRAINT `products_productcate_parent_category_id_a15b1c75_fk_products_` FOREIGN KEY (`parent_category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productcategory` */

insert  into `products_productcategory`(`id`,`name`,`slug`,`detail`,`icon`,`created_at`,`is_active`,`parent_category_id`,`extra_info`,`position`) values 
(1,'平袋','flatbag','平袋','products/extra/category/ic_nav_film.svg','2023-04-27 02:17:50.857661',1,3,'\"\"',10000),
(2,'インナーバッグ','inner-bag','インナーバッグ','','2023-04-27 02:18:36.258083',1,1,'\"\"',10000),
(3,'root','root','','','2023-04-27 16:48:53.676409',1,NULL,'\"\"',10000),
(4,'紙袋','paper-bag','Made with paper','products/extra/category/ic_nav_paperbox.svg','2023-05-18 07:40:04.762100',1,3,'\"\"',10000),
(5,'青い紙箱','blue-paper-box','for test','products/extra/category/ic_nav_paperbox.svg','2023-05-18 07:42:52.770283',1,4,'\"\"',10000),
(6,'段ボール','cardboard','','products/extra/category/ic_nav_cardboox.svg','2023-05-18 09:23:50.647501',1,3,'\"\"',10000),
(7,'マウスの段ボール','cardboard-mouse','','','2023-05-18 09:24:41.017503',1,6,'\"\"',10000),
(8,'信玄袋','cloth-bag',NULL,NULL,'2023-05-18 09:58:06.000000',1,1,NULL,0);

/*Table structure for table `products_productcategory_tags` */

DROP TABLE IF EXISTS `products_productcategory_tags`;

CREATE TABLE `products_productcategory_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `productcategory_id` int NOT NULL,
  `productcategorytag_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `products_productcategory_productcategory_id_produ_c5043efd_uniq` (`productcategory_id`,`productcategorytag_id`) USING BTREE,
  KEY `products_productcate_productcategorytag_i_4a7b5a8b_fk_products_` (`productcategorytag_id`) USING BTREE,
  CONSTRAINT `products_productcate_productcategory_id_e95f7f84_fk_products_` FOREIGN KEY (`productcategory_id`) REFERENCES `products_productcategory` (`id`),
  CONSTRAINT `products_productcate_productcategorytag_i_4a7b5a8b_fk_products_` FOREIGN KEY (`productcategorytag_id`) REFERENCES `products_productcategorytag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productcategory_tags` */

insert  into `products_productcategory_tags`(`id`,`productcategory_id`,`productcategorytag_id`) values 
(1,4,1),
(2,6,2),
(3,7,2),
(5,8,3);

/*Table structure for table `products_productcategorytag` */

DROP TABLE IF EXISTS `products_productcategorytag`;

CREATE TABLE `products_productcategorytag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `extra_info` longtext,
  `position` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productcategorytag` */

insert  into `products_productcategorytag`(`id`,`name`,`url`,`extra_info`,`position`) values 
(1,'paper tag','https://paper-tag.com','\"\"',10000),
(2,'cardboard tag',NULL,'\"\"',10000),
(3,'flat bag',NULL,NULL,0);

/*Table structure for table `products_productexampleimage` */

DROP TABLE IF EXISTS `products_productexampleimage`;

CREATE TABLE `products_productexampleimage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `example_url` varchar(300) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `position` smallint unsigned NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_productexam_product_id_554ed567_fk_products_` (`product_id`) USING BTREE,
  CONSTRAINT `products_productexam_product_id_554ed567_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productexampleimage` */

/*Table structure for table `products_productimage` */

DROP TABLE IF EXISTS `products_productimage`;

CREATE TABLE `products_productimage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `alt_text` varchar(300) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_id` int NOT NULL,
  `is_hover_image` tinyint(1) NOT NULL,
  `position` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_productimage_product_id_e747596a_fk_products_product_id` (`product_id`) USING BTREE,
  CONSTRAINT `products_productimage_product_id_e747596a_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productimage` */

/*Table structure for table `products_productinfo` */

DROP TABLE IF EXISTS `products_productinfo`;

CREATE TABLE `products_productinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_contact_required` tinyint(1) NOT NULL,
  `can_order_sample` tinyint(1) NOT NULL,
  `min_ordering_quantity` int unsigned NOT NULL,
  `max_ordering_quantity` int unsigned NOT NULL,
  `estimated_shipping_date_first` int unsigned NOT NULL,
  `estimated_shipping_date_repeat` int unsigned NOT NULL,
  `can_select_original_size` tinyint(1) NOT NULL,
  `is_design_necessary` tinyint(1) NOT NULL,
  `is_easy_draft_available` tinyint(1) NOT NULL,
  `notes` longtext,
  `shipping_area` longtext,
  `size_limit` longtext,
  `choosable_color` longtext,
  `product_id` int NOT NULL,
  `contact_url` varchar(200) DEFAULT NULL,
  `can_order_on_site` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `product_id` (`product_id`) USING BTREE,
  CONSTRAINT `products_productinfo_product_id_4374058f_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productinfo` */

insert  into `products_productinfo`(`id`,`is_contact_required`,`can_order_sample`,`min_ordering_quantity`,`max_ordering_quantity`,`estimated_shipping_date_first`,`estimated_shipping_date_repeat`,`can_select_original_size`,`is_design_necessary`,`is_easy_draft_available`,`notes`,`shipping_area`,`size_limit`,`choosable_color`,`product_id`,`contact_url`,`can_order_on_site`) values 
(1,0,0,0,0,0,0,0,1,0,NULL,NULL,NULL,NULL,1,NULL,0),
(2,0,0,0,0,0,0,0,1,0,NULL,NULL,NULL,NULL,2,NULL,0),
(5,0,1,0,0,0,0,0,1,1,NULL,NULL,NULL,NULL,4,NULL,1);

/*Table structure for table `products_productoption` */

DROP TABLE IF EXISTS `products_productoption`;

CREATE TABLE `products_productoption` (
  `id` int NOT NULL AUTO_INCREMENT,
  `slug` varchar(50) NOT NULL,
  `name` varchar(360) NOT NULL,
  `detail` longtext,
  `required` tinyint(1) NOT NULL,
  `position` smallint unsigned NOT NULL,
  `widget_type` varchar(120) DEFAULT NULL,
  `product_id` int NOT NULL,
  `modal_blocks` longtext,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_productopti_product_id_6dc2057d_fk_products_` (`product_id`) USING BTREE,
  KEY `products_productoption_slug_b335eb2f` (`slug`) USING BTREE,
  CONSTRAINT `products_productopti_product_id_6dc2057d_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productoption` */

/*Table structure for table `products_productoptioncondition` */

DROP TABLE IF EXISTS `products_productoptioncondition`;

CREATE TABLE `products_productoptioncondition` (
  `id` int NOT NULL AUTO_INCREMENT,
  `operator` varchar(120) NOT NULL,
  `item_id` int NOT NULL,
  `option_id` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_productopti_item_id_9adf2933_fk_products_` (`item_id`) USING BTREE,
  KEY `products_productopti_option_id_692bedbb_fk_products_` (`option_id`) USING BTREE,
  CONSTRAINT `products_productopti_item_id_9adf2933_fk_products_` FOREIGN KEY (`item_id`) REFERENCES `products_productoptionitem` (`id`),
  CONSTRAINT `products_productopti_option_id_692bedbb_fk_products_` FOREIGN KEY (`option_id`) REFERENCES `products_productoption` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productoptioncondition` */

/*Table structure for table `products_productoptioncondition_values` */

DROP TABLE IF EXISTS `products_productoptioncondition_values`;

CREATE TABLE `products_productoptioncondition_values` (
  `id` int NOT NULL AUTO_INCREMENT,
  `productoptioncondition_id` int NOT NULL,
  `productoptionitem_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `products_productoptionco_productoptioncondition_i_e92ff40e_uniq` (`productoptioncondition_id`,`productoptionitem_id`) USING BTREE,
  KEY `products_productopti_productoptionitem_id_3b291533_fk_products_` (`productoptionitem_id`) USING BTREE,
  CONSTRAINT `products_productopti_productoptionconditi_87b3a0e3_fk_products_` FOREIGN KEY (`productoptioncondition_id`) REFERENCES `products_productoptioncondition` (`id`),
  CONSTRAINT `products_productopti_productoptionitem_id_3b291533_fk_products_` FOREIGN KEY (`productoptionitem_id`) REFERENCES `products_productoptionitem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productoptioncondition_values` */

/*Table structure for table `products_productoptionitem` */

DROP TABLE IF EXISTS `products_productoptionitem`;

CREATE TABLE `products_productoptionitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(360) DEFAULT NULL,
  `delimiter` varchar(8) DEFAULT NULL,
  `value` varchar(360) DEFAULT NULL,
  `detail` longtext,
  `image` varchar(100) DEFAULT NULL,
  `is_default` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_reorderable` tinyint(1) NOT NULL,
  `position` smallint unsigned NOT NULL,
  `option_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `products_productopti_option_id_86faac18_fk_products_` (`option_id`) USING BTREE,
  CONSTRAINT `products_productopti_option_id_86faac18_fk_products_` FOREIGN KEY (`option_id`) REFERENCES `products_productoption` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productoptionitem` */

/*Table structure for table `products_productprice` */

DROP TABLE IF EXISTS `products_productprice`;

CREATE TABLE `products_productprice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `key` varchar(300) DEFAULT NULL,
  `csv` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `product_id` int NOT NULL,
  `refer_to` varchar(120) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `sample_unit_price` double DEFAULT NULL,
  `sample_lot` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `products_productprice_product_id_efef3000_uniq` (`product_id`) USING BTREE,
  CONSTRAINT `products_productprice_product_id_efef3000_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productprice` */

insert  into `products_productprice`(`id`,`key`,`csv`,`created_at`,`updated_at`,`product_id`,`refer_to`,`url`,`sample_unit_price`,`sample_lot`) values 
(1,NULL,'','2023-04-27 02:19:39.582383','2023-04-27 02:19:39.582383',1,'url',NULL,NULL,NULL),
(2,NULL,'','2023-04-27 12:20:28.538588','2023-04-27 12:20:28.538588',2,'url',NULL,NULL,NULL),
(4,NULL,'','2023-05-18 09:13:20.000000','2023-05-18 09:13:23.000000',4,'url',NULL,NULL,NULL);

/*Table structure for table `products_producttag` */

DROP TABLE IF EXISTS `products_producttag`;

CREATE TABLE `products_producttag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `color` varchar(16) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `extra_info` longtext,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_producttag` */

/*Table structure for table `products_productusecase` */

DROP TABLE IF EXISTS `products_productusecase`;

CREATE TABLE `products_productusecase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `slug` varchar(120) NOT NULL,
  `content` longtext,
  `image` varchar(100) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `extra_info` longtext,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `slug` (`slug`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `products_productusecase` */

/*Table structure for table `socialaccount_socialaccount` */

DROP TABLE IF EXISTS `socialaccount_socialaccount`;

CREATE TABLE `socialaccount_socialaccount` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`) USING BTREE,
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_accounts_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `socialaccount_socialaccount` */

/*Table structure for table `socialaccount_socialapp` */

DROP TABLE IF EXISTS `socialaccount_socialapp`;

CREATE TABLE `socialaccount_socialapp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `socialaccount_socialapp` */

/*Table structure for table `socialaccount_socialapp_sites` */

DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;

CREATE TABLE `socialaccount_socialapp_sites` (
  `id` int NOT NULL AUTO_INCREMENT,
  `socialapp_id` int NOT NULL,
  `site_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`) USING BTREE,
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`) USING BTREE,
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `socialaccount_socialapp_sites` */

/*Table structure for table `socialaccount_socialtoken` */

DROP TABLE IF EXISTS `socialaccount_socialtoken`;

CREATE TABLE `socialaccount_socialtoken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int NOT NULL,
  `app_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`) USING BTREE,
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`) USING BTREE,
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

/*Data for the table `socialaccount_socialtoken` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
