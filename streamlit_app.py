import streamlit as st
from streamlit_option_menu import option_menu

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="PPM Calculator",
    page_icon="🧪",
    layout="centered"
)

# --- CUSTOM CSS UNTUK TEMA UNGU ---
st.markdown("""
    <style>
    /* Mengubah warna latar belakang utama dan teks */
    .stApp {
        background-color: #f3f0f7;
    }
    h1, h2, h3 {
        color: #4A154B !important; /* Ungu Gelap */
    }
    /* Mengubah gaya tombol */
    .stButton>button {
        background-color: #6A1B9A !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #8E24AA !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    /* Kotak hasil/sukses */
    .stAlert {
        background-color: #E8E0F5 !important;
        border-left: 5px solid #6A1B9A !important;
        color: #4A154B !important;
    }
    </style>
""", unsafe_allow_html=True) 

# --- SIDEBAR MENU (TEMA UNGU) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluent/96/chemistry-glass.png", width=80)
    st.markdown("<h2 style='color: #6A1B9A; margin-top:0;'>PPM Lab</h2>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title="Navigasi Menu",
        options=["Latar Belakang", "Kalkulator PPM", "Tentang Web"],
        icons=["info-circle", "calculator", "code-slash"],
        menu_icon="cast",
        default_index=1, # Default langsung membuka kalkulator
        styles={
            "container": {"padding": "5px!", "background-color": "#fafafa"},
            "icon": {"color": "#8E24AA", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px", "--hover-color": "#E8E0F5"},
            "nav-link-selected": {"background-color": "#6A1B9A", "color": "white"},
        }
    )

# --- KONTEN MENU 1: LATAR BELAKANG ---
if selected == "Latar Belakang":
    st.title("🍇 Kenapa Web Ini Dibuat?")
    st.write("""
    Dalam dunia sains, pertanian hidroponik, akuakultur, hingga industri kimia, akurasi dalam mengukur konsentrasi larutan adalah segalanya. 
    Salah satu satuan yang paling sering digunakan adalah **PPM (Parts Per Million)** atau Bagian Per Sejuta.
    """)
    
    st.markdown("### 💡 Masalah yang Sering Dihadapi:")
    st.write("* **Rumus yang Membingungkan:** Banyak orang sering keliru mengonversi satuan massa (mg, gram, kg) ke volume air (ml, liter).")
    st.write("* **Risiko Kesalahan Manual:** Menghitung manual di atas kertas memperbesar peluang kesalahan fatal (misal: tanaman hidroponik mati karena over-dosis nutrisi).")
    
    st.markdown("### 🎯 Solusi Kami:")
    st.info("Web ini diciptakan sebagai alat bantu yang cepat, praktis, dan instan untuk membantu para praktisi, pelajar, dan hobiis dalam menghitung kebutuhan PPM secara akurat tanpa ribet hitung manual!")

# --- KONTEN MENU 2: KALKULATOR PPM (INTERAKTIF) ---
elif selected == "Kalkulator PPM":
    st.title("🧮 Kalkulator PPM Interaktif")
    st.write("Hitung konsentrasi larutan Anda atau cari tahu berapa massa zat yang Anda butuhkan.")
    
    # Pilih Mode Kalkulator
    mode = st.radio(
        "Pilih apa yang ingin Anda hitung:",
        ("Cari Nilai PPM (Konsentrasi)", "Cari Massa Zat (Gram) yang Dibutuhkan"),
        horizontal=True
    )
    
    st.write("---")
    
    if mode == "Cari Nilai PPM (Konsentrasi)":
        st.subheader("🧪 Hitung Konsentrasi (PPM)")
        
        col1, col2 = st.columns(2)
        with col1:
            massa = st.number_input("Masukkan Massa Zat Terlarut:", min_value=0.0, value=1.0, step=0.1)
            satuan_massa = st.selectbox("Satuan Massa:", ["Miligram (mg)", "Gram (g)"])
        with col2:
            volume = st.number_input("Masukkan Volume Pelarut (Air):", min_value=0.01, value=1.0, step=0.1)
            satuan_volume = st.selectbox("Satuan Volume:", ["Liter (L)", "Mililiter (ml)"])
            
        if st.button("Hitung PPM"):
            # Konversi semua ke mg dan Liter (karena 1 PPM = 1 mg/L)
            massa_mg = massa if satuan_massa == "Miligram (mg)" else massa * 1000
            volume_l = volume if satuan_volume == "Liter (L)" else volume / 1000
            
            hasil_ppm = massa_mg / volume_l
            
            st.balloons()
            st.success(f"🎉 Hasil Konsentrasi: **{hasil_ppm:,.2f} PPM**")
            
            # Tips Interaktif
            if hasil_ppm > 1500:
                st.warning("⚠️ Konsentrasi cukup tinggi! Pastikan ini sesuai dengan peruntukan larutan Anda.")
            elif hasil_ppm < 100:
                st.info("💡 Larutan tergolong encer.")

    else:
        st.subheader("⚖️ Hitung Massa Zat yang Diperlukan")
        
        target_ppm = st.number_input("Masukkan Target PPM yang Diinginkan:", min_value=0.0, value=500.0, step=10.0)
        
        col1, col2 = st.columns(2)
        with col1:
            volume_target = st.number_input("Masukkan Volume Air:", min_value=0.01, value=1.0, step=0.1)
        with col2:
            satuan_vol_target = st.selectbox("Satuan Volume Air:", ["Liter (L)", "Mililiter (ml)"])
            
        if st.button("Hitung Kebutuhan Zat"):
            volume_target_l = volume_target if satuan_vol_target == "Liter (L)" else volume_target / 1000
            
            # Rumus: Massa (mg) = PPM * Volume (L)
            massa_butuh_mg = target_ppm * volume_target_l
            massa_butuh_g = massa_butuh_mg / 1000
            
            st.balloons()
            st.success(f"🎉 Anda membutuhkan **{massa_butuh_g:.4f} gram** (atau {massa_butuh_mg:,.1f} mg) zat terlarut.")

# --- KONTEN MENU 3: TENTANG WEBSITE ---
elif selected == "Tentang Web":
    st.title("💻 Tentang Aplikasi")
    
    st.write("""
    Aplikasi **PPM Calculator** ini dibangun menggunakan teknologi modern berbasis Python untuk memberikan pengalaman komputasi sains yang ramah pengguna (*user-friendly*).
    """)
    
    # Menampilkan spesifikasi teknologi dengan tabel/fitur aesthetic
    st.markdown("### 🛠️ Tech Stack & Spesifikasi:")
    
    info_aplikasi = {
        "Komponen": ["Framework UI", "Bahasa Pemrograman", "Tema Warna", "Fitur Utama"],
        "Detail": ["Streamlit (Python)", "Python 3.x", "Deep Purple & Lavender", "Multi-mode kalkulator, Deteksi otomatis unit, Responsif UI"]
    }
    st.table(info_aplikasi)
    
    st.markdown("### 📌 Rumus Dasar yang Digunakan:")
    st.code("1 PPM = 1 mg / 1 Liter Air", language="text")
    
    st.markdown("---")
    st.caption("Dibuat dengan 💜 menggunakan Streamlit | © 2026")
