import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="SecureFair AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* Main app background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0f172a);
    color: white;
}

/* Remove default top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Hero title */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0.2rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

/* Glass card style */
.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 1.2rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    margin-bottom: 1rem;
}

/* Metric cards */
.metric-card {
    background: white;
    color: #0f172a;
    padding: 1rem;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    text-align: center;
    min-height: 120px;
}

.metric-title {
    font-size: 1rem;
    color: #475569;
    font-weight: 600;
}

.metric-value {
    font-size: 2rem;
    font-weight: 800;
    margin-top: 0.4rem;
}

/* Risk badges */
.badge-low {
    display: inline-block;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    background: #dcfce7;
    color: #166534;
    font-weight: 700;
}

.badge-medium {
    display: inline-block;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    background: #fef3c7;
    color: #92400e;
    font-weight: 700;
}

.badge-high {
    display: inline-block;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    background: #fee2e2;
    color: #991b1b;
    font-weight: 700;
}

/* Section heading */
.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: white;
    margin-top: 1rem;
    margin-bottom: 0.8rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1f2937);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1rem;
    font-size: 1rem;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(59,130,246,0.35);
}

.stButton>button:hover {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
}

/* Text area and inputs */
textarea, input, .stSelectbox, .stNumberInput, .stSlider {
    border-radius: 12px !important;
}

/* Fix white background containers */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0f172a);
}

/* Main content area */
[data-testid="stVerticalBlock"] {
    background: transparent;
}

/* Streamlit elements */
[data-testid="stMetric"] {
    background-color: transparent !important;
}

/* Fix chart background */
canvas {
    background-color: transparent !important;
}

/* Dataframe background */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.05);
}

/* Markdown containers */
[data-testid="stMarkdownContainer"] {
    background: transparent;
}

