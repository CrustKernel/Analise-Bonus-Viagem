import pandas as pd
from twilio.rest import Client

# Download the helper library from https://www.twilio.com/docs/python/install


# Your Account SID from twilio.com/console
account_sid = "account sid"
# Your Auth Token from twilio.com/console
auth_token  = "auth token"

client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        
        message = client.messages.create(
            body='Hi there',
            from_='insert here',
            to=' insert here'

        print(message.sid)




