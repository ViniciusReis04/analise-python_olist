import pandas as pd

# Carrega os dados
df = pd.read_csv('dados/olist_orders_dataset.csv')

print("Arquivo lido com sucesso!")
print(f"Tem {len(df)} linhas")
print(df.head())

print("\n--- PRIMEIRA ANÁLISE ---")
print(df['order_status'].value_counts())