import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Streamlit sayfa ayarlarını yapılandır
st.set_page_config(
    page_title="HedefAVM Dijital Katalog",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gereksiz Streamlit boşluklarını (margin/padding) sıfırlamak için ufak bir stil
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Dosya yolları (Aynı klasörde oldukları varsayılmaktadır)
pdf_file_path = "dugunpaketi2026.pdf"
html_file_path = "index.html"

# 3. PDF ve HTML dosyalarını oku
if not os.path.exists(pdf_file_path):
    st.error(f"⚠️ Hata: '{pdf_file_path}' dosyası bulunamadı. Lütfen PDF dosyasını uygulamanın yanına koyun.")
    st.stop()

if not os.path.exists(html_file_path):
    st.error(f"⚠️ Hata: '{html_file_path}' dosyası bulunamadı. Lütfen index.html dosyasını uygulamanın yanına koyun.")
    st.stop()

# PDF'i Base64 formatına çevir (Streamlit iframe'i dış dosyaları güvenlikten dolayı engelleyebileceği için veriyi direkt HTML'e gömüyoruz)
with open(pdf_file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_data_uri = f"data:application/pdf;base64,{base64_pdf}"

# HTML'i metin olarak oku
with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# 4. HTML içindeki varsayılan dosya adını, kodlanmış Base64 verimiz ile değiştir
html_code = html_code.replace(
    "let DEFAULT_PDF_URL = 'dugunpaketi2026.pdf';", 
    f"let DEFAULT_PDF_URL = '{pdf_data_uri}';"
)

# 5. HTML (Katalog) bileşenini Streamlit ekranına tam boyutla bas
# height parametresi ekranın yüksekliğini belirler, duruma göre arttırılabilir.
components.html(html_code, height=850, scrolling=False)
