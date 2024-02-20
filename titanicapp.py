import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title(F'Visualización Titanic {"🚢"}')

df=pd.read_csv('train.csv')

Class = st.selectbox('SELECCIONA UNA CLASE', ['💵', '💵💵', '💵💵💵'])

if Class == '💵💵💵':
    seleccionar_clase=1

elif Class == '💵💵':
    seleccionar_clase=2

elif Class == '💵':
    seleccionar_clase=3

# Filtrar el DataFrame según la clase seleccionada
df_filtered_clase = df[df['Pclass'] == seleccionar_clase]

# Plot de edades
st.markdown('*EDADES*')
fig_edad, ax_edad = plt.subplots()
bins=[0,10,20,30,40,50,60,70,80]
sns.histplot(data=df_filtered_clase, x='Age', color='#b4bd84', bins=bins, ax=ax_edad)
ax_edad.set_title(f'EDADES')
st.pyplot(fig_edad)

st.markdown('---')

# Plot de géneros
st.markdown('*GÉNEROS*')
fig_genero, ax_genero = plt.subplots()
sns.histplot(data=df_filtered_clase, x='Sex', color='#225d82', ax=ax_genero)
ax_genero.set_title(f'CANTIDAD DE HOMBRES Y MUJERES')
st.pyplot(fig_genero)

st.markdown('---')

# Plot de SibSp
st.markdown('*SibSp*')
fig_sib = plt.figure()
sns.histplot(data=df_filtered_clase, x='SibSp', color='#0a383d')
plt.title(f'HERMANOS Y CÓNYUGES')

# Establecer los marcadores del eje x como enteros
plt.xticks(list(range(int(df_filtered_clase['SibSp'].min()), int(df_filtered_clase['SibSp'].max()) + 1)))
st.pyplot(fig_sib)


st.markdown('---')

# Plot de Parch
st.markdown('*Parch*')
fig_parch = plt.figure()
sns.histplot(data=df_filtered_clase, x='Parch', color='#453a43', discrete=True)
plt.title(f'PADRES E HIJOS')
st.pyplot(fig_parch)

st.markdown('---')

# Plot de Fare
st.markdown('*FARE*')
fig_fare, ax_fare = plt.subplots()
if seleccionar_clase==1:
    bins = [0, 100, 200, 300, 400, 500,600] 
elif seleccionar_clase==2:
    bins = [0, 20,40,60,80,100]
elif seleccionar_clase==3:
    bins = [0, 20,40,60,80]

sns.histplot(data=df_filtered_clase, x='Fare', color='#3d0333', bins=bins,ax=ax_fare)
ax_fare.set_title(f'PRECIO DEL TICKET')
st.pyplot(fig_fare)

st.markdown('---')

# Plot de Embarked
st.markdown('*EMBARQUE*')
fig_em, ax_em = plt.subplots()
sns.histplot(data=df_filtered_clase, x='Embarked', color='#516350', ax=ax_em)
ax_em.set_title(f'PUNTO DE INICIO')
st.pyplot(fig_em)
