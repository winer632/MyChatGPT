CREATE TABLE account (
  id INT AUTO_INCREMENT PRIMARY KEY,
  business_model_id INT DEFAULT 1,
  business_type VARCHAR(80) DEFAULT NULL,
  access_key VARCHAR(255) DEFAULT NULL,
  recharge_amount DECIMAL(10,2) DEFAULT 0,
  expiration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  last_login_time DATETIME DEFAULT NULL,
  client_reference_id INT DEFAULT NULL,
  email VARCHAR(80) DEFAULT NULL,
  phone VARCHAR(80) DEFAULT NULL,
  reserved_1 VARCHAR(80) DEFAULT NULL,
  reserved_2 VARCHAR(80) DEFAULT NULL
);


CREATE TABLE business_model (
  id INT AUTO_INCREMENT PRIMARY KEY,
  business_type VARCHAR(80) DEFAULT NULL,
  subscription_type VARCHAR(80) DEFAULT NULL,
  unit_fee DECIMAL(10,2) DEFAULT 0,
  unit_validity_time INT DEFAULT 0,
  reserved_1 VARCHAR(80) DEFAULT NULL,
  reserved_2 VARCHAR(80) DEFAULT NULL
);




INSERT INTO business_model (business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("basic_chat", "trial", 2, 900);
INSERT INTO business_model (business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("basic_chat", "per_month", 20, 2592000);
INSERT INTO business_model (business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("basic_chat", "per_year", 200, 31536000);