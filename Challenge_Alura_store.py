import pandas as pd
from matplotlib.cbook import index_of

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url) 
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

def Analisis_De_facturacion(tiend):
    suma_ingresos_por_tienda=sum(tiend['Precio'])
    return suma_ingresos_por_tienda


print(Analisis_De_facturacion(tienda))
print(tienda.columns)
registros=[tienda,tienda2,tienda3,tienda4]
tiendas=['tienda1','tienda2','tienda3','tienda4']

Ingresos_totales_por_tienda= {tiendas[i]:Analisis_De_facturacion(registros[i]) for i in range(len(tiendas))}
print(Ingresos_totales_por_tienda)

def calificacion_promedio(t):
    valoracion=sum(t['Calificación'])/len(t['Calificación'])
    return valoracion

Calificación_por_tienda={tiendas[i]:round(calificacion_promedio(registros[i]),2) for i in range(len(tiendas))}
print(Calificación_por_tienda)

def mas_populares(df):
    top3 = df.nlargest(3, 'Cantidad de cuotas')
    resultado = list(zip(top3['Categoría del Producto'], top3['Cantidad de cuotas'].astype(int)))
    return resultado
productos_mas_populares={tiendas[i]:mas_populares(registros[i]) for i in range(len(registros))}

print(productos_mas_populares)

mas_tienda2=max(tienda2['Cantidad de cuotas'])


def mas_vendidos(list_1):
    indice_max = list_1['Cantidad de cuotas'].idxmax()
    valor_max=[list_1.loc[indice_max, 'Categoría del Producto'],int(list_1.loc[indice_max, 'Cantidad de cuotas'])]
    return valor_max

def menos_vendidos(list_2):
    indice_min=list_2['Cantidad de cuotas'].idxmin()
    valor_min=[list_2.loc[indice_min, 'Categoría del Producto'],int(list_2.loc[indice_min, 'Cantidad de cuotas'])]
    return valor_min

productos_mas_menos= {tiendas[i]:[mas_vendidos(registros[i]),menos_vendidos(registros[i])] for i in range(len(tiendas))}
print(productos_mas_menos)


def envio_promedio(lista):
    valor_promedio_de_envio=sum(lista['Costo de envío'])/len(lista['Costo de envío'])
    return valor_promedio_de_envio

costos_de_envio_promedio={tiendas[i]:round(envio_promedio(registros[i]),2) for i in range(len(registros))}
print(costos_de_envio_promedio)

import matplotlib.pyplot as plt
plt.figure()
plt.bar(x=Ingresos_totales_por_tienda.keys(), height=Ingresos_totales_por_tienda.values(),color='#f4d03f')
plt.title('Ingresos totales por tienda', fontsize=16, color='darkred')
plt.xlabel('Tiendas', fontsize=15,color='green')
plt.ylabel('Ventas', fontsize=16,color='red')
# Fondo
plt.gca().set_facecolor('#c39bd3')  # cambia el color de fondo del área del gráfico
# Mostrar cuadrícula
plt.grid(True, linestyle='--', linewidth=0.5, axis='y')


plt.figure()
plt.plot(list(Calificación_por_tienda.keys()), list(Calificación_por_tienda.values()), color='#2ecc71')
plt.title('Calificaciones promedio',fontsize=16,color='darkred')
plt.xlabel('Tiendas',fontsize=15,color='green')
plt.ylabel('Calificación',fontsize=16,color='red')
plt.gca().set_facecolor('#85929e')
plt.grid(True, linestyle='--', linewidth=0.5, axis='y')

plt.figure()
plt.bar(x=costos_de_envio_promedio.keys(), height=costos_de_envio_promedio.values(),color='#224ee5')
plt.title('Costos promedio por envio', fontsize=16, color='darkred')
plt.xlabel('Tiendas', fontsize=15,color='green')
plt.ylabel('Costos', fontsize=16,color='red')
# Fondo
plt.gca().set_facecolor('#a6bdb7')  # cambia el color de fondo del área del gráfico
# Mostrar cuadrícula
plt.grid(True, linestyle='--', linewidth=0.5, axis='y')


x = list(productos_mas_menos.keys())
mas = [v[0][1] for v in productos_mas_menos.values()]
menos = [v[1][1] for v in productos_mas_menos.values()]
etiquetas_mas = [v[0][0] for v in productos_mas_menos.values()]
etiquetas_menos = [v[1][0] for v in productos_mas_menos.values()]

ancho = 0.35
pos = range(len(x))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(pos, mas, width=ancho, color='forestgreen', label='Más vendido')
ax.bar([p + ancho for p in pos], menos, width=ancho, color='crimson', label='Menos vendido')

ax.set_xticks([p + ancho/2 for p in pos])
ax.set_xticklabels(x)
ax.set_ylabel('Cantidad')
ax.set_title('Productos más y menos vendidos por tienda')
ax.legend()


for i in range(len(x)):
    ax.text(pos[i], mas[i] + 0.5, etiquetas_mas[i], ha='center', fontsize=9 )
    ax.text(pos[i] + ancho, menos[i] + 0.5, etiquetas_menos[i], ha='center', fontsize=9)
plt.gca().set_facecolor('#a6bdb7')
plt.tight_layout()
plt.show()

#Teniendo en cuenta el analisis previamente realizado se llego a la conclusion que la tienda que se debera vender es la tienda numero 4 debido a que esta en varios aspectos de los cuales se tomaron en cuenta
#para este analisis, resulto ser la tienda con las ventas mas bajas, y si bien los costos por envio son menores, la calificacion y los productos más vendidos no son favorables para esta tienda