/* Sidebar inputs */
section[data-testid="stSidebar"] input,
section[data-testid="stSidebar"] textarea,
section[data-testid="stSidebar"] .stSlider {
    background-color: #1f2937 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
try:
    model = joblib.load("outputs/model.pkl")
    model_columns = joblib.load("outputs/model_columns.pkl")
except:
    model = None
    model_columns = []

# ---------- HERO SECTION ----------
st.markdown('<div class="hero-title">🛡️ SecureFair AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Ethical, Explainable and Secure AI for Employee Resignation Prediction</div>',
    unsafe_allow_html=True
)

# ---------- TABS ----------
tab_pred, tab_analytics, tab_responsible = st.tabs(["🔮 Prediction", "📊 Analytics", "🛡️ Responsible AI"])

# ---------- SIDEBAR ----------
st.sidebar.markdown("## Employee Input")
salary = st.sidebar.slider("Salary", 30000, 150000, 60000)
engagement = st.sidebar.slider("Engagement Survey", 1.0, 5.0, 3.0)
satisfaction = st.sidebar.slider("Employee Satisfaction", 1, 5, 3)
absences = st.sidebar.slider("Absences", 0, 30, 5)
days_late = st.sidebar.slider("Days Late Last 30 Days", 0, 10, 1)
special_projects = st.sidebar.slider("Special Projects Count", 0, 10, 2)

feedback = st.sidebar.text_area(
    "Employee Feedback",
    "I feel my workload is too high and growth opportunities are limited."
)

def simple_sentiment(text):
    text = text.lower()
    negative_words = ["stress", "underpaid", "leave", "bad", "limited", "poor", "high workload", "micromanagement"]
    positive_words = ["supportive", "growth", "good", "happy", "balanced", "great"]

    neg = sum(word in text for word in negative_words)
    pos = sum(word in text for word in positive_words)

    if neg > pos:
        return -0.5, "Negative"
    elif pos > neg:
        return 0.4, "Positive"
    return 0.0, "Neutral"

sentiment_score, sentiment_label = simple_sentiment(feedback)

# ---------- INPUT DATA ----------
input_dict = {
    "Salary": salary,
    "EngagementSurvey": engagement,
    "EmpSatisfaction": satisfaction,
    "Absences": absences,
    "DaysLateLast30": days_late,
    "SpecialProjectsCount": special_projects,
    "sentiment_score": sentiment_score
}

input_df = pd.DataFrame([input_dict])

for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0

if model_columns:
    input_df = input_df[model_columns]

with tab_pred:
    if st.sidebar.button("🚀 Predict Resignation Risk"):
        if model is None:
            st.error("Model files not found. Please train and save the model first.")
        else:
            risk = model.predict_proba(input_df)[0][1]
            risk_percent = round(risk * 100, 1)

            if risk > 0.7:
                risk_label = "High Risk"
                badge_class = "badge-high"
            elif risk > 0.4:
                risk_label = "Moderate Risk"
                badge_class = "badge-medium"
            else:
                risk_label = "Low Risk"
                badge_class = "badge-low"

            reasons = []
            actions = []

            if satisfaction <= 2:
                reasons.append("Low employee satisfaction")
                actions.append("Schedule a manager check-in")
            if engagement <= 2.5:
                reasons.append("Low engagement level")
                actions.append("Review role fit and motivation")
            if absences >= 10:
                reasons.append("High absence frequency")
                actions.append("Assess workload and well-being")
            if sentiment_score < 0:
                reasons.append("Negative feedback sentiment")
                actions.append("Analyze employee concerns in detail")

            if not reasons:
                reasons.append("No major risk factors detected")
                actions.append("Continue monitoring employee well-being")

            # Top metrics row
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Resignation Risk</div>
                    <div class="metric-value">{risk_percent}%</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Risk Level</div>
                    <div style="margin-top: 1rem;"><span class="{badge_class}">{risk_label}</span></div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Feedback Sentiment</div>
                    <div class="metric-value">{sentiment_label}</div>
                </div>
                """, unsafe_allow_html=True)

            # Main content
            left, right = st.columns([1.4, 1])

            with left:
                st.markdown('<div class="section-title">Why is this employee at risk?</div>', unsafe_allow_html=True)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                for reason in reasons:
                    st.write(f"• {reason}")
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="section-title">Recommended Actions</div>', unsafe_allow_html=True)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                for action in actions:
                    st.write(f"• {action}")
                st.markdown('</div>', unsafe_allow_html=True)

            with right:
                st.markdown('<div class="section-title">Quick Insights</div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="card">
                <b>Salary:</b> ${salary:,}<br>
                <b>Engagement:</b> {engagement}/5.0<br>
                <b>Absences:</b> {absences} days
                </div>
                """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="card">
        <h3 style="margin-top:0; color:white;">Welcome to SecureFair AI</h3>
        <p style="color:#e2e8f0;">
        This dashboard helps HR teams predict resignation risk using structured employee metrics
        and feedback sentiment, while respecting fairness, privacy, and explainability principles.
        </p>
        <p style="color:#cbd5e1;">
        Use the sidebar to enter employee information and click <b>Predict Resignation Risk</b>.
        </p>
        </div>
        """, unsafe_allow_html=True)

with tab_analytics:
    st.markdown('<div class="section-title">System Analytics</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Top Risk Drivers")
        if os.path.exists("outputs/plots/top_features.png"):
            st.image("outputs/plots/top_features.png", use_container_width=True)
        else:
            st.info("Feature importance plot not found.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Model Explainability (SHAP)")
        if os.path.exists("outputs/plots/shap_summary.png"):
            st.image("outputs/plots/shap_summary.png", use_container_width=True)
        else:
            st.info("SHAP summary plot not found.")
        st.markdown('</div>', unsafe_allow_html=True)

with tab_responsible:
    st.markdown('<div class="section-title">Responsible AI Controls</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    ✅ <b>Fairness:</b> Sensitive attributes (Sex, Race) excluded from training to prevent structural bias.<br><br>
    ✅ <b>Privacy:</b> Personal identifiers removed and data anonymized for GDPR alignment.<br><br>
    ✅ <b>Explainability:</b> Uses SHAP values to provide transparent reasoning for risk scores.<br><br>
    ✅ <b>Human-in-the-Loop:</b> Designed as a decision support system; final decisions require human review.
    </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("outputs/fairness_report.csv"):
        st.write("### Latest Fairness Audit Results")
        fairness_df = pd.read_csv("outputs/fairness_report.csv")
        st.dataframe(fairness_df, use_container_width=True)

# Footer
st.markdown("<br><hr><center>SecureFair AI v1.0 | Hackathon 2026</center>", unsafe_allow_html=True)
