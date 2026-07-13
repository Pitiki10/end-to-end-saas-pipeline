
#---------------------------------------------------
#Importamos las librerías necesarias para el analisis
#---------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------
#Comenzamos con la revisión y limpieza del dataset
#---------------------------------------------------
df_customer_reviews = pd.read_csv(r'A:\Escritorio\Proyectos DATA\CRM\end-to-end-saas-pipeline\Raw_Data\customer_reviews_complete.csv')

print('Primeros 10 datos:\n')
print(df_customer_reviews.head(10))

print("\nInformación sobre el DataFrame:\n")
df_customer_reviews.info()

print("\nEstadísticas descriptivas:\n")
print(df_customer_reviews.describe(include='all'))

print("\nComprobando valores nulos:\n")
print(df_customer_reviews.isnull().sum().loc[lambda x: x > 0])

print("\nComprobamos si los nulos de product_name y product son iguales")


print('\nReviews duplicadas:')
if 'review_id' in df_customer_reviews.columns:
    duplicados = df_customer_reviews.duplicated(subset='review_id').sum()
    print(duplicados)
else:
    print('La columna review_id no existe en el DataFrame.')
#---------------------------------------------------
# Al verificar duplicados y nulos, comenzamos con su corrección y depuración.
#---------------------------------------------------

#1. Cargamos la base de datos customers_limpio
customers_limpio = pd.read_csv(r"A:\Escritorio\Proyectos DATA\CRM\end-to-end-saas-pipeline\customers_limpio.csv")

# 2. Creamos el diccionario confiable (ahora sí, sin basura)
diccionario_clientes = customers_limpio.set_index('customer_id')['full_name'].to_dict()

# 3. Rescatamos los nulos mapeando el ID
df_customer_reviews['full_name'] = df_customer_reviews['full_name'].fillna(
    df_customer_reviews['customer_id'].map(diccionario_clientes)
)

print(f"Nulos restantes en full_name: {df_customer_reviews['full_name'].isnull().sum()}")

#---------------------------------------------------
# Los nulos restantes en full_name fueron depurados
#---------------------------------------------------

#----------------------------------------------------------------------------------------------------------
# Traemos la df_transactions, ya que tiene los demás datos que necesitamos para purgar nuestra df objetivo
#----------------------------------------------------------------------------------------------------------
pd.read_csv(r'A:\Escritorio\Proyectos DATA\CRM\end-to-end-saas-pipeline\transactions_limpio.csv')
print('¡Base de datos: transactions_limpio.csv leída con éxito!')

#-------------------------------------------------------------------------------------------
# Ahora, simplemente llamamos las columnas que queremos modificar con um merge (left join)
#-------------------------------------------------------------------------------------------


