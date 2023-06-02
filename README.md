# MyChatGPT
# business_type include basic_chat, internet_chat, pdf and so on
# subscription_type include trial，per_month，per_year
# access_key should be unique in the scope of business_type

pip install -r requirements.txt


# run jwt_server with this command on Azure virtual machine
# client will use http://service.bizoe.tech/v1/xxx to access the API jwt_server provided

azureuser@MyChatGPT:~/gpt/MyChatGPT$ sudo gunicorn -w 5 -b :80 jwt_server:app

