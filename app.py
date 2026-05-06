import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="HyperGate-MoE-IDS Dashboard",
    page_icon="🔐",
    layout="wide"
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
with st.sidebar:
    st.markdown("## 🔐 HyperGate")
    st.markdown("### Navigation")
    st.markdown("🧭 Dashboard")
    st.markdown("🏥 Devices")
    st.markdown("🚨 Alerts")
    st.markdown("🧠 Models")
    st.markdown("📊 Explainability")
    st.markdown("⚙️ Settings")
    st.markdown("---")
    st.markdown("**System Mode:** Live Simulation")
    st.markdown("**Deployment:** Edge–Fog–Cloud")
    st.markdown("**Version:** Prototype v1.0")

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown("""
<style>
header[data-testid="stHeader"] {
    height: 0rem;
    background: transparent;
}

.stApp {
    background: linear-gradient(135deg, #080B12 0%, #0E1117 45%, #111827 100%);
    color: #F8FAFC;
}

.block-container {
    padding-top: 3.8rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

.main-title {
    font-size: clamp(28px, 3.4vw, 38px);
    font-weight: 900;
    color: #F8FAFC;
    line-height: 1.2;
    white-space: normal;
    word-break: normal;
    margin-bottom: 12px;
}

.subtitle {
    font-size: 16px;
    color: #9CA3AF;
    margin-bottom: 22px;
}

.top-filter {
    background: rgba(15,23,42,0.9);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 18px;
    padding: 14px 18px;
    margin-bottom: 20px;
    color: #CBD5E1;
}

.status-card {
    background: linear-gradient(135deg, #122016, #0B2B1A);
    border: 1px solid #22C55E;
    border-radius: 18px;
    padding: 20px 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 28px rgba(34,197,94,0.15);
}

.kpi-card, .section-card, .arch-card {
    background: rgba(17,24,39,0.92);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.28);
    margin-bottom: 18px;
}

.kpi-label {
    color: #9CA3AF;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 12px;
}

.kpi-value {
    color: #F8FAFC;
    font-size: 31px;
    font-weight: 900;
    word-break: break-word;
}

.arch-card {
    background: linear-gradient(135deg, rgba(15,23,42,0.96), rgba(30,41,59,0.72));
    border: 1px solid rgba(56,189,248,0.28);
}

.arch-title, .info-title {
    color: #F8FAFC;
    font-size: 18px;
    font-weight: 900;
    margin-bottom: 10px;
}

.info-line {
    color: #CBD5E1;
    font-size: 15px;
    margin-bottom: 8px;
}

.info-value {
    color: #F8FAFC;
    font-weight: 800;
}

.recommend-high {
    background: linear-gradient(135deg, rgba(127,29,29,0.65), rgba(30,41,59,0.78));
    border: 1px solid rgba(248,113,113,0.40);
}

.recommend-medium {
    background: linear-gradient(135deg, rgba(124,45,18,0.65), rgba(30,41,59,0.78));
    border: 1px solid rgba(251,146,60,0.40);
}

.recommend-low {
    background: linear-gradient(135deg, rgba(20,83,45,0.65), rgba(30,41,59,0.78));
    border: 1px solid rgba(74,222,128,0.40);
}

.performance-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 12px;
}

.perf-box {
    background: rgba(15,23,42,0.95);
    border: 1px solid rgba(56,189,248,0.22);
    border-radius: 14px;
    padding: 14px;
    text-align: center;
}

.perf-label {
    color: #94A3B8;
    font-size: 13px;
    font-weight: 700;
}

.perf-value {
    color: #F8FAFC;
    font-size: 22px;
    font-weight: 900;
}

.alert-high {
    background: linear-gradient(135deg, rgba(127,29,29,0.75), rgba(69,10,10,0.85));
    border: 1px solid rgba(248,113,113,0.45);
    border-radius: 16px;
    padding: 18px;
    color: #FCA5A5;
    font-weight: 800;
}

.alert-normal {
    background: linear-gradient(135deg, rgba(20,83,45,0.75), rgba(5,46,22,0.85));
    border: 1px solid rgba(74,222,128,0.45);
    border-radius: 16px;
    padding: 18px;
    color: #86EFAC;
    font-weight: 800;
}

.blue-box, .green-box {
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 14px;
}

.blue-box {
    background: linear-gradient(135deg, rgba(30,64,175,0.55), rgba(15,23,42,0.85));
    border: 1px solid rgba(96,165,250,0.35);
}

.green-box {
    background: linear-gradient(135deg, rgba(22,101,52,0.55), rgba(15,23,42,0.85));
    border: 1px solid rgba(74,222,128,0.35);
}

.expert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 10px;
}

.expert-card {
    background: rgba(15,23,42,0.95);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    color: #CBD5E1;
}

.expert-active {
    border: 1px solid #38BDF8;
    box-shadow: 0 0 22px rgba(56,189,248,0.25);
    color: #F8FAFC;
}

.bar-card {
    background: rgba(15,23,42,0.95);
    border: 1px solid rgba(148,163,184,0.16);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 10px;
}

.bar-label {
    display: flex;
    justify-content: space-between;
    color: #F8FAFC;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 6px;
}

.bar-bg {
    background: rgba(51,65,85,0.85);
    border-radius: 999px;
    height: 13px;
    overflow: hidden;
}

.bar-fill {
    background: linear-gradient(90deg, #38BDF8, #2563EB);
    height: 13px;
    border-radius: 999px;
}

.flow-wrap {
    display: flex;
    align-items: stretch;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 14px;
}

.flow-box {
    background: rgba(15,23,42,0.95);
    border: 1px solid rgba(59,130,246,0.40);
    border-radius: 14px;
    padding: 14px 12px;
    text-align: center;
    font-weight: 800;
    color: #DBEAFE;
    min-height: 58px;
    font-size: 13px;
    flex: 1;
    min-width: 130px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.flow-arrow {
    color: #38BDF8;
    font-size: 24px;
    font-weight: 900;
    display: flex;
    align-items: center;
}

.note-box {
    background: rgba(113,63,18,0.35);
    border: 1px solid rgba(234,179,8,0.35);
    border-radius: 16px;
    padding: 16px;
    color: #FEF3C7;
    font-size: 15px;
}

div[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

hr {
    border: none;
    border-top: 1px solid rgba(148,163,184,0.18);
    margin: 26px 0;
}

@media (max-width: 900px) {
    .main-title {
        font-size: 32px;
    }

    .performance-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .expert-grid {
        grid-template-columns: repeat(1, 1fr);
    }
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Simulated IDS Logic
# -------------------------------------------------
attack_types = ["Normal", "DDoS", "Spoofing", "Malware", "Ransomware"]
devices = [
    ("Sensor-01", "Vital Sensor", "Moderate"),
    ("Monitor-02", "Patient Monitor", "High"),
    ("Wearable-03", "Wearable Device", "Medium"),
    ("Pump-04", "Infusion Pump", "Critical"),
    ("Gateway-05", "IoMT Gateway", "High")
]

prediction = random.choice(attack_types)
confidence = round(random.uniform(0.72, 0.98), 2)
uncertainty = round(1 - confidence, 2)
device_id, device_type, sensitivity = random.choice(devices)

if prediction == "Normal":
    risk = "Low"
    selected_expert = "ML Expert: RF / LightGBM"
    hyper_mode = "Low-computation monitoring mode"
    recommended_action = "Continue monitoring and store the event in the audit log."
    recommendation_class = "recommend-low"
elif prediction in ["DDoS", "Spoofing"]:
    risk = random.choice(["Medium", "High"])
    selected_expert = "CNN Expert"
    hyper_mode = "Traffic-pattern sensitivity mode"
    recommended_action = "Increase monitoring sensitivity and validate traffic source integrity."
    recommendation_class = "recommend-medium" if risk == "Medium" else "recommend-high"
else:
    risk = "High"
    selected_expert = "FT-Transformer Expert"
    hyper_mode = "High-sensitivity deep analysis mode"
    recommended_action = "Isolate the affected device, trigger high-priority alert, and escalate to SOC review."
    recommendation_class = "recommend-high"

risk_display = {"Low": "🟢 Low", "Medium": "🟠 Medium", "High": "🔴 High"}

active_devices = random.randint(22, 38)
packets_per_sec = random.randint(950, 1850)
blocked_attempts = random.randint(6, 24) if risk != "Low" else random.randint(0, 4)
avg_latency = random.randint(12, 28)

# -------------------------------------------------
# Header + Filter Bar
# -------------------------------------------------
st.markdown(
    '<div class="main-title">🔐&nbsp; HyperGate-MoE-IDS Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Adaptive IoMT intrusion-detection prototype using Hypernetwork control, MoE expert routing, uncertainty estimation, and risk-aware decision logic.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="top-filter">
    ⏱️ Time Window: <b>This Week</b> &nbsp;&nbsp; | &nbsp;&nbsp;
    🏥 Device Group: <b>All IoMT Devices</b> &nbsp;&nbsp; | &nbsp;&nbsp;
    🚨 Risk Filter: <b>High + Medium</b> &nbsp;&nbsp; | &nbsp;&nbsp;
    📥 Report: <b>Ready for Export</b>
</div>
""", unsafe_allow_html=True)

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
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Traffic Classification</div><div class="kpi-value">{prediction}</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Confidence Score</div><div class="kpi-value">{confidence}</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Uncertainty Score</div><div class="kpi-value">{uncertainty}</div></div>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Risk Level</div><div class="kpi-value">{risk_display[risk]}</div></div>', unsafe_allow_html=True)

