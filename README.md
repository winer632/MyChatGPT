# MyChatGPT
# business_type include basic_chat, internet_chat, pdf and so on
# subscription_type include trial，per_month，per_year
# access_key should be unique in the scope of business_type

pip install -r requirements.txt


# Use gunicorn to run jwt_server in production environment  
# client use http://service.bizoe.tech/v1/validity http://service.bizoe.tech/v1/recharge to access the APIs

# Run gunicorn with HTTPS on port 443
# Note that port 443 is a privileged port, so you may need to run the command with sudo or as root user

sudo gunicorn -w 5 -b 0.0.0.0:443 --certfile openssl/server.crt --keyfile openssl/server.key jwt_server:app
