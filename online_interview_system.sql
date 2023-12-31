-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: online_interview_system
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('8185ce5f7b08');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `application`
--

DROP TABLE IF EXISTS `application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `application` (
  `AID` int NOT NULL AUTO_INCREMENT,
  `UID` int DEFAULT NULL,
  `PID` int DEFAULT NULL,
  `MID` int DEFAULT NULL,
  `salary` int NOT NULL,
  `introduction` text NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`AID`),
  KEY `MID` (`MID`),
  KEY `PID` (`PID`),
  KEY `UID` (`UID`),
  CONSTRAINT `application_ibfk_1` FOREIGN KEY (`MID`) REFERENCES `meetingroom` (`MID`),
  CONSTRAINT `application_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `position` (`PID`),
  CONSTRAINT `application_ibfk_3` FOREIGN KEY (`UID`) REFERENCES `user` (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
INSERT INTO `application` VALUES (1,1,1,1,10000,'student from SE ',1);
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interviewresult`
--

DROP TABLE IF EXISTS `interviewresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interviewresult` (
  `IRID` int NOT NULL AUTO_INCREMENT,
  `AID` int DEFAULT NULL,
  `answer` text,
  `grade` int NOT NULL,
  `evaluation` text NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`IRID`),
  KEY `AID` (`AID`),
  CONSTRAINT `interviewresult_ibfk_1` FOREIGN KEY (`AID`) REFERENCES `application` (`AID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interviewresult`
--

LOCK TABLES `interviewresult` WRITE;
/*!40000 ALTER TABLE `interviewresult` DISABLE KEYS */;
INSERT INTO `interviewresult` VALUES (3,1,'print(\"Welcome to the expanded view!\")',11,'11111',0);
/*!40000 ALTER TABLE `interviewresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meetingroom`
--

DROP TABLE IF EXISTS `meetingroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meetingroom` (
  `MID` int NOT NULL AUTO_INCREMENT,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`MID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meetingroom`
--

LOCK TABLES `meetingroom` WRITE;
/*!40000 ALTER TABLE `meetingroom` DISABLE KEYS */;
INSERT INTO `meetingroom` VALUES (1,'2023-12-14 14:35:00','2023-12-14 15:35:00',1);
/*!40000 ALTER TABLE `meetingroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `position` (
  `PID` int NOT NULL AUTO_INCREMENT,
  `positionName` varchar(255) NOT NULL,
  `positionDescription` varchar(1000) DEFAULT NULL,
  `positionRequirement` varchar(1000) DEFAULT NULL,
  `salary` int NOT NULL,
  PRIMARY KEY (`PID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES (1,'backend engineer','backend engineer description','backend engineer requirement',10000),(2,'frontend engineer','frontend engineer description','frontend engineer requirement',8000),(3,'network engineer','network engineer Description','network engineer Requirement',20000);
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problem`
--

DROP TABLE IF EXISTS `problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `problem` (
  `ProID` int NOT NULL AUTO_INCREMENT,
  `problemDescription` text NOT NULL,
  `pythonDescription` text NOT NULL,
  `javaDescription` text NOT NULL,
  `pythonTitle` text NOT NULL,
  `javaTitle` text NOT NULL,
  `pythonSolution` text NOT NULL,
  `javaSolution` text NOT NULL,
  `pythonTestCode` text NOT NULL,
  `javaTestCode` text NOT NULL,
  PRIMARY KEY (`ProID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problem`
--

LOCK TABLES `problem` WRITE;
/*!40000 ALTER TABLE `problem` DISABLE KEYS */;
INSERT INTO `problem` VALUES (1,'缁欏畾涓€涓暣鏁版暟缁?nums 鍜屼竴涓洰鏍囧€?target锛岃浣犲湪璇ユ暟缁勪腑鎵惧嚭鍜屼负鐩爣鍊肩殑閭ｄ袱涓暣鏁帮紝骞惰繑鍥炲畠浠殑鏁扮粍涓嬫爣銆?,'绀轰緥:\n杈撳叆: nums = [2, 7, 11, 15], target = 9\n杈撳嚭: [0, 1]\n瑙ｉ噴: nums[0] + nums[1] = 2 + 7 = 9, 鎵€浠ヨ繑鍥?[0, 1]\n','绀轰緥:\n杈撳叆: int[] nums = {2, 7, 11, 15};, int target = 9;\n杈撳嚭: {0,1}}\n瑙ｉ噴: nums[0] + nums[1] = 2 + 7 = 9, 鎵€浠ヨ繑鍥?{0,1}}\n','class Solution:\n    def twoSum(self, nums, target):\n','class Solution {\n    public int[] twoSum(int[] nums, int target) {\n    }\n}','class Solution:\n    def twoSum(self, nums, target):\n        lookup = {}\n        for i, num in enumerate(nums):\n            if target - num in lookup:\n                return [lookup[target - num], i]\n            lookup[num] = i\n        return []\n','class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        Map<Integer, Integer> lookup = new HashMap<>();\n        for (int i = 0; i < nums.length; i++) {\n            if (lookup.containsKey(target - nums[i])) {\n                return new int[] {lookup.get(target - nums[i]), i};\n            }\n            lookup.put(nums[i], i);\n        }\n        return new int[0];\n    }\n}\n','if __name__ == \"__main__\":\n    solution = Solution()\n    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]\n    assert solution.twoSum([3, 2, 4], 6) == [1, 2]\nassert solution.twoSum([3, 3], 6) == [0, 1]\n','public class Main {\n    public static void main(String[] args) {\n        Solution solution = new Solution();\n        assert Arrays.equals(solution.twoSum(new int[] {2, 7, 11, 15}, 9), new int[] {0, 1});\n        assert Arrays.equals(solution.twoSum(new int[] {3, 2, 4}, 6), new int[] {1, 2});\n        assert Arrays.equals(solution.twoSum(new int[] {3, 3}, 6), new int[] {0, 1});\n    }\n}\n'),(2,'缂栧啓涓€涓嚱鏁帮紝鍏朵綔鐢ㄦ槸灏嗚緭鍏ョ殑瀛楃涓插弽杞繃鏉ャ€傝緭鍏ュ瓧绗︿覆浠ュ瓧绗︽暟缁?s 鐨勫舰寮忕粰鍑恒€?,'绀轰緥:\n杈撳叆锛歴 = [\'h\',\'e\',\'l\',\'l\',\'o\']\n杈撳嚭锛歔\'o\',\'l\',\'l\',\'e\',\'h\']\n','绀轰緥:\n杈撳叆锛歋tring[] s =  {\'h\',\'e\',\'l\',\'l\',\'o\'}\n杈撳嚭锛歿\'o\',\'l\',\'l\',\'e\',\'h\'}\n','class Solution:\n    def reverseString(self, s):\n','class Solution {\n    public void reverseString(char[] s) {\n    \n    }\n}','class Solution:\n    def reverseString(self, s):\n        left, right = 0, len(s) - 1\n        while left < right:\n            s[left], s[right] = s[right], s[left]\n            left, right = left + 1, right - 1\n','class Solution {\n    public void reverseString(char[] s) {\n        int left = 0, right = s.length - 1;\n        while (left < right) {\n            char temp = s[left];\n            s[left] = s[right];\n            s[right] = temp;\n            left++;\n            right--;\n        }\n    }\n}\n','if __name__ == \"__main__\":\n    solution = Solution()\n    s1 = [\"h\",\"e\",\"l\",\"l\",\"o\"]\n    solution.reverseString(s1)\n    assert s1 == [\"o\",\"l\",\"l\",\"e\",\"h\"]\n\n    s2 = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]\n    solution.reverseString(s2)\n    assert s2 == [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]\n','public class Main {\n    public static void main(String[] args) {\n        Solution solution = new Solution();\n        char[] s1 = {\'h\', \'e\', \'l\', \'l\', \'o\'};\n        solution.reverseString(s1);\n        assert Arrays.equals(s1, new char[] {\'o\', \'l\', \'l\', \'e\', \'h\'});\n\n        char[] s2 = {\'H\', \'a\', \'n\', \'n\', \'a\', \'h\'};\n        solution.reverseString(s2);\n        assert Arrays.equals(s2, new char[] {\'h\', \'a\', \'n\', \'n\', \'a\', \'H\'});\n    }\n}\n\n'),(3,'缁欏畾涓€涓彧鍖呮嫭 \'(\'锛孿')\'锛孿'{\'锛孿'}\'锛孿'[\'锛孿']\' 鐨勫瓧绗︿覆 s锛屽垽鏂瓧绗︿覆鏄惁鏈夋晥銆俓n\n鏈夋晥瀛楃涓查渶婊¤冻锛歕n\n宸︽嫭鍙峰繀椤荤敤鐩稿悓绫诲瀷鐨勫彸鎷彿闂悎銆俓n宸︽嫭鍙峰繀椤讳互姝ｇ‘鐨勯『搴忛棴鍚堛€?,'绀轰緥:\n杈撳叆锛歴 = \"()\"锛岃緭鍑猴細true\n杈撳叆锛歴 = \"()[]{}\"锛岃緭鍑猴細true\n杈撳叆锛歴 = \"(]\"锛岃緭鍑猴細false\n','绀轰緥:\n杈撳叆锛歴 = \"()\"锛岃緭鍑猴細true\n杈撳叆锛歴 = \"()[]{}\"锛岃緭鍑猴細true\n杈撳叆锛歴 = \"(]\"锛岃緭鍑猴細false\n','class Solution:\n    def isValid(self, s):\n','class Solution {\n    public boolean isValid(String s) {}\n}','class Solution:\n    def isValid(self, s):\n        stack = []\n        mapping = {\")\": \"(\", \"}\": \"{\", \"]\": \"[\"}\n        for char in s:\n            if char in mapping:\n                top_element = stack.pop() if stack else \'#\'\n                if mapping[char] != top_element:\n                    return False\n            else:\n                stack.append(char)\n        return not stack\n','class Solution {\n    public boolean isValid(String s) {\n        Stack<Character> stack = new Stack<>();\n        for (char c : s.toCharArray()) {\n            if (c == \'(\') {\n                stack.push(\')\');\n            } else if (c == \'{\') {\n                stack.push(\'}\');\n            } else if (c == \'[\') {\n                stack.push(\']\');\n            } else if (stack.isEmpty() || stack.pop() != c) {\n                return false;\n            }\n        }\n        return stack.isEmpty();\n    }\n}\n','if __name__ == \"__main__\":\n    solution = Solution()\n    assert solution.isValid(\"()\") == True\n    assert solution.isValid(\"()[]{}\") == True\n    assert solution.isValid(\"(]\") == False\n    assert solution.isValid(\"([)]\") == False\n    assert solution.isValid(\"{[]}\") == True\n','public class Main {\n    public static void main(String[] args) {\n        Solution solution = new Solution();\n        assert solution.isValid(\"()\") == true;\n        assert solution.isValid(\"()[]{}\") == true;\n        assert solution.isValid(\"(]\") == false;\n        assert solution.isValid(\"([)]\") == false;\n        assert solution.isValid(\"{[]}\") == true;\n    }\n}\n'),(4,'缁欏畾涓€涓瓧绗︿覆锛岃浣犳壘鍑哄叾涓笉鍚湁閲嶅瀛楃鐨勬渶闀垮瓙涓茬殑闀垮害銆?,'绀轰緥:\n杈撳叆: \"abcabcbb\"\n杈撳嚭: 3\n瑙ｉ噴: 鍥犱负鏃犻噸澶嶅瓧绗︾殑鏈€闀垮瓙涓叉槸 \"abc\"锛屾墍浠ュ叾闀垮害涓?3銆俓n','绀轰緥:\n杈撳叆: \"abcabcbb\"\n杈撳嚭: 3\n瑙ｉ噴: 鍥犱负鏃犻噸澶嶅瓧绗︾殑鏈€闀垮瓙涓叉槸 \"abc\"锛屾墍浠ュ叾闀垮害涓?3銆俓n','class Solution:\n    def lengthOfLongestSubstring(self, s):\n','class Solution {\n    public int lengthOfLongestSubstring(String s) {\n    }\n}','class Solution:\n    def lengthOfLongestSubstring(self, s):\n        char_map = {}\n        max_length = start = 0\n        for i, char in enumerate(s):\n            if char in char_map and start <= char_map[char]:\n                start = char_map[char] + 1\n            else:\n                max_length = max(max_length, i - start + 1)\n            char_map[char] = i\n        return max_length\n','class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        Map<Character, Integer> charMap = new HashMap<>();\n        int max_length = 0;\n        for (int start = 0, i = 0; i < s.length(); i++) {\n            char ch = s.charAt(i);\n            if (charMap.containsKey(ch)) {\n                start = Math.max(start, charMap.get(ch) + 1);\n            }\n            max_length = Math.max(max_length, i - start + 1);\n            charMap.put(ch, i);\n        }\n        return max_length;\n    }\n}\n','if __name__ == \"__main__\":\n    solution = Solution()\n    assert solution.lengthOfLongestSubstring(\"abcabcbb\") == 3\n    assert solution.lengthOfLongestSubstring(\"bbbbb\") == 1\nassert solution.lengthOfLongestSubstring(\"pwwkew\") == 3\n','public class Main {\n    public static void main(String[] args) {\n        Solution solution = new Solution();\n        assert solution.lengthOfLongestSubstring(\"abcabcbb\") == 3;\n        assert solution.lengthOfLongestSubstring(\"bbbbb\") == 1;\n        assert solution.lengthOfLongestSubstring(\"pwwkew\") == 3;\n    }\n}\n');
/*!40000 ALTER TABLE `problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`UID`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'LZH','pbkdf2:sha256:600000$8RvhOTxB3ocpD9f7$ec59ac84d5757547ab71ee3ca6bc4ab0c29f870a124cd4ae551ff98427f46f7a','13071108606@163.com',2),(2,'CHY','pbkdf2:sha256:600000$tltgO9plFqSm2sDv$03f873eec456ba63c622dca08a4871b48b5cc09fef90de9e9814778a0dcfbb97','1307110@163.com',0),(3,'TJL','pbkdf2:sha256:600000$l751A70mmL4KR4Ic$b6e8037ec535e43a4c3c4bfdfb2c961e6c483c4dbfd87759f280c05838deb6cf','1307@163.com',1),(5,'ZWY','pbkdf2:sha256:600000$T97nw8qsTytE8HUL$3cdfb52aa0f3223b52fa0732ba7b29cbd1fc32c0d560fee8a80b0e20d35e3076','222@222',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-15 21:46:54
