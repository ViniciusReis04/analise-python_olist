# Análise de Transações - Dataset Olist (99k pedidos) | Python + SQL

> Projeto end-to-end simulando rotina de Análise de Dados em ambiente bancário: ingestão, tratamento, auditoria e análise de comportamento transacional.

### Pergunta de negócio que respondi:
Como o comportamento de pagamento e a localização impactam a receita e a recorrência de clientes? Análise aplicável a risco, fraude e LTV em bancos e fintechs.

### O que fiz:
- **ETL em Python:** Extração de 9 tabelas CSV, tratamento de nulos, conversão de datas e carga em PostgreSQL via SQLAlchemy
- **Modelagem em SQL:** Criação de schema `olist`, chaves primárias, views analíticas e rotina de auditoria de duplicidade e integridade
- **Análise:** 96.096 transações únicas, R$ 16M em volume transacionado, 3,2% de recorrência, concentração de receita por UF e forma de pagamento

### Principais insights (exemplo):
- 73% do volume concentrado em SP, RJ e MG - risco de concentração
- Boleto tem ticket médio 23% maior, mas maior tempo de confirmação - insight para análise de crédito
- 0,8% de transações com inconsistência de valor - ponto de auditoria

### Stack:
Python (Pandas, SQLAlchemy), PostgreSQL, SQL (Views, Auditoria), Power BI (em andamento)

### Como rodar:
1. `pip install -r requirements.txt`
2. Criar `.env` com `DATABASE_URL`
3. `python src/load_data.py`

### Próximos passos:
- Dashboard de acompanhamento de KPIs de pagamento
- Análise de atraso de entrega como proxy de risco operacional

---
**Autor:** Vinicius Dias - ADS UNIP 2º semestre | Em busca de estágio em Análise de Dados / Risco
www.linkedin.com/in/viniciusreis26 | reisv2877@gmail.com
