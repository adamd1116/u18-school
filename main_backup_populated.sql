CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `trip_id` int DEFAULT NULL,
  `seatNumber` longtext NOT NULL,
  `bookingDate` longtext NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `trip_id` (`trip_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`trip_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,1,8,'2','2019-11-10'),(2,1,5,'2','2019-11-12'),(3,2,8,'2','2019-11-11'),(4,3,8,'2','2019-11-02'),(5,4,15,'1','2019-11-06'),(6,4,14,'1','2019-11-03'),(7,5,8,'3','2019-11-11'),(8,5,9,'2','2019-11-07'),(9,6,2,'1','2019-11-07'),(10,6,4,'2','2019-11-08'),(11,7,11,'1','2019-11-05'),(12,7,15,'2','2019-11-07'),(13,8,13,'2','2019-11-12'),(14,8,15,'2','2019-11-14'),(15,9,8,'2','2019-11-04'),(16,10,2,'2','2019-11-15'),(17,10,2,'5','2019-11-08'),(18,11,2,'1','2019-11-07'),(19,11,4,'2','2019-11-08'),(20,12,2,'2','2019-11-09'),(21,12,7,'1','2019-11-14'),(22,13,13,'2','2019-11-04'),(23,13,8,'2','2019-11-01'),(24,14,15,'2','2019-11-02'),(25,15,13,'2','2019-11-09'),(26,16,2,'2','2019-11-02'),(27,17,4,'2','2019-11-03'),(28,17,15,'2','2019-11-07'),(29,18,15,'1','2019-11-04'),(30,18,14,'1','2019-11-01'),(31,19,11,'1','2019-11-13'),(32,20,11,'1','2019-11-05'),(33,21,14,'2','2019-11-05'),(34,22,9,'2','2019-11-11'),(35,23,2,'1','2019-11-13'),(36,23,4,'2','2019-11-13'),(37,24,4,'2','2019-11-15'),(38,25,13,'2','2019-11-13'),(39,25,13,'2','2019-11-13'),(40,26,8,'2','2019-11-07'),(41,27,12,'1','2019-11-11'),(42,28,9,'4','2019-11-07'),(43,28,5,'2','2019-11-03'),(44,29,9,'4','2019-11-06'),(45,30,14,'3','2019-11-05'),(46,31,1,'8','2019-11-11'),(47,32,13,'2','2019-11-11'),(48,32,9,'4','2019-11-12'),(49,33,9,'2','2019-11-06'),(50,34,4,'2','2019-11-11'),(51,34,2,'5','2019-11-15'),(52,35,11,'2','2019-11-15'),(53,36,5,'2','2019-11-04'),(54,38,13,'2','2019-11-06'),(55,39,4,'2','2019-11-10'),(56,39,7,'2','2019-11-04'),(57,40,5,'2','2019-11-09'),(58,40,6,'4','2019-11-06'),(59,41,2,'2','2019-11-11'),(60,41,12,'1','2019-11-09'),(61,42,12,'2','2019-11-05'),(62,42,8,'2','2019-11-02'),(63,43,6,'2','2019-11-06'),(64,44,6,'2','2019-11-04'),(65,44,9,'1','2019-11-04'),(66,45,15,'2','2019-11-14'),(67,45,9,'1','2019-11-10'),(68,46,6,'1','2019-11-08'),(69,46,13,'2','2019-11-09'),(70,47,2,'2','2019-11-09'),(71,48,12,'2','2019-11-07'),(72,48,7,'1','2019-11-05'),(73,49,6,'2','2019-11-14'),(74,50,14,'1','2019-11-02'),(75,50,13,'2','2019-11-01'),(76,51,11,'2','2019-11-14'),(77,52,14,'1','2019-11-03'),(78,52,2,'2','2019-11-04'),(79,54,8,'2','2019-11-12'),(80,54,13,'2','2019-11-10'),(81,53,8,'2','2019-11-10'),(82,55,1,'5','2019-11-05'),(83,55,11,'2','2019-11-10'),(84,56,9,'3','2019-11-10'),(85,56,12,'1','2019-11-01'),(86,57,5,'2','2019-11-04'),(87,57,2,'3','2019-11-01'),(88,58,4,'2','2019-11-14'),(89,58,13,'2','2019-11-03'),(90,59,9,'1','2019-11-01'),(91,59,5,'2','2019-11-05'),(92,60,9,'2','2019-11-06'),(93,60,5,'2','2019-11-12'),(94,61,15,'2','2019-11-09'),(95,62,11,'2','2019-11-02'),(96,63,11,'3','2019-11-08'),(97,63,8,'1','2019-11-12'),(98,64,9,'1','2019-11-03'),(99,64,7,'6','2019-11-15'),(100,65,2,'2','2019-11-15'),(101,65,15,'2','2019-11-02'),(102,67,12,'2','2019-11-12'),(103,67,15,'2','2019-11-13'),(104,66,15,'2','2019-11-14'),(105,66,11,'1','2019-11-10'),(106,68,15,'1','2019-11-12'),(107,69,4,'2','2019-11-08'),(108,69,5,'2','2019-11-04'),(109,70,13,'2','2019-11-09'),(110,70,6,'2','2019-11-01'),(111,71,11,'1','2019-11-02'),(112,72,11,'2','2019-11-05'),(113,73,8,'2','2019-11-06'),(114,73,11,'2','2019-11-07'),(115,74,8,'2','2019-11-03'),(116,74,7,'2','2019-11-12'),(117,75,12,'3','2019-11-09'),(118,75,14,'1','2019-11-05'),(119,76,2,'3','2019-11-08'),(120,77,11,'1','2019-11-01'),(121,78,9,'2','2019-11-12'),(122,78,1,'6','2019-11-03'),(123,79,4,'2','2019-11-14'),(124,79,15,'2','2019-11-02'),(125,80,6,'2','2019-11-01'),(126,80,6,'2','2019-11-07'),(127,81,13,'2','2019-11-10'),(128,81,13,'2','2019-11-15'),(129,82,12,'2','2019-11-08'),(130,83,5,'1','2019-11-14'),(131,84,15,'1','2019-11-03'),(132,84,15,'2','2019-11-06'),(133,85,13,'2','2019-11-11'),(134,86,13,'1','2019-11-15'),(135,87,14,'2','2019-11-01'),(136,88,4,'2','2019-11-15'),(137,89,7,'2','2019-11-06'),(138,89,4,'1','2019-11-01'),(139,90,7,'6','2019-11-04'),(140,91,4,'3','2019-11-03'),(141,92,8,'1','2019-11-03'),(142,93,6,'2','2019-11-10'),(143,93,5,'2','2019-11-13'),(144,94,9,'3','2019-11-11'),(145,95,12,'1','2019-11-02'),(146,96,14,'2','2019-11-13'),(147,97,12,'1','2019-11-08'),(148,97,11,'1','2019-11-02'),(149,98,15,'2','2019-11-13'),(150,99,8,'2','2019-11-09'),(151,99,4,'2','2019-11-08'),(152,1,1,'3','2019-11-20'),(153,99,1,'2','2019-11-20');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach`
--

DROP TABLE IF EXISTS `coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach` (
  `coach_id` int NOT NULL AUTO_INCREMENT,
  `registration` longtext NOT NULL,
  `seatNumber` longtext NOT NULL,
  PRIMARY KEY (`coach_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach`
--

LOCK TABLES `coach` WRITE;
/*!40000 ALTER TABLE `coach` DISABLE KEYS */;
INSERT INTO `coach` VALUES (1,'BA59 NFU','53'),(2,'FR67 RTE','53'),(3,'PJ07 EUN','49'),(4,'S11 VER','85'),(5,'S17 VER','57'),(6,'Y895 RET','49');
/*!40000 ALTER TABLE `coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `firstName` longtext NOT NULL,
  `surname` longtext NOT NULL,
  `AddressLine1` longtext NOT NULL,
  `AddressLine2` longtext,
  `Postcode` longtext NOT NULL,
  `phoneNum` longtext NOT NULL,
  `email` longtext NOT NULL,
  `specialNeed` longtext,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Adam','Redford','65 Rendlesham Road','None','E5 8PJ','(020) 1366 6714','adamredford@yahoo.com','None'),(2,'Adrian','Hadcock','Flat 30','Gill Street','E14 8HG','(020) 6055 6832','adrianhadcock@gmail.com','None'),(3,'Ami','Todeo','Flat 5','4 - 6 Davenant Street','E16 4ST','(020) 8675 5833','amitodeo@gmail.com','None'),(4,'Amii','Polet','24 Marshfield Street','None','E14 3HQ','(020) 0502 2727','amiipolet@gmail.com','None'),(5,'Amy','Swane','Flat 2','122 St Katharines Way','E1W 1UJ','(020) 1137 5241','amyswane@gmail.com','None'),(6,'Anastassia','Geharke','Flat 42','1 Rembrandt Close','E14 3XA','(020) 2467 7001','anastassiageharke@gmail.com','None'),(7,'Andie','Ashley','8 Poppleton Road','None','E11 1LR','(01708) 688377','andieashley@yahoo.com','None'),(8,'Andrew','Roberts','4 Quilter Street','None','E2 7BT','(020) 1751 8130','andrewroberts@gmail.com','None'),(9,'Ann','Hall','2 Gerry Raffles Square','None','E15 1BG','(020) 8607 0642','annhall@gmail.com','None'),(10,'Archy','Goodee','12 Oswald Street','None','E5 0BT','(020) 2021 6041','archygoodee@outlook.com','None'),(11,'Ardith','Eede','28 Camden Road','None','E11 2JP','(01708) 232668','arditheede@gmail.com','None'),(12,'Audrey','Bishop','19 Randolph Road','None','E17 9NR','(020) 0074 1188','audreybishop@gmail.com','None'),(13,'Blinni','Quakley','48 Boundary Road','None','E13 9PR','(01708) 022736','blinniquakley@gmail.com','None'),(14,'Brian','Jeffcoat','Unit 2 Dorma Trading Park','None','E10 7QX','(020) 5885 7761','brianjeffcoat@gmail.com','Suffers from anxiety'),(15,'Cathleen','Brierley','96 Copenhagen Place','None','E14 7DE','(020) 6252 2758','cathleenbrierley@gmail.com','None'),(16,'Christoph','Jolliss','Flat 7','4 Darndale Close','E17 5LH','(020) 5251 6546','christophjolliss@gmail.com','None'),(17,'Cointon','Leal','5 Trevose Road','None','E17 4DS','(01708) 162265','cointonleal@yahoo.com','None'),(18,'Constantine','Ledamun','31B Haroldstone Road','None','E17 7AN','(020) 3660 7787','constantineledamun@gmail.com','None'),(19,'Cornie','Micheu','Flat 6','2 Kings Close','E10 5BB','(020) 6440 7257','corniemicheu@gmail.com','None'),(20,'Cosetta','McWilliams','15 Cedars Avenue','None','E17 7QL','(020) 5485 5387','cosettamcwilliams@outlook.com','Uses a motorised wheelchair'),(21,'Crissie','Klug','142 Leyton Road','None','E15 1DR','(020) 6308 6418','crissieklug@outlook.com','None'),(22,'Daniel','Nicholson','32 Walsingham Road','None','E5 8NF','(020) 6641 8020','danielnicholson@gmail.com','None'),(23,'Danni','Dashkov','Flat 311','4 Westferry Road','E14 8JL','(020) 3432 3562','dannidashkov@gmail.com','None'),(24,'Darren','Hill','14 London Terrace','None','E2 7SQ','(020) 5580 6861','darrenhill@outlook.com','None'),(25,'David','Hesketh','Flat 147','340 The Highway','E1W 3EU','(020) 1875 7542','davidhesketh@yahoo.com','None'),(26,'David','Collins','Flat 401','37 Commercial Road','E1 1LF','(020) 6350 4606','davidcollins@gmail.com','None'),(27,'David','Clarke','87 Park Grove Road','None','E11 4PT','(020) 7458 0770','davidclarke@gmail.com','None'),(28,'Debra','Duke','16 Alma Street','None','E15 1QA','(020) 3860 7850','debraduke@outlook.com','None'),(29,'Derek','Morrow','15 St Johns Road','None','E6 1NW','(01708) 153825','derekmorrow@outlook.com','None'),(30,'Doll','Berfoot','Flat 48','Bromley High Street','E3 3BQ','(020) 6438 3010','dollberfoot@gmail.com','None'),(31,'Duncan','McColl','193 Boleyn Road','None','E7 9QH','(01708) 378271','duncanmccoll@gmail.com','None'),(32,'Eileen','McDermott','30 Ming Street','None','E14 8HT','(020) 3275 8448','eileenmcdermott@gmail.com','None'),(33,'Eilis','Ferrand','Flat 5','110 The Grove','E15 1NR','(020) 7067 2145','eilisferrand@gmail.com','None'),(34,'Eimile','Bruun','Apartment 624','4 Oakland Quay','E14 9EA','(020) 1720 5754','eimilebruun@gmail.com','None'),(35,'Erica','Coaker','14 Sandford Road','None','E6 3QJ','(01708) 556681','ericacoaker@outlook.com','None'),(36,'Fey','Pallent','Flat 3','93 Upper Clapton Road','E5 9BU','(020) 2315 1513','feypallent@gmail.com','None'),(37,'Fiona','Jones','30 Harrington Hill','None','E5 9EY','(020) 5227 2135','fionajones@gmail.com','None'),(38,'Florella','Korous','90A Markhouse Road','None','E17 8BG','(020) 6377 2272','florellakorous@yahoo.com','None'),(39,'Floris','Bosket','98B Mile End Road','None','E1 4UN','(020) 4353 1713','florisbosket@gmail.com','None'),(40,'Freida','Hulburt','14 Canning Road','None','E15 3NW','(020) 4646 5811','freidahulburt@outlook.com','None'),(41,'Galina','McAllaster','Flat 1','Buckhurst Street','E1 5QY','(020) 2687 4114','galinamcallaster@gmail.com','None'),(42,'Godard','Seedman','Flat 10','87 - 91 Hackney Road','E2 8FE','(020) 4452 5786','godardseedman@gmail.com','None'),(43,'Grant','Dawson','Flat 1','Derwent House','E3 4PU','(020) 6671 6468','grantdawson@gmail.com','None'),(44,'Gunar','Hacquel','6 Fulbourne Road','None','E17 4EE','(01708) 631166','gunarhacquel@yahoo.com','None'),(45,'Hattie','Pacquet','7 East Road','None','E15 3QS','(020) 3554 1476','hattiepacquet@yahoo.com','None'),(46,'Hazel','Brookes','18 Woodbine Place','None','E11 2RH','(01708) 253425','hazelbrookes@gmail.com','None'),(47,'Helen','French','108A Vansittart Road','None','E7 0AA','(01708) 778342','helenfrench@outlook.com','None'),(48,'Idalina','Weeke','67 Acacia Road','None','E17 8BN','(020) 1078 8338','idalinaweeke@yahoo.com','None'),(49,'Ileana','Guitton','115 Hatherley Gardens','None','E6 3HD','(01708) 451733','ileanaguitton@outlook.com','None'),(50,'Jeffie','Westcott','Flat 42','78 Kingsland Road','E2 8DP','(020) 2188 0213','jeffiewestcott@gmail.com','None'),(51,'Jeffy','Maidlow','Flat 15','Tiller Road','E14 8PT','(020) 5616 5047','jeffymaidlow@gmail.com','None'),(52,'Joeann','Hayhurst','6 Corbicum','None','E11 1AW','(01708) 075501','joeannhayhurst@yahoo.com','None'),(53,'John','Brown','46 Belgrave Road','None','E11 3QW','(020) 6247 1718','johnbrown@outlook.com','None'),(54,'John','Collinson','122 Keogh Road','None','E15 4NT','(01708) 257222','johncollinson@gmail.com','Registered disabled (mobility)'),(55,'Karen','Angell','Flat 28','Thornfield House','E14 8EW','(020) 2380 3623','karenangell@gmail.com','None'),(56,'Kassey','Braunfeld','65 Desford Road','None','E16 4NJ','(020) 2783 8624','kasseybraunfeld@yahoo.com','None'),(57,'Keith','Germaine','Flat A','35 Poppleton Road','E11 1LP','(01708) 563836','keithgermaine@gmail.com','None'),(58,'Kerwin','Minihane','68A Sixth Avenue','None','E12 5PR','(01708) 618485','kerwinminihane@yahoo.com','None'),(59,'Kincaid','Milner','10 Heatherwood Close','None','E12 5SB','(01708) 662131','kincaidmilner@outlook.com','None'),(60,'Laura','Hancock','Garage 16','Wanstead','E11 1PD','(01708) 850745','laurahancock@gmail.com','None'),(61,'Leonora','Radcliffe','Flat 27','4 Overbury Street','E5 0TF','(020) 7515 6706','leonoraradcliffe@gmail.com','None'),(62,'Lib','Lutsch','67 London Road','None','E13 0DF','(020) 5314 5510','liblutsch@yahoo.com','None'),(63,'Lynda','Bentley','110 Jack Clow Road','None','E15 3AS','(020) 3282 3208','lyndabentley@outlook.com','None'),(64,'Marchelle','McLean','11 Carnarvon Road','None','E10 6DW','(020) 2265 4702','','Onset of dementia'),(65,'Maria','Roche','201 Sixth Avenue','None','E12 5PT','(01708) 587255','mariaroche@gmail.com','None'),(66,'Mark','Fitton','220 Grantham Road','None','E12 5ND','(01708) 787071','markfitton@gmail.com','None'),(67,'Mark','Jordan','Flat 12','3 Brockway Close','E11 4TE','(020) 2000 0025','markjordan@gmail.com','None'),(68,'Maureen','Heal','Flat 4','124 Wapping High Street','E1W 2NJ','(020) 6250 6156','maureenheal@gmail.com','Suffers from anxiety'),(69,'Michael','Gibbons','51 Brookfield Avenue','None','E17 9ER','(020) 0751 1252','michaelgibbons@yahoo.com','None'),(70,'Michal','Krawczyk','Flat 2','White Horse Lane','E1 4QS','(020) 0330 1830','michalkrawczyk@gmail.com','None'),(71,'Mitchell','Noblet','Flat 7','Jackman Street','E8 4QY','(020) 3835 4887','mitchellnoblet@gmail.com','None'),(72,'Nasar','Mahmood','61 Kimberley Avenue','None','E6 3BE','(01708) 122266','nasarmahmood@yahoo.com','None'),(73,'Niki','Sich','6 Belle Vue Lodge','Connaught Avenue','E4 7AB','(01708) 664310','nikisich@yahoo.com','None'),(74,'Philip','Burrough','60 Credon Road','None','E13 9DR','(01708) 407412','philipburrough@yahoo.com','None'),(75,'Remy','Stower','12 Pengelly Apartments','9 Bartlett Mews','E14 3GT','(020) 1257 4614','remystower@outlook.com','None'),(76,'Rica','Hail','40 Shacklewell Lane','None','E8 2EZ','(020) 1140 5414','ricahail@gmail.com','None'),(77,'Richard','Leach','Flat 2','2 New Goulston Street','E1 7PR','(020) 6010 0244','richardhayter@gmail.com','None'),(78,'Richard','Hayter','Apartment 305','24 Goldsmiths Row','E2 8GL','(020) 2037 0576','richardleach@gmail.com','None'),(79,'Roman','MacGorrie','18 Pier Road','None','E16 2LH','(01708) 038568','romanmacgorrie@outlook.com','None'),(80,'Roz','Sclater','Flat 1504','4 Prestons Road','E14 9EX','(020) 2455 7425','rozsclater@gmail.com','None'),(81,'Salvidor','Skelhorn','Ground Floor Flat','53 Upper Clapton Road','E5 8AY','(020) 0117 1403','salvidorskelhorn@gmail.com','None'),(82,'Samantha','Kenyon','Flat 4','Kerbey Street','E14 6AP','(020) 7274 3445','samanthakenyon@gmail.com','None'),(83,'Sandor','Krystek','292 High Road Leyton','None','E10 5PW','(020) 6500 5168','sandorkrystek@gmail.com','None'),(84,'Shelagh','Bickham','Quay House','2 Admirals Way','E14 9XG','(020) 1137 2688','shelaghbickham@gmail.com','None'),(85,'Shelley','De la Perrelle','Flat 20','Wolffe Gardens','E15 4JL','(020) 5656 7446','shelleyde la perrelle@gmail.com','None'),(86,'Sileas','Hoy','24 Blanche Street','None','E16 4JR','(020) 7864 7021','sileashoy@gmail.com','None'),(87,'Sinclare','Wooder','5 Shaw Square','None','E17 5JB','(020) 4718 4008','sinclarewooder@gmail.com','None'),(88,'Stan','McGettigan','3 Sanctuary Mews','None','E8 3BD','(020) 3620 8035','stanmcgettigan@gmail.com','None'),(89,'Stephen','Norman','181 Colchester Road','None','E10 6HG','(020) 2421 7324','stephennorman@gmail.com','None'),(90,'Steven','Dolan','314 The Loft Westfield Stratford City','Montfichet Road','E20 1ET','(020) 5526 5858','stevendolan@gmail.com','None'),(91,'Susan','Jackson','116 Osborne Road','None','E7 0PL','(01708) 061143','susanjackson@outlook.com','None'),(92,'Terence','Harris','16 Higham Hill Road','None','E17 6ER','(020) 7323 1357','terenceharris@outlook.com','None'),(93,'Timothy','Cargill','28 Kingspark Court','None','E18 2DD','(01708) 860127','timothycargill@gmail.com','None'),(94,'Tommie','Kollaschek','10B Stondon Walk','None','E6 1LZ','(01708) 787665','tommiekollaschek@outlook.com','None'),(95,'Tracy','Dunn','48 Taeping Street','None','E14 9UT','(020) 8056 1866','tracydunn@gmail.com','None'),(96,'Vanessa','Seeger','183 Shrewsbury Road','None','E7 8QH','(01708) 422082','vanessaseeger@gmail.com','Registered disabled (blind)'),(97,'Wayland','Jeroch','26 Turner Street','None','E1 2AS','(020) 0406 8870','waylandjeroch@gmail.com','None'),(98,'Winfield','Wogan','8 Widdin Street','None','E15 4RY','(020) 5516 6306','winfieldwogan@yahoo.com','Needs to sit near front'),(99,'Zak','Kuhl','12 Mornington Road','None','E11 3BE','(01708) 744712','zakkuhl@outlook.com','None');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destination`
