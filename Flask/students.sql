DROP TABLE IF EXISTS `grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE 'grades' (
  'studentID' varchar(30) DEFAULT NULL,
  'surname' varchar(30) DEFAULT NULL,
  'forename' varchar(30) DEFAULT NULL,
  'module_code' varchar(30) DEFAULT NULL,
  'score' int(11) DEFAULT NULL
)  ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grades`
--

LOCK TABLES `grades` WRITE;

INSERT INTO `grades` VALUES ('1','Smith','John','MATH101',85),('2','Jones','Dave','COMP101',93),('3','Bob','Alice','MATH101',50),('4','Alice','Bob','MATH101',66);

/*CREATE TABLE modules
SELECT DISTINCT module_code
FROM grades;

ALTER TABLE modules
ADD moduleName varchar(255) DEFAULT NULL;

INSERT INTO `modules` (moduleName) VALUES ('Mathematics 101'),('Computer Science 101')

CREATE TABLE students
SELECT surname, forename
FROM grades;

ALTER TABLE students
ADD studentID varchar(8) DEFAULT NULL;

INSERT INTO `students` (studentID) VALUES ('1'),('2'),('3'),('4')*/

/*!40000 ALTER TABLE `grades` ENABLE KEYS */;

UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;