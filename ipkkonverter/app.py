# app.py
import streamlit as st
import math # Gunakan math.pi untuk nilai pi yang lebih akurat

# Fungsi perhitungan volume tabung
def hitung_volume_tabung(r, t):
    # Menggunakan nilai pi dari modul math untuk akurasi yang lebih baik
    # Rumus Volume = pi * r^2 * t
    volume = math.pi * r * r * t
    return volume

st.title("🛢️ Kalkulator Volume Tabung (Cylinder)")
st.write("""
Aplikasi ini menghitung volume tabung berdasarkan jari-jari ($r$) dan tinggi ($t$) yang Anda masukkan.
Rumus yang digunakan adalah $V = \pi r^2 t$.
""")


[Image of a cylinder with radius labeled 'r' and height labeled 'h']


# --- Input Nilai menggunakan Widget Streamlit ---

# Input jari-jari (r)
# Gunakan st.number_input dengan min_value >= 0 karena jari-jari tidak mungkin negatif
jari_jari = st.number_input(
    "Masukkan Jari-jari Tabung ($r$):",
    min_value=0.0,
    value=5.0, # Nilai default
    step=0.1
)

# Input tinggi (t)
# Gunakan st.number_input dengan min_value >= 0 karena tinggi tidak mungkin negatif
tinggi = st.number_input(
    "Masukkan Tinggi Tabung ($t$):",
    min_value=0.0,
    value=10.0, # Nilai default
    step=0.1
)

# Tombol untuk memicu perhitungan
if st.button("Hitung Volume"):
    if jari_jari == 0.0 or tinggi == 0.0:
        st.error("Jari-jari dan Tinggi harus lebih besar dari nol untuk mendapatkan volume yang valid.")
    else:
        # Memanggil fungsi dan menyimpan hasil
        hasil_volume = hitung_volume_tabung(jari_jari, tinggi)

        # Menampilkan hasil
        st.success("✅ Hasil Perhitungan Volume:")
        
        # st.metric menampilkan hasil perhitungan dengan jelas
        st.metric(
            label="Volume Tabung",
            value=f"{hasil_volume:.2f}",
            delta="satuan kubik"
        )
        
        # Menampilkan detail perhitungan
        st.markdown(f"""
        Detail Perhitungan:
        * $r$ = **{jari_jari}**
        * $t$ = **{tinggi}**
        * $\pi$ $\approx$ **{math.pi:.5f}**
        * $V = \pi \times {jari_jari}^2 \times {tinggi} \approx$ **{hasil_volume:.2f}**
        """)