# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:58:55 2024

@author: FERNANDO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos= pd.read_csv('living.csv')
print(datos.info())

print(datos.columns)

#Los 10 países con el costo de vida más alto

top_10_cost_of_living = datos[['Countries', 'Cost of living, 2017']].nlargest(10, 'Cost of living, 2017')

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(top_10_cost_of_living['Countries'], top_10_cost_of_living['Cost of living, 2017'], color='skyblue')
plt.xlabel('Costo de Vida')
plt.title('Top 10 Países con el Costo de Vida Más Alto')
plt.gca().invert_yaxis()
plt.show()


#Los 10 países con el costo de vida más bajo

bottom_10_cost_of_living = datos[['Countries', 'Cost of living, 2017']].nsmallest(10, 'Cost of living, 2017')

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(bottom_10_cost_of_living['Countries'], bottom_10_cost_of_living['Cost of living, 2017'], color='lightgreen')
plt.xlabel('Costo de Vida')
plt.title('Top 10 Países con el Costo de Vida Más Bajo')
plt.gca().invert_yaxis()  # Para que el país con el costo más bajo esté en la parte superior
plt.show()


# Filtrar los datos para obtener solo los países de America
america_countries = datos[datos['Continent'] == 'America'][['Countries', 'Cost of living, 2017']]

# Ordenar los países de América por costo de vida

america_countries = america_countries.sort_values(by='Cost of living, 2017', ascending=False)

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(america_countries['Countries'], america_countries['Cost of living, 2017'], color='coral')
plt.xlabel('Costo de Vida')
plt.title('Costo de Vida en los Países de America')
plt.gca().invert_yaxis()
plt.show()