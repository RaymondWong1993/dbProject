-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `yummy_item`
--
-- CREATE DATABASE `test` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

DROP TABLE IF EXISTS `yummy_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yummy_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `bookedNumber` int(11) DEFAULT NULL,
  `createTime` datetime DEFAULT NULL,
  `supplier` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yummy_item`
--

LOCK TABLES `yummy_item` WRITE;
/*!40000 ALTER TABLE `yummy_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `yummy_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yummy_order`
--

DROP TABLE IF EXISTS `yummy_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yummy_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createTime` datetime DEFAULT NULL,
  `totalPrice` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `items` text COLLATE utf8_bin,
  `business_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yummy_order`
--

LOCK TABLES `yummy_order` WRITE;
/*!40000 ALTER TABLE `yummy_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `yummy_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yummy_user`
--

DROP TABLE IF EXISTS `yummy_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yummy_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `hashpw` varchar(60) COLLATE utf8_bin DEFAULT NULL,
  `salt` varchar(29) COLLATE utf8_bin DEFAULT NULL,
  `name` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `describe` varchar(1024) COLLATE utf8_bin DEFAULT NULL,
  `contact` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `type` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yummy_user`
--

LOCK TABLES `yummy_user` WRITE;
/*!40000 ALTER TABLE `yummy_user` DISABLE KEYS */;
INSERT INTO `yummy_user` VALUES (1,'burder','burder',NULL,'Burger King','汉堡王,旧译堡加敬,是美国起家的知名国际性速食连锁店.它的海外据点多为私人经营,即特许加盟店.其中,大部分的加盟业者只经营单一店家,少数则自行发展为大型企业.截至财政年度2011年为止,汉堡王已拥有超过12400家连锁据点,分布于73个国家.','','yummy_business'),(2,'jiangnan','jiangnan',NULL,'俏江南','俏江南集团由张兰女士创始于2000年，总部位于北京，旗下品牌包括俏江南品牌餐厅和SUBU两大高端品牌，是中国最具发展潜力、值得信赖的国际餐饮服务管理集团。','','yummy_business'),(3,'sihaiyijia','sihaiyijia',NULL,'四海一家','四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴','','yummy_business'),(4,'guangzhou','guangzhou',NULL,'广州酒家','广州酒家于1939年建立， 改革开放后，广州酒家积极开拓连锁经营，企业规模由原来的一间店发展为包括有6间高级酒家、1个大型食品生产基地及30多间连锁食品商场等在内的大型饮食企业集团，总资产与达4亿多元，在行业中位居全国前列。','','yummy_business'),(5,'jiyejia','jiyejia',NULL,'吉野家','吉野家是一家享有百年历史的著名日本牛肉饭专门店，始创于1899年，在日本筑地鱼市场开设第一间分店。“吉野家”的名字来源于地名，日本的吉野山地区的牛肉饭最为著名，传说是12世纪时候日本名将源义经的爱妾静在掩护义经避难之时，在吉野山把制作牛肉饭的技巧教给了当地居民，于是牛肉饭成为当地的特产美味，“吉野家”之所以这样取名，也是为了说明自己的牛肉饭正宗。','','yummy_business'),(6,'zhengongfu','zhengongfu',NULL,'真功夫','真功夫的品牌形象代言人乃是李小龙宗师在死亡的游戏中的形象的动漫卡通版。真功夫是知名的中式快餐品牌，主打美味、营养的原盅蒸汤、蒸饭，其前身是蔡达标与潘宇海1994年创立于广东东莞的“168”蒸品店，1997年改名为“双种子”，04年改名为“真功夫”。','','yummy_business'),(7,'admin','admin',NULL,'','','','yummy_user');
/*!40000 ALTER TABLE `yummy_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-05-17 18:59:52
