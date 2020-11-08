import streamlit as st
import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import re
sns.set()
from fun import next_letter, next_vowel, clean_data_letter, clean_data_vowel, empty_panel, empty_consonant, empty_vowel, clean_empty_consonant, clean_empty_vowel
from PIL import Image
import json

st.title("Predict next letter")
image = Image.open('../Data_files/wheel_of_fortune.jpg')
st.image(image, caption='Wheel of Fortune',use_column_width=True)


st.subheader("Select the letter/s you have and predict the next one")

filenames= os.listdir('../Files')


data_select = st.selectbox('Select your language',filenames )

st.info(f'You selected {data_select}')

lan= re.sub(r'.csv', '', data_select)

#Read Data
df= pd.read_csv(f'../Files/{data_select}', index_col=0)
df_AllLetters= pd.read_csv(f'../Data_files/{lan}_allwords.csv', index_col=0)
with open(f'../Files/{lan}_dictionary.json', 'r') as f:
    dic = json.load(f)
#Show Dataset      #PONER PORCENTAJE DE VECES QUE APARECE CADA COLUMNA Y ELEGIR QUE DATASET SE QIERE VER

if st.checkbox("Show Dataset"):
  st.dataframe(df)

#Select lettes alredy in the word

all_letters= df.columns.tolist()

question1 = st.radio("What do you have?", ('Word with some letters','Empty panel', 'Empty word but with some letters'))

if question1 == 'Word with some letters':
  letters= st.multiselect("Select letters you have", all_letters)
  question2 = st.radio("What do you need?", ('Consonant', 'Vowel'))
  if question2 == "Consonant":
    st.subheader(next_letter(df, letters))
    st.dataframe(clean_data_letter(df, letters))

  if question2 == "Vowel":
    st.subheader(next_vowel(df, letters))
    st.dataframe(clean_data_vowel(df, letters))

if question1 == 'Empty panel':
  st.subheader(empty_panel(df_AllLetters))
  st.dataframe(df_AllLetters)


if question1 == 'Empty word but with some letters':
  letters= st.multiselect("Select letters you have", all_letters)
  question2 = st.radio("What do you need?", ('Consonant', 'Vowel'))
  if question2 == "Consonant":
    st.subheader(empty_consonant(dic, letters))
    st.dataframe(clean_empty_consonant(dic, letters))

  if question2 == "Vowel":
    st.subheader(empty_vowel(dic, letters))
    st.dataframe(clean_empty_vowel(dic, letters))