--

DROP TABLE IF EXISTS `destination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destination` (
  `destination_id` int NOT NULL AUTO_INCREMENT,
  `destName` longtext NOT NULL,
  `hotelName` longtext,
  PRIMARY KEY (`destination_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination`
--

LOCK TABLES `destination` WRITE;
/*!40000 ALTER TABLE `destination` DISABLE KEYS */;
INSERT INTO `destination` VALUES (1,'Bicester Village',''),(2,'Calais Shopping Trip',''),(3,'Cardiff the Welsh Capital','Royal Welsh'),(4,'Chester - Roman Trip','Grosvenor'),(5,'Edinburgh Hogmanay','Hilton'),(6,'Lakeside Shopping','Hilton'),(7,'Lincoln Xmas Market','White Hart'),(8,'Norwich',''),(9,'Salisbury',''),(10,'Sunny Brighton',''),(11,'Torquay Break','The Cliffdown'),(12,'Winchester',''),(13,'York City Visit','Fenland Hotel');
/*!40000 ALTER TABLE `destination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver` (
  `driver_id` int NOT NULL AUTO_INCREMENT,
  `firstName` longtext NOT NULL,
  `secondName` longtext NOT NULL,
  PRIMARY KEY (`driver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (1,'Deepak','Gautam'),(2,'Doug','Flenn'),(3,'Pat','Holbrook'),(4,'Rob','Douglas'),(5,'Susanne','Mccorvey');
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS `trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip` (
  `trip_id` int NOT NULL AUTO_INCREMENT,
  `destination_id` int NOT NULL,
  `personCost` longtext NOT NULL,
  `startDate` longtext NOT NULL,
  `duration` longtext NOT NULL,
  `coach_id` int DEFAULT NULL,
  `driver_id` int DEFAULT NULL,
  PRIMARY KEY (`trip_id`),
  KEY `driver_id` (`driver_id`),
  KEY `destination_id` (`destination_id`),
  KEY `coach_id` (`coach_id`),
  CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`),
  CONSTRAINT `trip_ibfk_2` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`),
  CONSTRAINT `trip_ibfk_3` FOREIGN KEY (`coach_id`) REFERENCES `coach` (`coach_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES `trip` WRITE;
/*!40000 ALTER TABLE `trip` DISABLE KEYS */;
INSERT INTO `trip` VALUES (1,1,'30','2019-12-23','1',6,2),(2,2,'39','2019-12-23','1',2,2),(3,2,'39','2020-01-23','1',2,4),(4,3,'299','2019-12-30','3',1,5),(5,4,'199','2019-12-31','2',5,1),(6,5,'399','2019-12-30','3',4,3),(7,6,'20','2019-12-20','1',3,3),(8,7,'199','2019-12-19','2',4,5),(9,8,'20','2020-02-29','1',6,4),(10,8,'20','2020-04-01','1',6,4),(11,9,'27','2019-12-16','1',2,4),(12,10,'25','2020-01-01','1',5,3),(13,11,'299','2020-02-01','3',1,5),(14,12,'27','2019-12-15','1',3,2),(15,13,'299','2020-02-01','3',2,3),(17,2,'12330','2011-11-11','2',2,2),(18,2,'100','2012-12-12','50',2,2);
/*!40000 ALTER TABLE `trip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-20 21:26:39
