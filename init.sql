CREATE TABLE account (
  id int PRIMARY KEY AUTO_INCREMENT,
  product_id varchar(80),
  business_type varchar(80),
  access_key varchar(255),
  recharge_amount decimal(10,2) DEFAULT 0.00,
  expiration_date datetime DEFAULT CURRENT_TIMESTAMP,
  last_login_time datetime,
  chat_count int NOT NULL DEFAULT 0,
  client_reference_id int,
  email varchar(80),
  phone varchar(80),
  reserved_1 varchar(80),
  reserved_2 varchar(80),
  INDEX access_key (access_key)
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


CREATE TABLE settings (
  chat_count_setting INT DEFAULT 50
);

# cny, hkd, usd, eur have fractions or cents, so you need to multiply the amount by 100 when using them with Stripe. 
# For example, if you want to charge 10 CNY, you need to set the amount to 1000.
# 4 CNY for 15 minutes, 20 CNY for 1 month, 200 CNY for 1 year

# product environment
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DnzwF8ZK5VJ0", "basic_chat", "trial", 400, 86400);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_PNGG48oMxPNetE", "basic_chat", "per_month", 3000, 2592000);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O1fiOSsJRrZUjU", "basic_chat", "per_year", 20000, 31536000);

# test environment
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DmW5dfkzy20h", "basic_chat", "trial", 400, 86400);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O2DlrcVr01dqOX", "basic_chat", "trial", 500, 604800);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O22ExVNaXKhT9F", "basic_chat", "per_month", 1000, 2592000);
INSERT INTO product (product_id, business_type, subscription_type, unit_fee, unit_validity_time) VALUES ("prod_O22Dzh2L54hASR", "basic_chat", "per_year", 6000, 31536000);


INSERT INTO settings (chat_count_setting) VALUES (50);