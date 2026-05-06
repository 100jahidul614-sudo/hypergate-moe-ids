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

confidence = round(random.uniform(0.78, 0.98), 2)

uncertainty = round(1 - confidence, 2)

if prediction == "Normal":
    risk = "Low"
    risk_color = "green"
    selected_expert = "ML Expert (RF / LightGBM)"
    hyper_mode = "Low-computation mode"
    detection_message = "Current traffic is classified as normal."

elif prediction in ["DDoS", "Spoofing"]:
    risk = "Medium"
    risk_color = "orange"
    selected_expert = "CNN Expert"
    hyper_mode = "Traffic-pattern sensitivity mode"
    detection_message = f"Potential cyber threat detected: {prediction}"

else:
    risk = "High"
    risk_color = "red"
    selected_expert = "FT-Transformer Expert"
    hyper_mode = "High-sensitivity deep analysis mode"
    detection_message = f"Critical cyber threat detected: {prediction}"

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown("# 🔐 HyperGate-MoE-IDS Dashboard")

st.markdown("""
<p class='small-text'>
Adaptive IoMT intrusion detection prototype using Hypernetwork control,
Mixture-of-Experts routing, uncertainty estimation, and risk-aware
decision-making.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="status-box">
🟢 System Status: Operational
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# Top Metrics
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Traffic Status</div>
        <div class="metric-value">{prediction}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Confidence Score</div>
        <div class="metric-value">{confidence}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Uncertainty Score</div>
        <div class="metric-value">{uncertainty}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Risk Level</div>
        <div class="metric-value {risk_color}">{risk}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Detection Result + Adaptive Behaviour
# -------------------------------------------------
st.markdown("---")

left, right = st.columns(2)

with left:

    st.markdown("""
    <div class='section-title'>
    📊 Detection Result
    </div>
    """, unsafe_allow_html=True)

    if risk == "Low":
        st.success(detection_message)

    elif risk == "Medium":
        st.warning(detection_message)

    else:
        st.error(detection_message)

with right:

    st.markdown("""
    <div class='section-title'>
    🧠 Adaptive Model Behaviour
    </div>
    """, unsafe_allow_html=True)

    st.info(f"Hypernetwork Mode: **{hyper_mode}**")

    st.success(f"Selected MoE Expert: **{selected_expert}**")

# -------------------------------------------------
# Alerts Panel + Explainability
# -------------------------------------------------
st.markdown("---")

col_alerts, col_xai = st.columns([1.15, 1])

# ---------------- Alerts ----------------
with col_alerts:

    st.markdown("""
    <div class='section-title'>
    🚨 Alerts Panel
    </div>
    """, unsafe_allow_html=True)

    alerts = pd.DataFrame({
        "Time": ["10:01", "10:05", "10:10", "10:14"],
        "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03", "Pump-04"],
        "Threat": ["DDoS", "Spoofing", "Malware", prediction],
        "Risk": ["High", "Medium", "High", risk],
        "Confidence": [0.94, 0.88, 0.91, confidence]
    })

    st.dataframe(
        alerts,
        use_container_width=True,
        hide_index=True
    )

# ---------------- Explainability ----------------
with col_xai:

    st.markdown("""
    <div class='section-title'>
    🧠 Explainability
    </div>
    """, unsafe_allow_html=True)

    features = [
        "Packet Rate",
        "Flow Duration",
        "Protocol Entropy",
        "Byte Count",
        "Connection Frequency"
    ]

    importance = [
        round(random.uniform(0.25, 0.95), 2)
        for _ in features
    ]

    explain_df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    })

    explain_df = explain_df.sort_values(
        by="Importance",
        ascending=False
    )

    top_feature = explain_df.iloc[0]["Feature"]

    st.markdown(
        f"Top influencing feature: **{top_feature}**"
    )

    st.bar_chart(
        explain_df.set_index("Feature"),
        height=350
    )

# -------------------------------------------------
# System Flow Simulation
# -------------------------------------------------
st.markdown("---")

st.markdown("""
<div class='section-title'>
🔄 System Flow Simulation
</div>
""", unsafe_allow_html=True)

st.markdown("""
```text
IoMT Data
   ↓
Preprocessing & Feature Extraction
   ↓
Context Encoding
   ↓
Hypernetwork Adaptation
   ↓
Mixture-of-Experts Routing
   ↓
Prediction + Uncertainty Estimation
   ↓
Risk-Aware Decision
   ↓
Alert Generation
   ↓
Explainability (SHAP / LIME)
