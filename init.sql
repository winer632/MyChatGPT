CREATE TABLE account (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id VARCHAR(80) DEFAULT NULL,
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


CREATE TABLE product (
  product_id VARCHAR(80) DEFAULT NULL,
  business_type VARCHAR(80) DEFAULT NULL,
  subscription_type VARCHAR(80) DEFAULT NULL,
  unit_fee DECIMAL(10,2) DEFAULT 0,
  unit_validity_time INT DEFAULT 0,
  reserved_1 VARCHAR(80) DEFAULT NULL,
  reserved_2 VARCHAR(80) DEFAULT NULL
);


# cny, hkd, usd, eur have fractions or cents, so you need to multiply the amount by 100 when using them with Stripe. 
# For example, if you want to charge 10 CNY, you need to set the amount to 1000.
# 4 CNY for 15 minutes, 20 CNY for 1 month, 200 CNY for 1 year

# product environment
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DnzwF8ZK5VJ0", "basic_chat", "trial", 400, 86400);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O1fjN9tEctwBk9", "basic_chat", "trial", 1000, 604800);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O1fjBZzo9dChqI", "basic_chat", "per_month", 2000, 2592000);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O1fiOSsJRrZUjU", "basic_chat", "per_year", 20000, 31536000);

# test environment
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DmW5dfkzy20h", "basic_chat", "trial", 400, 86400);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DlrcVr01dqOX", "basic_chat", "trial", 1000, 604800);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O22ExVNaXKhT9F", "basic_chat", "per_month", 2000, 2592000);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O22Dzh2L54hASR", "basic_chat", "per_year", 20000, 31536000);
