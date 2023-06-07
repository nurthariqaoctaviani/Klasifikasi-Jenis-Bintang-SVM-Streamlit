import pickle
import streamlit as st

# membaca model
starsclass_model =  pickle.load(open('star_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Klasifikasi Tipe Bintang')

Temperature = st.text_input('Masukan Nilai Suhu')

L = st.text_input('Masukan Luminositas Relatif')

R = st.text_input('Masukan Radius Relatif')

A_M = st.text_input('masukan Absolute Magnitude')

Color = st.text_input('masukan Warna Umum Spektrum')

Spectral_Class = st.text_input ('masukan Jenis spektral asteroid')


# code untuk kelompok jenis bintang
star_clasifikasi = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    star_prediction = starsclass_model.predict([[Temperature ,L, R, A_M, Color, Spectral_Class]])
    
    if (star_prediction[0] == 0):
            star_clasifikasi = 'Bintang Tipe Red Dwarf'
    elif(star_prediction[0]==1):
            star_clasifikasi ='Bintang Tipe Brown Dwarf'
    elif(star_prediction[0]==2):
            star_clasifikasi ='Bintang Tipe White Dwarf'
    elif(star_prediction[0]==3):
            star_clasifikasi ='Bintang Tipe Main Sequence'
    elif(star_prediction[0]==4):
            star_clasifikasi ='Bintang Tipe Super Giants'
    else :
         star_clasifikasi ='Bintang Tipe Hyper Giants'

st.success(star_clasifikasi)
