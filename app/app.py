import streamlit as st
import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from fun import next_letter, next_vowel

st.title("Predict next letter")
st.subheader("Select the letter/s you have and predict the next one")

filenames= os.listdir('../Files')


data_select = st.selectbox('Select your language',filenames )

st.info(f'You selected {data_select}')

#Read Data
df= pd.read_csv(f'../Files/{data_select}', index_col=0)

#Show Dataset      #PONER PORCENTAJE DE VECES QUE APARECE CADA COLUMNA Y ELEGIR QUE DATASET SE QIERE VER

if st.checkbox("Show Dataset"):
  st.dataframe(df)

#Select lettes alredy in the word

all_letters= df.columns.tolist()

letters= st.multiselect("Select letters you have", all_letters)

question = st.radio("What do you need?", ('Consonant', 'Vowel'))

if question == "Consonant":
  st.subheader(next_letter(df, letters))

if question == "Vowel":
  st.subheader(next_vowel(df, letters))









