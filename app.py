import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="HyperGate-MoE-IDS Dashboard",
    page_icon="🔐",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #161B22;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #30363D;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
.metric-title {
    font-size: 15px;
    color: #AAB2C0;
    margin-bottom: 8px;
}
.metric-value {
    font-size: 36px;
    font-weight: 700;
    color: #FFFFFF;
}
.small-text {
    color: #AAB2C0;
    font-size: 14px;
}
.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 12px;
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
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Simulated IDS Logic
# -----------------------------
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

# -----------------------------
# Header
# -----------------------------
st.markdown("# 🔐 HyperGate-MoE-IDS Dashboard")
st.markdown(
    "<p class='small-text'>Adaptive IoMT intrusion detection prototype using Hypernetwork control, MoE routing, uncertainty estimation, and risk-aware decision-making.</p>",
    unsafe_allow_html=True
)

st.markdown("### 🟢 System Status: Operational")

# -----------------------------
# Top Metric Cards
# -----------------------------
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

st.markdown("---")

# -----------------------------
# Detection + Adaptive Behaviour
# -----------------------------
left, right = st.columns([1, 1])

with left:
    st.markdown("<div class='section-title'>📊 Detection Result</div>", unsafe_allow_html=True)
    if risk == "Low":
        st.success(detection_message)
    elif risk == "Medium":
        st.warning(detection_message)
    else:
        st.error(detection_message)

with right:
    st.markdown("<div class='section-title'>🧠 Adaptive Model Behaviour</div>", unsafe_allow_html=True)
    st.info(f"Hypernetwork Mode: **{hyper_mode}**")
    st.success(f"Selected MoE Expert: **{selected_expert}**")

# -----------------------------
# Alerts + Explainability
# -----------------------------
st.markdown("---")
col_alerts, col_xai = st.columns([1.15, 1])

with col_alerts:
    st.markdown("<div class='section-title'>🚨 Alerts Panel</div>", unsafe_allow_html=True)

    alerts = pd.DataFrame({
        "Time": ["10:01", "10:05", "10:10", "10:14"],
        "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03", "Pump-04"],
        "Threat": ["DDoS", "Spoofing", "Malware", prediction],
        "Risk": ["High", "Medium", "High", risk],
        "Confidence": [0.94, 0.88, 0.91, confidence]
    })

    st.dataframe(alerts, use_container_width=True, hide_index=True)

with col_xai:
    st.markdown("<div class='section-title'>🧠 Explainability</div>", unsafe_allow_html=True)

    features = ["Packet Rate", "Flow Duration", "Protocol Entropy", "Byte Count", "Connection Frequency"]
    importance = [round(random.uniform(0.25, 0.95), 2) for _ in features]

    explain_df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    top_feature = explain_df.iloc[0]["Feature"]
    st.markdown(f"Top influencing feature: **{top_feature}**")
    st.bar_chart(explain_df.set_index("Feature"), height=320)

# -----------------------------
# System Flow
# -----------------------------
st.markdown("---")
st.markdown("<div class='section-title'>🔄 System Flow Simulation</div>", unsafe_allow_html=True)

st.markdown("""
```text
IoMT Data → Preprocessing → Context Encoding → Hypernetwork Adaptation → MoE Expert Routing → Prediction + Uncertainty → Risk-Aware Decision → Alert Generation → Explainability
