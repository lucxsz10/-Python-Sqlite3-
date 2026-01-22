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

tabela = int(input("""
                   
            Digite o número da tabela que deseja visualizar:
            1 - Cotacao do Dólar
            2 - Cotacao do Euro
            3 - Cotacao do Peso Argentino          
            """))
                  

while tabela < 4:
    if tabela == 1:
        cursor.execute('SELECT venda FROM Cotacao_dolar')
        dados = cursor.fetchall()
        for linha in dados:
            print(f"O valor do Dólar é: {linha}")
        break
    elif tabela == 2:
        cursor.execute('SELECT venda FROM Cotacao_euro')
        dados = cursor.fetchall()
        for linha in dados:
            print(f"O valor do Euro é: {linha}")
        break
    elif tabela == 3:
        cursor.execute('SELECT venda FROM Peso_argentino')
        dados = cursor.fetchall()
        for linha in dados:
            print(f"O valor do Peso Argentino é: {linha}")
        break
    else:
        print("Opção inválida. Tente novamente.")
    


    conn.commit()
    conn.close()