# -------------------------------------------------
# Architecture Summary
# -------------------------------------------------
st.markdown(f"""
<div class="arch-card">
    <div class="arch-title">🧬 Architecture Summary</div>
    Hypernetwork control adjusts model behaviour according to traffic context and uncertainty.
    MoE routing selects the most suitable expert model, while risk-aware logic converts the prediction into an operational security alert.
    <br><br>
    <b>Current route:</b> {hyper_mode} → {selected_expert} → {risk} risk decision.
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Live Operational Intelligence
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📡 Live Operational Intelligence")

op1, op2, op3 = st.columns(3)

with op1:
    st.markdown(f"""
    <div class="section-card">
        <div class="info-title">🏥 Device Context</div>
        <div class="info-line"><span class="info-value">Device ID:</span> {device_id}</div>
        <div class="info-line"><span class="info-value">Device Type:</span> {device_type}</div>
        <div class="info-line"><span class="info-value">Sensitivity:</span> {sensitivity}</div>
        <div class="info-line"><span class="info-value">Priority:</span> {"Urgent" if risk == "High" else "Standard"}</div>
    </div>
    """, unsafe_allow_html=True)

with op2:
    st.markdown(f"""
    <div class="section-card {recommendation_class}">
        <div class="info-title">🛡️ Risk Recommendation</div>
        <div class="info-line"><span class="info-value">Recommended Action:</span></div>
        <div class="info-line">{recommended_action}</div>
    </div>
    """, unsafe_allow_html=True)

with op3:
    st.markdown(f"""
    <div class="section-card">
        <div class="info-title">⚡ Runtime Summary</div>
        <div class="info-line"><span class="info-value">Active Devices:</span> {active_devices}</div>
        <div class="info-line"><span class="info-value">Packets/sec:</span> {packets_per_sec}</div>
        <div class="info-line"><span class="info-value">Blocked Attempts:</span> {blocked_attempts}</div>
        <div class="info-line"><span class="info-value">Avg Latency:</span> {avg_latency} ms</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Visual Analytics
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📊 Threat Analytics Overview")

v1, v2, v3 = st.columns([1, 1.2, 1])

with v1:
    st.markdown('<div class="section-card"><div class="info-title">🧩 Threat Distribution</div>', unsafe_allow_html=True)
    threat_dist = {
        "DDoS": random.randint(20, 40),
        "Spoofing": random.randint(15, 35),
        "Malware": random.randint(10, 30),
        "Ransomware": random.randint(5, 20),
        "Normal": random.randint(20, 45)
    }
    total = sum(threat_dist.values())
    for threat, count in threat_dist.items():
        pct = int((count / total) * 100)
        st.markdown(f"""
        <div class="bar-card">
            <div class="bar-label"><span>{threat}</span><span>{pct}%</span></div>
            <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with v2:
    st.markdown('<div class="section-card"><div class="info-title">📈 Live Traffic Trend</div>', unsafe_allow_html=True)
    traffic_df = pd.DataFrame({
        "Time": [f"T-{i}" for i in range(20, 0, -1)],
        "Packets/sec": [random.randint(800, 1900) for _ in range(20)]
    }).set_index("Time")
    st.line_chart(traffic_df, use_container_width=True, height=260)
    st.markdown('</div>', unsafe_allow_html=True)

with v3:
    st.markdown("""
    <div class="section-card">
        <div class="info-title">🌍 Attack-Origin Intelligence</div>
        <div class="info-line"><span class="info-value">Top Source Region:</span> External Network</div>
        <div class="info-line"><span class="info-value">Suspicious IPs:</span> 14</div>
        <div class="info-line"><span class="info-value">Most Targeted Asset:</span> IoMT Gateway</div>
        <div class="info-line"><span class="info-value">Dominant Pattern:</span> Burst Traffic</div>
        <div class="info-line"><span class="info-value">Geo Status:</span> Multi-source probing detected</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Model Performance + Expert Routing
# -------------------------------------------------
st.markdown("""
<div class="arch-card">
    <div class="arch-title">📈 Model Performance Snapshot</div>
    <div class="performance-grid">
        <div class="perf-box"><div class="perf-label">Accuracy</div><div class="perf-value">96.4%</div></div>
        <div class="perf-box"><div class="perf-label">Precision</div><div class="perf-value">94.1%</div></div>
        <div class="perf-box"><div class="perf-label">Recall</div><div class="perf-value">95.7%</div></div>
        <div class="perf-box"><div class="perf-label">F1-score</div><div class="perf-value">94.9%</div></div>
        <div class="perf-box"><div class="perf-label">Latency</div><div class="perf-value">18 ms</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arch-card"><div class="arch-title">🧠 MoE Expert Routing Visual</div><div class="expert-grid">', unsafe_allow_html=True)

experts = ["ML Expert: RF / LightGBM", "CNN Expert", "FT-Transformer Expert"]
for expert in experts:
    active_class = "expert-active" if expert == selected_expert else ""
    st.markdown(f"""
    <div class="expert-card {active_class}">
        <b>{expert}</b><br><br>
        {"✅ Selected for current traffic" if expert == selected_expert else "Standby expert"}
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------------------------------------
# Detection + Adaptive Behaviour
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)

left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📊 Detection Result")

    if prediction == "Normal":
        st.markdown('<div class="alert-normal">Current traffic is classified as Normal. No immediate cyber threat detected.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="alert-high">Potential cyber threat detected: {prediction}</div>', unsafe_allow_html=True)

    st.markdown("#### Decision Interpretation")
    st.write("The system combines prediction confidence, uncertainty level, and device-risk context before generating the final alert.")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🧠 Adaptive Model Behaviour")

    st.markdown(f"""
    <div class="blue-box">
        <b>⚙️ Hypernetwork Control</b><br><br>
        Adaptive mode activated: <b>{hyper_mode}</b>
    </div>
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
        "Device ID": ["Sensor-01", "Monitor-02", "Wearable-03", device_id],
        "Threat": ["DDoS", "Spoofing", "Malware", prediction],
        "Risk": ["High", "Medium", "High", risk],
        "Confidence": [0.94, 0.88, 0.91, confidence],
        "Status": ["Escalated", "Monitoring", "Investigating", "New"],
        "Action": ["Block", "Validate", "Isolate", "Review"]
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
            <div class="bar-label"><span>{row["Feature"]}</span><span>{row["Importance"]}</span></div>
            <div class="bar-bg"><div class="bar-fill" style="width:{percentage}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# System Flow
# -------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("🔄 System Flow Simulation")

flow_steps = [
    "IoMT Data", "Preprocessing", "Context Encoding", "Hypernetwork Adaptation",
    "MoE Routing", "Prediction + Uncertainty", "Risk Decision", "Alert + Explainability"
]

flow_html = '<div class="flow-wrap">'
for i, step in enumerate(flow_steps):
    flow_html += f'<div class="flow-box">{step}</div>'
    if i != len(flow_steps) - 1:
        flow_html += '<div class="flow-arrow">→</div>'
flow_html += '</div>'

st.markdown(flow_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="note-box">
    <b>Prototype note:</b> This dashboard simulates the behaviour of the proposed HyperGate-MoE-IDS architecture.
    It does not yet implement the full trained Hypernetwork or MoE model. Performance values are illustrative for prototype demonstration.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔁 Refresh Simulation", use_container_width=True):
    st.rerun()
