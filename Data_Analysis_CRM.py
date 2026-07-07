
#---------------------------------------------------
#Importamos las liberías necesarias para el analisis
#---------------------------------------------------
from matplotlib.pylab import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------
#Comenzamos con la revisión y limpieza del dataset
#---------------------------------------------------
df = pd.read_csv(r'A:\Escritorio\Proyectos DATA\CRM\archive (3)\customer_reviews_complete.csv')
df_customer_reviews = pd.DataFrame(df)

print('Primeros 10 datos:\n')
print(df_customer_reviews.head(10))

print("Información sobre el DataFrame:\n")
df_customer_reviews.info()

print("Estadísticas descriptivas:\n")
print(df_customer_reviews.describe())

print("Comprobando valores nulos:\n")
print(df_customer_reviews.isnull().sum().loc[lambda x: x > 0])

print('Reviews duplicadas:')
df_limpia = df.duplicated(subset='review_id').sum()
print(df_limpia)
#---------------------------------------------------
# Al verificar duplicados y nulos, comenzamos con su correción y depuración.
#---------------------------------------------------