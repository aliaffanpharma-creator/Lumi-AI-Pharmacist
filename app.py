import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Lumi - AI Digital Pharmacist", layout="wide")

# --- CUSTOM CSS FOR THE "LUMI" LOOK ---
st.markdown("""
    <style>
    .main { background-color: #F8F9FE; }
    [data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 1px solid #E6E8F1; }
    .stButton>button { background-color: #7B61FF; color: white; border-radius: 10px; }
    .risk-card {
        background-color: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E6E8F1; text-align: center;
    }
    .metric-value { font-size: 48px; font-weight: bold; color: #333; }
    .medicine-table { background-color: white; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_value=True)

# --- SIDEBAR (Matching Design Tempelate.jpg) ---
with st.sidebar:
    st.title("✨ Lumi")
    st.caption("AI Digital Pharmacist")
    st.markdown("---")
    st.button("🏠 Home")
    st.button("🔍 Scan Prescription")
    st.button("💊 My Medicines")
    st.button("⚠️ Drug Interactions")
    st.button("🔔 Reminders")
    st.button("👤 Patient Profile")
    st.markdown("---")
    st.info("Hi! I'm Lumi. How can I help you today?")

# --- MAIN DASHBOARD ---
st.title("Hello, Ali 👋")
st.write("We're here to help you stay healthy.")

# TOP ROW: SCANNING OPTIONS
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Scan Prescription")
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
    
with col2:
    st.subheader("Prescription Risk Score")
    st.markdown("""
        <div class="risk-card">
            <p>Moderate Risk</p>
            <div class="metric-value">7.5 <span style="font-size:20px">/10</span></div>
        </div>
    """, unsafe_allow_value=True)

with col3:
    st.subheader("Today's Schedule")
    st.write("✅ Metformin 500mg - 8:00 AM")
    st.write("🕒 Amoxicillin 500mg - 1:00 PM")

st.markdown("---")

# MIDDLE ROW: AI SUMMARY & MEDICINES
col_mid1, col_mid2 = st.columns([2, 1])

with col_mid1:
    st.subheader("💊 Your Medicines")
    # Mock data to match the UI pic
    data = {
        "Medicine": ["Metformin 500mg", "Amoxicillin 500mg", "Ibuprofen 400mg"],
        "Purpose": ["Control blood sugar", "Bacterial infection", "Pain and fever"],
        "When to Take": ["After breakfast", "After food, 3x daily", "If needed"],
        "Safety": ["✅ Safe", "✅ Caution", "❌ High Risk"]
    }
    st.table(data)

with col_mid2:
    st.subheader("🤖 Talk to Lumi")
    user_input = st.text_input("Ask in Urdu, Sindhi, or English...")
    if st.button("Send"):
        st.write("Lumi is thinking...")

# --- LOGIC FOR GEMINI ---
if uploaded_file is not None:
    # This is where the RAG/OCR happens
    image = Image.open(uploaded_file)
    st.image(image, caption='Prescription Uploaded', use_column_width=True)
    st.success("Analysis starting... (Using Gemini 1.5 Flash)")
