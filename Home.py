import streamlit as st

st.set_page_config(
    page_title="MediScan AI",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    .stApp { background-color: #060610; color: #e8e8f0; }
    section[data-testid="stSidebar"] { display: none; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 0 !important; max-width: 1100px !important; }

    /* Equal height columns */
    div[data-testid="column"] {
        display: flex !important;
        flex-direction: column !important;
        padding: 0.4rem !important;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 4rem 2rem 2rem;
    }
    .hero, .hero * { text-align: center !important; }
    .hero-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.78rem;
        font-weight: 500;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: #5b5bff;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        line-height: 1.05;
        color: #ffffff;
        margin: 0 0 1.2rem;
    }
    .hero-title span {
        background: linear-gradient(90deg, #5b5bff, #00e5ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .hero-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.05rem;
        color: #7878a0;
        max-width: 700px;
        width: 100%;
        margin: 0 auto 2rem;
        line-height: 1.7;
        display: block;
    }

    /* Stats */
    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 3rem;
        padding: 1.5rem 2rem;
        background: #0a0a18;
        border-top: 1px solid #1a1a30;
        border-bottom: 1px solid #1a1a30;
        margin-bottom: 2.5rem;
        flex-wrap: wrap;
    }
    .stat-item { text-align: center; }
    .stat-num {
        font-family: 'Syne', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        color: #5b5bff;
    }
    .stat-label {
        font-size: 0.75rem;
        color: #55558a;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .section-label {
        font-family: 'Syne', sans-serif;
        font-size: 0.72rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #44446a;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    /* Card — flex column so tag always sticks to bottom */
    .card {
        background: #0e0e1e;
        border-radius: 16px;
        padding: 1.8rem 1.6rem 1.4rem;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
        height: 100%;
        box-sizing: border-box;
    }
    .card-body { flex: 1; }
    .card-icon { font-size: 2.2rem; margin-bottom: 0.8rem; display: block; }
    .card-title {
        font-family: 'Syne', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .card-desc {
        font-size: 0.83rem;
        color: #55558a;
        line-height: 1.6;
        margin-bottom: 1.2rem;
    }
    .card-footer { margin-top: auto; }
    .tag-ready {
        display: inline-block;
        font-size: 0.68rem;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 0.22rem 0.6rem;
        border-radius: 20px;
        color: #00e5a0;
        border: 1px solid #00e5a033;
        background: #00e5a010;
    }
    .tag-soon {
        display: inline-block;
        font-size: 0.68rem;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 0.22rem 0.6rem;
        border-radius: 20px;
        color: #7878a0;
        border: 1px solid #7878a033;
        background: #7878a010;
    }

    /* Accent top borders */
    .accent-brain  { border-top: 3px solid #5b5bff; }
    .accent-lung   { border-top: 3px solid #ff5b8a; }
    .accent-kidney { border-top: 3px solid #00e5b0; }
    .accent-retina { border-top: 3px solid #c75bff; }
    .accent-skin   { border-top: 3px solid #ffcc00; }
    .accent-chest  { border-top: 3px solid #00ffaa; }

    .footer {
        text-align: center;
        padding: 2.5rem 2rem;
        font-size: 0.78rem;
        color: #2a2a4a;
        border-top: 1px solid #12122a;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# ---- HERO ----
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">AI-Powered Medical Imaging</div>
    <h1 class="hero-title">MediScan <span>AI</span></h1>
    <p class="hero-eyebrow">
        Deep learning diagnostic tools for medical imaging. <br>
        Select a scan type below to begin analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- STATS ----
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">7.5M</div>
        <div class="stat-label">Model Parameters</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">VRF-Net</div>
        <div class="stat-label">Architecture</div>
    </div>
</div>
<div class="section-label">— Select a diagnostic module —</div>
""", unsafe_allow_html=True)

# ---- CARDS ROW 1 ----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card accent-brain">
        <div class="card-body">
            <span class="card-icon">🧠</span>
            <div class="card-title">Brain Tumor Classification</div>
        </div>
        <div class="card-footer"><span class="tag-ready">✓ Ready</span></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🧠 → Open Classifier", key="brain_btn", use_container_width=True):
        st.switch_page("pages/1_brain_tumor_classification.py")

with col2:
    st.markdown("""
    <div class="card accent-lung">
        <div class="card-body">
            <span class="card-icon">🫁</span>
            <div class="card-title">Lung Disease Classification</div>
        </div>
        <div class="card-footer"><span class="tag-ready">✓ Ready</span></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🫁 → Open Classifier", key="lungs_btn", use_container_width=True):
            st.switch_page("pages/2_lungs_disease_classification.py")

with col3:
    st.markdown("""
    <div class="card accent-kidney">
        <div class="card-body">
            <span class="card-icon">🫘</span>
            <div class="card-title">Kidney Stone Classification</div>
        </div>
        <div class="card-footer"><span class="tag-ready">✓ Ready</span></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🫘 → Open Classifier", key="kidney_btn", use_container_width=True):
        st.switch_page("pages/3_kidney_stone_classification.py")

# ---- CARDS ROW 2 ----
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card accent-retina">
        <div class="card-body">
            <span class="card-icon">👁️</span>
            <div class="card-title">Retinal Disease Analysis</div>
        </div>
        <div class="card-footer"><span class="tag-ready">✓ Ready</span></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👁️ → Open Classifier", key="eye_btn", use_container_width=True):
            st.switch_page("pages/4_eye_disease_classification.py")

with col5:
    st.markdown("""
    <div class="card accent-skin">
        <div class="card-body">
            <span class="card-icon">🩹</span>
            <div class="card-title">Skin Lesion Classification</div>
        </div>
        <div class="card-footer"><span class="tag-soon">Coming Soon</span></div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card accent-chest">
        <div class="card-body">
            <span class="card-icon">🩻</span>
            <div class="card-title">Fracture X-Ray Analysis</div>
        </div>
        <div class="card-footer"><span class="tag-soon">Coming Soon</span></div>
    </div>
    """, unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""
<div class="footer">
    ⚠️ For research and educational use only · Not a substitute for professional medical diagnosis<br>
    MediScan AI · Built with TensorFlow &amp; Streamlit
</div>
""", unsafe_allow_html=True)