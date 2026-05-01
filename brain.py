import google.generativeai as genai
import streamlit as st

def analyze_prescription(image):
    # This pulls the API Key from your Streamlit Secrets later
    if "GEMINI_API_KEY" not in st.secrets:
        return "Error: Gemini API Key not found in Secrets. Please add it to your deployment settings."
    
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # We use Flash because it's fast and free
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Clinical Pharmacist Persona
    prompt = """
    You are Lumi, a senior clinical pharmacist. Your task is to analyze the provided prescription image.
    
    1. EXTRACT: List every medicine, its strength (e.g., 500mg), and dosage instructions.
    2. SAFETY CHECK: Identify any drug-to-drug interactions or contraindications.
    3. RISK SCORE: Assign a 'Prescription Risk Score' (1-10) where 1 is safe and 10 is dangerous. 
       - If you see Ibuprofen + Aspirin, or multiple antibiotics, increase the risk.
    4. EDUCATION: Explain in simple English AND Roman Urdu what each medicine is for.
    5. WARNINGS: Add specific warnings for pregnancy, kidney (renal), or liver (hepatic) issues if applicable.
    
    Format the output beautifully using Markdown headers and bullet points.
    """
    
    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Lumi Brain Error: {str(e)}"
