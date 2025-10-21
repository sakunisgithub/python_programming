import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customer_ids = set(customers['id']) - set(orders['customerId'])
    return customers.loc[customers['id'].isin(customer_ids), ['name']].rename(columns = {'name' : 'Customers'})