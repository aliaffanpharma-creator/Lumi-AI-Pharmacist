import streamlit as st
from PIL import Image
import os
from brain import analyze_prescription

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Lumi - AI Digital Pharmacist", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- UI STYLING (MATCHING DESIGN TEMPELATE.JPG) ---
st.markdown("""
    <style>
    /* Main Background */
    .main { background-color: #F8F9FE; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF; 
        border-right: 1px solid #E6E8F1; 
    }
    
    /* Buttons */
    .stButton>button { 
        background-color: #7B61FF; 
        color: white; 
        border-radius: 12px; 
        border: none;
        padding: 10px 24px;
        width: 100%;
    }
    
    /* Risk Card Styling */
    .risk-card {
        background-color: white; 
        padding: 25px; 
        border-radius: 20px;
        border: 1px solid #E6E8F1; 
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    }
    .metric-value { 
        font-size: 54px; 
        font-weight: bold; 
        color: #333; 
        margin: 10px 0;
    }
    
    /* Status Tags */
    .status-safe { color: #28C76F; font-weight: bold; }
    .status-caution { color: #FF9F43; font-weight: bold; }
    .status-risk { color: #EA5455; font-weight: bold; }
    </style>
    """, unsafe_allow_value=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4320/4320350.png", width=50) # Placeholder logo
    st.title("Lumi")
    st.caption("AI Digital Pharmacist")
    st.markdown("---")
    
    # Navigation Buttons (Visual only for Demo)
    st.button("🏠 Home")
    st.button("🔍 Scan Prescription")
    st.button("💊 My Medicines")
    st.button("⚠️ Drug Interactions")
    st.button("🔔 Reminders")
    st.button("👤 Patient Profile")
    st.button("🤖 AI Chat Assistant")
    
    st.markdown("---")
    # Chatbot Avatar area
    st.info("**Hi! I'm Lumi ✨**\nYour AI Pharmacist. How can I help you today?")
    st.text_input("Talk to Lumi...", placeholder="Ask about dosage...")

# --- MAIN DASHBOARD AREA ---
st.title("Hello, Ali 👋")
st.write("We're here to help you stay healthy.")

# TOP ROW: Action Cards
col_upload, col_risk, col_schedule = st.columns([1.5, 1, 1])

with col_upload:
    st.subheader("Scan Prescription")
    uploaded_file = st.file_uploader("Upload or Capture Prescription Image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file:
        st.image(uploaded_file, caption="Prescription Preview", use_container_width=True)

with col_risk:
    st.subheader("Prescription Risk Score")
    # This score updates dynamically if logic is added; for now, it mirrors the design
    st.markdown("""
        <div class="risk-card">
            <p style="color: #FF9F43; font-weight: bold;">Moderate Risk</p>
            <div class="metric-value">7.5 <span style="font-size:22px; color: #666;">/10</span></div>
            <p style="font-size: 14px; color: #888;">Based on current medications</p>
        </div>
    """, unsafe_allow_value=True)

with col_schedule:
    st.subheader("Today's Schedule")
    st.markdown("""
    - 🕒 **8:00 AM**: Metformin 500mg <span class="status-safe">Taken</span>
    - 🕒 **1:00 PM**: Amoxicillin 500mg <span class="status-caution">Due</span>
    - 🕒 **8:00 PM**: Aspirin 75mg <span class="status-caution">Due</span>
    """, unsafe_allow_value=True)

st.markdown("---")

# BOTTOM SECTION: Analysis Result
if uploaded_file is not None:
    st.subheader("🤖 Lumi AI Clinical Analysis")
    with st.spinner('Lumi is analyzing your prescription for safety...'):
        try:
            # Convert uploaded file to PIL Image for the AI
            image_pil = Image.open(uploaded_file)
            # Call the brain.py function
            report = analyze_prescription(image_pil)
            
            # Display result in a nice box
            st.success("Analysis Complete!")
            st.markdown(report)
            
        except Exception as e:
            st.error(f"Could not analyze image: {e}")

else:
    # Default view if no file is uploaded (Table view from Design)
    col_meds, col_nearby = st.columns([2, 1])
    
    with col_meds:
        st.subheader("💊 Your Medicines")
        med_data = [
            {"Medicine": "Metformin 500mg", "Purpose": "Control blood sugar", "When": "After breakfast", "Safety": "✅ Safe"},
            {"Medicine": "Amoxicillin 500mg", "Purpose": "Bacterial infection", "When": "After food, 3x daily", "Safety": "⚠️ Caution"},
            {"Medicine": "Ibuprofen 400mg", "Purpose": "Pain and fever", "When": "If needed", "Safety": "❌ High Risk"}
        ]
        st.table(med_data)
        
    with col_nearby:
        st.subheader("📍 Nearby Pharmacies")
        st.write("🏥 **HealthPlus Pharmacy** (0.5 km)")
        st.write("🏥 **LifeCare Pharmacy** (0.8 km)")
        st.button("Order Medicine 🛒")

# FOOTER ACTIONS
st.markdown("---")
fcol1, fcol2, fcol3, fcol4 = st.columns(4)
fcol1.button("📞 Consult Doctor")
fcol2.button("⏰ Set Reminder")
fcol3.button("📤 Share Report")
fcol4.button("🌍 Change Language")
