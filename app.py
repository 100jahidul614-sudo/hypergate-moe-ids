import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="HyperGate-MoE-IDS Dashboard",
    page_icon="🔐",
    layout="wide"
)

# -----------------------------
# Simulated IDS Logic
# -----------------------------
attack_types = ["Normal", "DDoS", "Spoofing", "Malware", "Ransomware"]
risk_levels = ["Low", "Medium", "High"]
experts = ["ML Expert (RF / LightGBM)", "CNN Expert", "FT-Transformer Expert"]

prediction = random.choice(attack_types)
confidence = round(random.uniform(0.72, 0.98), 2)

if prediction == "Normal":
    risk = "Low"
    selected_expert = "ML Expert (RF / LightGBM)"
    hyper_mode = "Low-computation mode"
elif prediction in ["DDoS", "Spoofing"]:
    risk = random.choice(["Medium", "High"])
    selected_expert = "CNN Expert"
    hyper_mode = "Traffic-pattern sensitivity mode"
else:
    risk = "High"
    selected_expert = "FT-Transformer Expert"
    hyper_mode = "High-sensitivity deep analysis mode"

uncertainty = round(1 - confidence, 2)

risk_icon = {
    "Low": "🟢 Low",
    "Medium": "🟠 Medium",
    "High": "🔴 High"
}

# -----------------------------
# Header
# -----------------------------
st.title("🔐 HyperGate-MoE-IDS Dashboard")
st.caption("Conceptual prototype for adaptive IoMT intrusion detection using Hypernetwork, MoE routing, uncertainty estimation, and risk-aware decisions.")

st.markdown("### 🟢 System Status: Operational")

# -----------------------------
# Top Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Traffic Status", prediction)
col2.metric("Confidence Score", confidence)
col3.metric("Uncertainty Score", uncertainty)
col4.metric("Risk Level", risk_icon[risk])

st.markdown("---")

# -----------------------------
# Detection Result
# -----------------------------
st.subheader("📊 Detection Result")

if prediction == "Normal":
    st.success("Current traffic is classified as **Normal**.")
else:
    st.error(f"Potential cyber threat detected: **{prediction}**")

# -----------------------------
# Hypernetwork + MoE
# -----------------------------
st.subheader("🧠 Adaptive Model Behaviour")

col5, col6 = st.columns(2)

with col5:
    st.markdown("#### ⚙️ Hypernetwork Control")
    st.info(f"Adaptive mode activated: **{hyper_mode}**")
    st.write("The Hypernetwork dynamically adjusts model behaviour based on traffic context, device sensitivity, and prediction uncertainty.")

with col6:
    st.markdown("#### 🧩 MoE Expert Selection")
    st.success(f"Selected expert: **{selected_expert}**")
    st.write("The routing mechanism selects the most suitable expert model for the current traffic condition.")

st.markdown("---")

# -----------------------------
# Alerts Panel
# -----------------------------
st.subheader("🚨 Alerts Panel")

alerts = pd.DataFrame({
    "Time": ["10:01", "10:05", "10:10", "10:14"],
    "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03", "Pump-04"],
    "Threat": ["DDoS", "Spoofing", "Malware", prediction],
    "Risk": ["High", "Medium", "High", risk],
    "Confidence": [0.94, 0.88, 0.91, confidence]
})

st.dataframe(alerts, use_container_width=True)

# -----------------------------
# Explainability
# -----------------------------
st.subheader("🧠 Explainability: Feature Importance")

features = ["Packet Rate", "Flow Duration", "Protocol Entropy", "Byte Count", "Connection Frequency"]
importance = [round(random.uniform(0.15, 0.95), 2) for _ in features]

explain_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

top_feature = explain_df.iloc[0]["Feature"]

st.write(f"Top influencing feature: **{top_feature}**")
st.bar_chart(explain_df.set_index("Feature"))

# -----------------------------
# Workflow Simulation
# -----------------------------
st.subheader("🔄 System Flow Simulation")

st.markdown("""
**IoMT Data → Preprocessing → Context Encoding → Hypernetwork Adaptation → MoE Expert Routing → Prediction + Uncertainty → Risk-Aware Decision → Alert Generation → Explainability**
""")

# -----------------------------
# Prototype Note
# -----------------------------
st.markdown("---")
st.warning(
    "Prototype note: This dashboard simulates the behaviour of the proposed HyperGate-MoE-IDS architecture. "
    "It does not yet implement the full trained Hypernetwork or MoE model."
)

# -----------------------------
# Refresh
# -----------------------------
if st.button("🔁 Refresh Simulation"):
    st.rerun()
