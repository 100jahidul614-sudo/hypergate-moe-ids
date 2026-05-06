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
# Custom CSS
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080B12 0%, #0E1117 45%, #111827 100%);
    color: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

.main-title {
    font-size: 46px;
    font-weight: 800;
    color: #F8FAFC;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 16px;
    color: #9CA3AF;
    margin-bottom: 35px;
}

.status-card {
    background: linear-gradient(135deg, #122016, #0B2B1A);
    border: 1px solid #22C55E;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 8px 28px rgba(34, 197, 94, 0.15);
}

.kpi-card {
    background: rgba(17, 24, 39, 0.92);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.28);
    min-height: 145px;
}

.kpi-label {
    color: #9CA3AF;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
}

.kpi-value {
    color: #F8FAFC;
    font-size: 31px;
    font-weight: 800;
    word-break: break-word;
}

.section-card {
    background: rgba(17, 24, 39, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
    margin-bottom: 20px;
}

.alert-high {
    background: linear-gradient(135deg, rgba(127,29,29,0.75), rgba(69,10,10,0.85));
    border: 1px solid rgba(248,113,113,0.45);
    border-radius: 16px;
    padding: 18px;
    color: #FCA5A5;
    font-weight: 700;
}

.alert-normal {
    background: linear-gradient(135deg, rgba(20,83,45,0.75), rgba(5,46,22,0.85));
    border: 1px solid rgba(74,222,128,0.45);
    border-radius: 16px;
    padding: 18px;
    color: #86EFAC;
    font-weight: 700;
}

.blue-box {
    background: linear-gradient(135deg, rgba(30,64,175,0.55), rgba(15,23,42,0.85));
    border: 1px solid rgba(96,165,250,0.35);
    border-radius: 16px;
    padding: 18px;
}

.green-box {
    background: linear-gradient(135deg, rgba(22,101,52,0.55), rgba(15,23,42,0.85));
    border: 1px solid rgba(74,222,128,0.35);
    border-radius: 16px;
    padding: 18px;
}

.flow-box {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(59,130,246,0.35);
    border-radius: 14px;
    padding: 14px 10px;
    text-align: center;
    font-weight: 700;
    color: #DBEAFE;
    min-height: 70px;
    font-size: 13px;
}

.note-box {
    background: rgba(113, 63, 18, 0.35);
    border: 1px solid rgba(234,179,8,0.35);
    border-radius: 16px;
    padding: 16px;
    color: #FEF3C7;
    font-size: 15px;
}

.bar-card {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 10px;
}

.bar-label {
    display: flex;
    justify-content: space-between;
    color: #F8FAFC;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 6px;
}

.bar-bg {
    background: rgba(51, 65, 85, 0.85);
    border-radius: 999px;
    height: 13px;
    overflow: hidden;
}

.bar-fill {
    background: linear-gradient(90deg, #38BDF8, #2563EB);
    height: 13px;
    border-radius: 999px;
}

div[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

hr {
    border: none;
    border-top: 1px solid rgba(148, 163, 184, 0.18);
    margin: 30px 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Simulated IDS Logic
# -------------------------------------------------
attack_types = ["Normal", "DDoS", "Spoofing", "Malware", "Ransomware"]
prediction = random.choice(attack_types)
confidence = round(random.uniform(0.72, 0.98), 2)
uncertainty = round(1 - confidence, 2)

if prediction == "Normal":
    risk = "Low"
    selected_expert = "ML Expert: RF / LightGBM"
    hyper_mode = "Low-computation monitoring mode"
elif prediction in ["DDoS", "Spoofing"]:
    risk = random.choice(["Medium", "High"])
    selected_expert = "CNN Expert"
    hyper_mode = "Traffic-pattern sensitivity mode"
else:
    risk = "High"
    selected_expert = "FT-Transformer Expert"
    hyper_mode = "High-sensitivity deep analysis mode"

risk_display = {
    "Low": "🟢 Low",
    "Medium": "🟠 Medium",
    "High": "🔴 High"
}

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown('<div class="main-title">🔐 HyperGate-MoE-IDS Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Adaptive IoMT intrusion-detection prototype using Hypernetwork control, MoE expert routing, uncertainty estimation, and risk-aware decision logic.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="status-card">
    <h3 style="margin:0;">🟢 System Status: Operational</h3>
    <p style="margin:8px 0 0 0; color:#BBF7D0;">Live simulation engine active · Monitoring IoMT traffic streams · Adaptive routing enabled</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Traffic Classification</div>
        <div class="kpi-value">{prediction}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Confidence Score</div>
        <div class="kpi-value">{confidence}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Uncertainty Score</div>
        <div class="kpi-value">{uncertainty}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Risk Level</div>
        <div class="kpi-value">{risk_display[risk]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Detection + Adaptive Behaviour
# -------------------------------------------------
left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📊 Detection Result")

    if prediction == "Normal":
        st.markdown(
            '<div class="alert-normal">Current traffic is classified as Normal. No immediate cyber threat detected.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="alert-high">Potential cyber threat detected: {prediction}</div>',
            unsafe_allow_html=True
        )

    st.markdown("#### Decision Interpretation")
    st.write(
        "The system combines prediction confidence, uncertainty level, and device-risk context before generating the final alert."
    )
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🧠 Adaptive Model Behaviour")

    st.markdown(f"""
    <div class="blue-box">
        <b>⚙️ Hypernetwork Control</b><br><br>
        Adaptive mode activated: <b>{hyper_mode}</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="green-box">
        <b>🧩 MoE Expert Selection</b><br><br>
        Selected expert: <b>{selected_expert}</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# Alerts + Explainability
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)

colA, colB = st.columns([1.1, 1])

with colA:
    st.subheader("🚨 Alerts Panel")

    alerts = pd.DataFrame({
        "Time": ["10:01", "10:05", "10:10", "10:14"],
        "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03", "Pump-04"],
        "Threat": ["DDoS", "Spoofing", "Malware", prediction],
        "Risk": ["High", "Medium", "High", risk],
        "Confidence": [0.94, 0.88, 0.91, confidence]
    })

    st.dataframe(alerts, use_container_width=True, hide_index=True)

with colB:
    st.subheader("🧠 Explainability")

    features = ["Packet Rate", "Flow Duration", "Protocol Entropy", "Byte Count", "Connection Frequency"]
    importance = [round(random.uniform(0.15, 0.95), 2) for _ in features]

    explain_df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    top_feature = explain_df.iloc[0]["Feature"]
    st.write(f"Top influencing feature: **{top_feature}**")

    for _, row in explain_df.iterrows():
        percentage = int(row["Importance"] * 100)
        st.markdown(f"""
        <div class="bar-card">
            <div class="bar-label">
                <span>{row["Feature"]}</span>
                <span>{row["Importance"]}</span>
            </div>
            <div class="bar-bg">
                <div class="bar-fill" style="width:{percentage}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# System Flow
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("🔄 System Flow Simulation")

flow_steps = [
    "IoMT Data",
    "Preprocessing",
    "Context Encoding",
    "Hypernetwork Adaptation",
    "MoE Routing",
    "Prediction + Uncertainty",
    "Risk Decision",
    "Alert + Explainability"
]

flow_cols = st.columns(len(flow_steps))

for i, step in enumerate(flow_steps):
    with flow_cols[i]:
        st.markdown(f'<div class="flow-box">{step}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# Prototype Note + Refresh
# -------------------------------------------------
st.markdown("""
<div class="note-box">
    <b>Prototype note:</b> This dashboard simulates the behaviour of the proposed HyperGate-MoE-IDS architecture.
    It does not yet implement the full trained Hypernetwork or MoE model.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔁 Refresh Simulation", use_container_width=True):
    st.rerun()
