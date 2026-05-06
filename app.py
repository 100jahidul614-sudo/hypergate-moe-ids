import streamlit as st
import pandas as pd
import random

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="HyperGate-MoE-IDS Dashboard",
    page_icon="🔐",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS Styling
# -------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.card {
    background-color: #161B22;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #30363D;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.35);
}

.metric-title {
    font-size: 15px;
    color: #AAB2C0;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 38px;
    font-weight: 700;
    color: white;
}

.small-text {
    color: #AAB2C0;
    font-size: 15px;
}

.section-title {
    font-size: 30px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.green {
    color: #2ECC71;
}

.orange {
    color: #F39C12;
}

.red {
    color: #FF4B4B;
}

.status-box {
    background-color: #132A13;
    padding: 12px 18px;
    border-radius: 12px;
    border: 1px solid #2ECC71;
    font-size: 18px;
    font-weight: 600;
    color: #2ECC71;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Simulated IDS Logic
# -------------------------------------------------
 attack_types = ["Normal", "DDoS", "Spoofing", "Malware", "Ransomware"]
 
 
 prediction = random.choice(attack_types)
 prediction = random.choice(attack_types)

 confidence = round(random.uniform(0.78, 0.98), 2)
 confidence = round(random.uniform(0.78, 0.98), 2)

 uncertainty = round(1 - confidence, 2)
 uncertainty = round(1 - confidence, 2)
 
 
 if prediction == "Normal":
 if prediction == "Normal":
 @@ -181,7 +179,6 @@
 left, right = st.columns(2)
 left, right = st.columns(2)
 
 
 with left:
 with left:

     st.markdown("""
     st.markdown("""
     <div class='section-title'>
     <div class='section-title'>
     📊 Detection Result
     📊 Detection Result
 @@ -190,23 +187,19 @@
 
 
     if risk == "Low":
     if risk == "Low":
         st.success(detection_message)
         st.success(detection_message)

     elif risk == "Medium":
     elif risk == "Medium":
         st.warning(detection_message)
         st.warning(detection_message)

     else:
     else:
         st.error(detection_message)
         st.error(detection_message)
 
 
 with right:
 with right:

     st.markdown("""
     st.markdown("""
     <div class='section-title'>
     <div class='section-title'>
     🧠 Adaptive Model Behaviour
     🧠 Adaptive Model Behaviour
     </div>
     </div>
     """, unsafe_allow_html=True)
     """, unsafe_allow_html=True)
 
 
     st.info(f"Hypernetwork Mode: **{hyper_mode}**")
     st.info(f"Hypernetwork Mode: **{hyper_mode}**")

     st.success(f"Selected MoE Expert: **{selected_expert}**")
     st.success(f"Selected MoE Expert: **{selected_expert}**")
 
 
 # -------------------------------------------------
 # -------------------------------------------------
 @@ -216,9 +209,7 @@
 
 
 col_alerts, col_xai = st.columns([1.15, 1])
 col_alerts, col_xai = st.columns([1.15, 1])
 
 
# ---------------- Alerts ----------------
 with col_alerts:
 with col_alerts:

     st.markdown("""
     st.markdown("""
     <div class='section-title'>
     <div class='section-title'>
     🚨 Alerts Panel
     🚨 Alerts Panel
 @@ -239,9 +230,7 @@
         hide_index=True
         hide_index=True
     )
     )
 
 
# ---------------- Explainability ----------------
 with col_xai:
 with col_xai:

     st.markdown("""
     st.markdown("""
     <div class='section-title'>
     <div class='section-title'>
     🧠 Explainability
     🧠 Explainability
 @@ -264,18 +253,14 @@
     explain_df = pd.DataFrame({
     explain_df = pd.DataFrame({
         "Feature": features,
         "Feature": features,
         "Importance": importance
         "Importance": importance
    })
    }).sort_values(

    explain_df = explain_df.sort_values(
         by="Importance",
         by="Importance",
         ascending=False
         ascending=False
     )
     )
 
 
     top_feature = explain_df.iloc[0]["Feature"]
     top_feature = explain_df.iloc[0]["Feature"]
 
 
    st.markdown(
    st.markdown(f"Top influencing feature: **{top_feature}**")
        f"Top influencing feature: **{top_feature}**"
    )
 
 
     st.bar_chart(
     st.bar_chart(
         explain_df.set_index("Feature"),
         explain_df.set_index("Feature"),
 @@ -287,14 +272,12 @@
 # -------------------------------------------------
 # -------------------------------------------------
 st.markdown("---")
 st.markdown("---")
 
 
st.markdown("""
st.markdown(
<div class='section-title'>
    "<div class='section-title'>🔄 System Flow Simulation</div>",
🔄 System Flow Simulation
    unsafe_allow_html=True
</div>
)
""", unsafe_allow_html=True)
 
 
st.markdown("""
flow_text = """
```text
 IoMT Data
 IoMT Data
    ↓
    ↓
 Preprocessing & Feature Extraction
 Preprocessing & Feature Extraction
 @@ -312,3 +295,31 @@
 Alert Generation
 Alert Generation
    ↓
    ↓
 Explainability (SHAP / LIME)
 Explainability (SHAP / LIME)
"""

st.code(flow_text, language="text")

# -------------------------------------------------
# Prototype Note
# -------------------------------------------------
st.markdown("---")

st.warning(
    "Prototype note: This dashboard simulates the proposed HyperGate-MoE-IDS behaviour. "
    "It demonstrates the workflow, alerting logic, adaptive expert selection, and explainability output "
    "without implementing the full trained model."
)

# -------------------------------------------------
# Refresh Button
# -------------------------------------------------
if st.button("🔁 Refresh Simulation"):
    st.rerun()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption(
    "HyperGate-MoE-IDS Conceptual Prototype | "
    "Capstone Research Project | IoMT Cybersecurity"
)
