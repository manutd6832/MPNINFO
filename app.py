import streamlit as st
import pandas as pd
import pymysql

# Konfigurasi koneksi ke database
db_config = {
    'host': '10.4.254.253',       # Ganti dengan host database Anda
    'user': 'mpninfo',          # Ganti dengan username MySQL Anda
    'password': 'Pancasila5%',       # Ganti dengan password MySQL Anda
    'database': 'mpninfo'       # Ganti dengan nama database Anda
}

# Membuat koneksi ke database
def get_data_from_db():
    try:
        # Membuat koneksi ke database
        connection = pymysql.connect(**db_config)
        query = "SELECT * FROM spmkp;"  # Query untuk tabel spmkp
        
        # Membaca hasil query ke DataFrame
        df = pd.read_sql(query, con=connection)
        return df
    except pymysql.MySQLError as err:
        # Menangani error MySQL
        st.error(f"Database error: {err}")
        return None
    finally:
        # Menutup koneksi jika terbuka
        if connection:
            connection.close()

# Judul aplikasi
st.title("Tampilan Data Tabel SPMKP")

# Menampilkan data
data = get_data_from_db()
if data is not None:
    st.write("Data dari tabel SPMKP:")
    st.dataframe(data)  # Menampilkan DataFrame dalam bentuk tabel interaktif
else:
    st.error("Tidak dapat memuat data.")

