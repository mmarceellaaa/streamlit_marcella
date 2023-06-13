import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('SIMPLE MATHEMATICS',
    ['Hitung Luas Bidang Belah Ketupat',
     'Hitung Luas Bidang Jajar Genjang'],
    default_index=0)

if (selected == 'Hitung Luas Bidang Belah Ketupat') :
    st.title('Luas Bidang Belah Ketupat')

    diagonal1 = st.number_input ("Masukkan nilai diagonal 1", 0)
    diagonal2 = st.number_input ("Masukkan nilai diagonal 2", 0)
    Hitung = st.button ('Hitung!')

    if Hitung :
        Luas = 0.5 * diagonal1 * diagonal2
        st.write ("Hasil Luas Bidang Belah Ketupat ", Luas)

if (selected == 'Hitung Luas Bidang Jajar Genjang') :
    st.title('Luas Bidang Jajar Genjang')

    alas = st.number_input ("Masukkan nilai alas", 0)
    tinggi = st.number_input ("Masukkan nilai tinggi", 0)
    Hitung = st.button ('Hitung!')

    if Hitung :
        luas = alas * tinggi
        st.write ("Hitung Luas Bidang Jajar Genjang ", luas)