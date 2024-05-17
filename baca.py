import pandas as pd

# Membaca dataset
df = pd.read_csv('harga_bahan_pokok_jawa_timur_2023.csv')

# Menampilkan daftar nama kolom dalam DataFrame
print("Nama kolom dalam DataFrame:", df.columns.tolist())

# Menampilkan beberapa baris pertama dari DataFrame untuk memastikan data terbaca dengan benar
print("Beberapa baris pertama dari DataFrame:")
print(df.head())

# Jika nama kolom sudah benar, lanjutkan dengan pengurutan
if 'harga_rata_rata' in df.columns:
    # Mengurutkan data berdasarkan kolom harga_rata_rata dari yang murah ke mahal
    df_sorted = df.sort_values(by='harga_rata_rata')

    # Mengambil kolom harga sebagai list setelah diurutkan
    harga = df_sorted['harga_rata_rata'].tolist()

    # Print the list of prices
    print(harga)
else:
    print("Kolom 'harga_rata_rata' tidak ditemukan dalam DataFrame.")
