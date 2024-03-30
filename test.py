import streamlit as st

st.header('aplikasi penjumlahan numerik', divider='rainbow')

Angka_pertama = st.number_input('masukan angka pertama')
st.write('the first number is',Angka_pertama)

Angka_kedua = st.number_input('masukan angka kedua')
st.write('the second number is',Angka_kedua)

operasi_matematika = Angka_pertama * Angka_kedua
st.write(f"Angka pertama {Angka_pertama} x Angka kedua {Angka_kedua} = {operasi_matematika}")