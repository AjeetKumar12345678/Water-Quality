import os
import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(
    page_title="AI Water Quality Assessment System",
    page_icon="💧",
    layout="wide"
)

st.title("💧 AI-Powered Water Quality Assessment System")
st.markdown("Assess water safety using **Fuzzy Logic** for deterministic scoring and **LangChain (LLM)** for intelligent expert recommendations.")

# --- SIDEBAR: CONFIGURATION ---
st.sidebar.header("Configuration")

# Automatically check Streamlit Secrets first, otherwise provide the text input fallback
default_key = st.secrets.get("OPENAI_API_KEY", "") if "OPENAI_API_KEY" in st.secrets else ""
api_key = st.sidebar.text_input("OpenAI API Key", value=default_key, type="password")

st.sidebar.markdown("---")
st.sidebar.info(
    "**Parameters Info:**\n"
    "- **pH:** Ideal range is 6.5 - 8.5\n"
    "- **Turbidity:** Measured in NTU (Ideal < 5)\n"
    "- **TDS:** Total Dissolved Solids in mg/L (Ideal < 500)"
)

# --- FUZZY LOGIC ENGINE ---
def compute_fuzzy_wqi(pH_val, turb_val, tds_val):
    """
    Computes a Water Quality Index score (0-100) using Fuzzy Logic.
    """
    # Antecedents (Inputs)
    pH = ctrl.Antecedent(np.arange(0, 14.1, 0.1), 'pH')
    turbidity = ctrl.Antecedent(np.arange(0, 100.1, 0.1), 'turbidity')
    tds = ctrl.Antecedent(np.arange(0, 1000.1, 1), 'tds')

    # Consequent (Output)
    wqi = ctrl.Consequent(np.arange(0, 101, 1), 'wqi')

    # Membership functions for pH
    pH['acidic'] = fuzz.trapmf(pH.universe, [0, 0, 5.5, 6.5])
    pH['optimal'] = fuzz.trimf(pH.universe, [6.0, 7.25, 8.5])
    pH['alkaline'] = fuzz.trapmf(pH.universe, [8.0, 9.0, 14, 14])

    # Membership functions for Turbidity
    turbidity['low'] = fuzz.trapmf(turbidity.universe, [0, 0, 3, 6])
    turbidity['moderate'] = fuzz.trimf(turbidity.universe, [4, 15, 30])
    turbidity['high'] = fuzz.trapmf(turbidity.universe, [20, 40, 100, 100])

    # Membership functions for TDS
    tds['low'] = fuzz.trapmf(tds.universe, [0, 0, 300, 500])
    tds['moderate'] = fuzz.trimf(tds.universe, [400, 600, 800])
    tds['high'] = fuzz.trapmf(tds.universe, [700, 900, 1000, 1000])

    # Membership functions for WQI Output
    wqi['poor'] = fuzz.trapmf(wqi.universe, [0, 0, 30, 50])
    wqi['fair'] = fuzz.trimf(wqi.universe, [40, 60, 80])
    wqi['good'] = fuzz.trapmf(wqi.universe, [70, 90, 100, 100])

    # Fuzzy Rules
    rule1 = ctrl.Rule(pH['optimal'] & turbidity['low'] & tds['low'], wqi['good'])
    rule2 = ctrl.Rule(pH['acidic'] | pH['alkaline'], wqi['poor'])
    rule3 = ctrl.Rule(turbidity['high'] | tds['high'], wqi['poor'])
    rule4 = ctrl.Rule(turbidity['moderate'] | tds['moderate'], wqi['fair'])
    rule5 = ctrl.Rule(pH['optimal'] & turbidity['low'] & tds['moderate'], wqi['fair'])

    # Control System
    wqi_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    wqi_sim = ctrl.ControlSystemSimulation(wqi_ctrl)

    # Pass inputs
    wqi_sim.input['pH'] = pH_val
    wqi_sim.input['turbidity'] = turb_val
    wqi_sim.input['tds'] = tds_val

    try:
        wqi_sim.compute()
        score = wqi_sim.output['wqi']
    except Exception:
        # Fallback if crisp inputs fall outside standard rule triggers
        score = 50.0 

    return score

# --- MAIN INTERFACE: INPUTS ---
col1, col2, col3 = st.columns(3)

with col1:
    pH_input = st.slider("pH Level", 0.0, 14.0, 7.2, 0.1)
with col2:
    turb_input = st.slider("Turbidity (NTU)", 0.0, 50.0, 2.5, 0.1)
with col3:
    tds_input = st.slider("Total Dissolved Solids (TDS mg/L)", 0.0, 1000.0, 150.0, 1.0)

if st.button("Run Water Assessment", type="primary"):
    if not api_key:
        st.error("Please enter your OpenAI API Key in the sidebar or configure it in Streamlit Secrets.")
    else:
        with st.spinner("Calculating fuzzy logic index and generating LLM report..."):
            # 1. Calculate Fuzzy Score
            fuzzy_score = compute_fuzzy_wqi(pH_input, turb_input, tds_input)
            
            if fuzzy_score >= 70:
                category = "Good / Safe"
                color = "green"
            elif fuzzy_score >= 40:
                category = "Fair / Moderate"
                color = "orange"
            else:
                category = "Poor / Unsafe"
                color = "red"

            # Display Metrics
            st.markdown("---")
            m1, m2 = st.columns(2)
            m1.metric(label="Fuzzy Logic WQI Score (0-100)", value=f"{fuzzy_score:.2f}")
            m2.markdown(f"### Status: :{color}[{category}]")

            # 2. LangChain Integration for Expert Insight
            llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.3)
            
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "You are an expert environmental scientist and water sanitation specialist."),
                ("user", """
                Analyze the following water sample parameters and fuzzy logic evaluation:
                - pH: {pH}
                - Turbidity: {turbidity} NTU
                - Total Dissolved Solids (TDS): {tds} mg/L
                - Fuzzy Logic Water Quality Score: {score} / 100
                - Preliminary Assessment Category: {category}

                Provide a comprehensive report including:
                1. Potential health and environmental impacts of these exact metrics.
                2. Whether this water is safe for consumption or irrigation.
                3. Actionable steps or treatment recommendations (e.g., filtration, boiling, chemical treatment) if necessary.
                """)
            ])

            chain = prompt_template | llm | StrOutputParser()
            
            report = chain.invoke({
                "pH": pH_input,
                "turbidity": turb_input,
                "tds": tds_input,
                "score": f"{fuzzy_score:.2f}",
                "category": category
            })

            # Display LLM Report
            st.markdown("### 📋 AI Expert Water Analysis Report")
            st.write(report)
