
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

