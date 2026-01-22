import sqlite3 as sql 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
conn = sql.connect('ETL.db')
cursor = conn.cursor()

url = 'https://br.dolarapi.com/v1/cotacoes'
response = requests.get(url)
if response.status_code != 200:
    raise Exception('Erro ao acessar a API')
data = response.json()

tabela = input("""
               
Escolha a tabela que deseja visualizar:
1 - Cotação do Dólar
2 - Cotação do Euro     
3 - Cotação do Peso Argentino
    
               
               """)
while tabela < 3:
    if tabela == 1:
        cursor.execute('SELECT * FROM Cotacao_dolar')
        dados = cursor.fetchall()
        for linha in dados:
            print(linha)
        break
    elif tabela == 2:
        cursor.execute('SELECT * FROM Cotacao_euro')
        dados = cursor.fetchall()
        for linha in dados:
            print(linha)
        break
    elif tabela == 3:
        cursor.execute('SELECT * FROM Peso_argentino')
        dados = cursor.fetchall()
        for linha in dados:
            print(linha)
        break
    else:
        print("Opção inválida. Tente novamente.")
        