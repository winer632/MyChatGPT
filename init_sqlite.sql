-- SQLite does not support the AUTO_INCREMENT keyword.
-- It uses the AUTOINCREMENT keyword as part of the INTEGER PRIMARY KEY declaration.
-- Also, VARCHAR fields do not need a length specified in SQLite.

CREATE TABLE account (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id TEXT,
  business_type TEXT,
  access_key TEXT,
  -- SQLite does not support the DECIMAL data type with precision and scale.
  -- You can use REAL for storing floating-point numbers or NUMERIC for arbitrary precision.
  recharge_amount REAL DEFAULT 0.00,
  -- SQLite uses CURRENT_TIMESTAMP for the default timestamp.
  expiration_date TEXT DEFAULT CURRENT_TIMESTAMP,
  last_login_time TEXT,
  chat_count INTEGER NOT NULL DEFAULT 0,
  client_reference_id INTEGER,
  email TEXT,
  phone TEXT,
  reserved_1 TEXT,
  reserved_2 TEXT
);

-- For indexing a column, you need to create the index after the table has been created.
CREATE INDEX idx_access_key ON account (access_key);

CREATE TABLE product (
  product_id TEXT DEFAULT NULL,
  business_type TEXT DEFAULT NULL,
  subscription_type TEXT DEFAULT NULL,
  -- SQLite supports the REAL data type for floating-point numbers.
  unit_fee REAL DEFAULT 0,
  unit_validity_time INTEGER DEFAULT 0,
  reserved_1 TEXT DEFAULT NULL,
  reserved_2 TEXT DEFAULT NULL
);

CREATE TABLE settings (
  chat_count_setting INTEGER DEFAULT 50
);

-- The INSERT statements remain the same as they are compatible with SQLite.
INSERT INTO `product` VALUES ('prod_O2DnzwF8ZK5VJ0','basic_chat','trial',400.00,86400,NULL,NULL),('prod_O1fiOSsJRrZUjU','basic_chat','per_year',20000.00,31536000,NULL,NULL),('prod_PNGG48oMxPNetE','basic_chat','per_month',3000.00,2592000,NULL,NULL);
-- ... (other INSERT statements follow the same pattern and remain unchanged)
INSERT INTO `settings` VALUES (60);

INSERT INTO `account` VALUES (3,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NKZZmCMTeU4V8Iq1VpRo27R',6000.00,'2024-06-18 04:21:40','2023-06-19 04:21:40',0,NULL,NULL,NULL,NULL,NULL),(17,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NLlsxCMTeU4V8Iq0JzyqIva',6000.00,'2024-06-21 11:42:48','2023-06-22 11:42:48',0,NULL,NULL,NULL,NULL,NULL),(20,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NLyqoCMTeU4V8Iq0RQA5TGE',6000.00,'2024-06-22 01:32:29','2023-06-23 01:32:29',0,NULL,NULL,NULL,NULL,NULL),(25,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NMnhbCMTeU4V8Iq02PVh5BY',6000.00,'2024-06-24 07:50:56','2023-06-25 07:50:56',9,NULL,NULL,NULL,NULL,NULL),(28,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NN5hhCMTeU4V8Iq1zQDewtq',6000.00,'2024-06-25 03:03:57','2023-06-26 03:03:57',0,NULL,NULL,NULL,NULL,NULL),(29,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNBMcCMTeU4V8Iq1gOQn9DE',6000.00,'2024-06-25 09:06:40','2023-06-26 09:06:40',0,NULL,NULL,NULL,NULL,NULL),(32,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNX6ZCMTeU4V8Iq02Fkv8D9',6000.00,'2024-06-26 08:19:58','2023-06-27 08:19:58',11,NULL,NULL,NULL,NULL,NULL),(33,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNr50CMTeU4V8Iq1PmCQoA5',6000.00,'2024-06-27 05:39:33','2023-06-28 05:39:33',0,NULL,NULL,NULL,NULL,NULL),(34,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NNr4jCMTeU4V8Iq1Ohzqsky',6000.00,'2024-06-27 05:42:33','2023-06-28 05:42:33',0,NULL,NULL,NULL,NULL,NULL),(37,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NpPBtCMTeU4V8Iq0o1NLDNF',20000.00,'2024-09-12 13:33:02','2023-09-13 00:46:18',0,NULL,NULL,NULL,NULL,NULL),(39,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3O5P65CMTeU4V8Iq0yExGzjR',20000.00,'2024-10-26 03:52:56','2023-10-27 03:52:56',0,NULL,NULL,NULL,NULL,NULL),(40,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NG9fCCMTeU4V8Iq8K9ebIaJ',6000.00,'2024-06-27 05:22:02','2023-06-27 05:22:02',32,NULL,NULL,NULL,NULL,NULL),(41,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NXyRjCMTeU4V8Iq0dfEuQJ7',20000.00,'2024-07-26 12:22:02','2023-07-26 12:22:02',0,NULL,NULL,NULL,NULL,NULL),(42,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NfeaNCMTeU4V8Iq0frdmvXl',20000.00,'2024-08-16 12:22:02','2023-08-16 12:22:02',5,NULL,NULL,NULL,NULL,NULL),(43,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3NvAs2CMTeU4V8Iq0l9DQvtk',20000.00,'2024-09-28 12:00:00','2023-09-28 12:00:00',0,NULL,NULL,NULL,NULL,NULL),(44,'prod_O1fiOSsJRrZUjU','basic_chat','pi_3OSgZfCMTeU4V8Iq0vpaujo0',20000.00,'2025-01-02 10:00:00','2024-01-02 10:00:00',0,NULL,NULL,NULL,NULL,NULL),(45,'prod_PNGG48oMxPNetE','basic_chat','pi_3OYgQ6CMTeU4V8Iq0Xbfghyk',3000.00,'2024-02-14 03:01:47','2024-01-15 03:01:47',12,NULL,NULL,NULL,NULL,NULL);
