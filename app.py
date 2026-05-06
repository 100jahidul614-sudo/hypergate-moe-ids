import streamlit as st
import random
import pandas as pd
import time

st.set_page_config(layout="wide")

st.title("🔐 HyperGate-MoE-IDS Dashboard")

# Simulated data
attack_types = ["Normal", "DDoS", "Spoofing", "Malware"]
risk_levels = ["Low", "Medium", "High"]

# Generate fake prediction
prediction = random.choice(attack_types)
confidence = round(random.uniform(0.7, 0.99), 2)
risk = random.choice(risk_levels)

# Top metrics
col1, col2, col3 = st.columns(3)

col1.metric("Traffic Status", prediction)
col2.metric("Confidence", confidence)
col3.metric("Risk Level", risk)

st.markdown("---")

# Detection Result
st.subheader("📊 Detection Result")
st.write(f"Predicted: **{prediction}**")

# Alerts Panel
st.subheader("🚨 Alerts Panel")

alerts = pd.DataFrame({
    "Time": ["10:01", "10:05", "10:10"],
    "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03"],
    "Threat": ["DDoS", "Spoofing", "Malware"]
})

st.dataframe(alerts)

# Explainability (Fake SHAP-like)
st.subheader("🧠 Explainability (Feature Importance)")

features = ["Packet Rate", "Flow Duration", "Protocol", "Entropy"]
importance = [random.uniform(0.1, 1.0) for _ in features]

chart_data = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

st.bar_chart(chart_data.set_index("Feature"))

# Simulated system flow
st.subheader("🔄 System Flow Simulation")

st.write("IoMT Data → Preprocessing → Context Encoding → Hypernetwork → MoE → Decision")

# Refresh button
if st.button("🔁 Refresh Simulation"):
    st.rerun()
