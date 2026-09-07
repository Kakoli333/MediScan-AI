import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Kidney Stone Classifier",
    page_icon="🫘",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'IBM Plex Mono', monospace !important;
        letter-spacing: -0.5px;
    }
    .stApp {
        background-color: #0d0d0d;
        color: #e8e8e8;
    }
    .main-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 2rem;
        font-weight: 600;
        color: #00e5ff;
        border-bottom: 2px solid #00e5ff44;
        padding-bottom: 0.5rem;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.9rem;
        color: #888;
        margin-bottom: 2rem;
    }
            
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

    .result-box {
        background: #1a1a2e;
        border: 1px solid #00e5ff33;
        border-left: 4px solid #00e5ff;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
    }
    .result-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.75rem;
        color: #00e5ff99;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0.3rem;
    }
    .result-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        text-transform: uppercase;
    }
    .confidence-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.2rem;
        color: #00e5ff;
    }
    .prob-bar-container {
        margin: 0.4rem 0;
    }
    .prob-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.8rem;
        color: #aaa;
        margin-bottom: 2px;
        text-transform: uppercase;
    }
    .disclaimer {
        background: #1a1a0d;
        border: 1px solid #ffcc0033;
        border-left: 4px solid #ffcc00;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        font-size: 0.82rem;
        color: #ccaa44;
        margin-top: 2rem;
    }
    .stFileUploader > div {
        border: 2px dashed #00e5ff44 !important;
        border-radius: 10px !important;
        background: #111 !important;
    }
    .stProgress > div > div {
        background-color: #00e5ff !important;
    }
    div[data-testid="stImage"] img {
        border-radius: 10px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Class Names & Descriptions
# -------------------------
CLASS_NAMES = ["Non-Stone", "Stone"]

CLASS_INFO = {
    "Non-Stone": "There is no stone in the kidney.",
    "Stone":     "There is stone in the kidney.",
}

# -------------------------
# Load Model
# -------------------------
@st.cache_resource
def load_model():
    try:
        import keras
        from keras.layers import Dense, Conv2D, DepthwiseConv2D, BatchNormalization

        # Patch all layers that may have quantization_config from newer Keras
        for layer_cls in [Dense, Conv2D, DepthwiseConv2D, BatchNormalization]:
            original_init = layer_cls.__init__
            def make_patched(orig):
                def patched_init(self, *args, **kwargs):
                    kwargs.pop("quantization_config", None)
                    orig(self, *args, **kwargs)
                return patched_init
            layer_cls.__init__ = make_patched(original_init)

        model = tf.keras.models.load_model("best_kidney_model.keras")
        return model, None

    except Exception as e:
        return None, str(e)

# -------------------------
# Preprocess Image
# -------------------------
def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Converts any PIL image to a model-ready (1, 224, 224, 3) float32 array.
    Handles RGB, RGBA, grayscale, and palette modes.
    """
    image = image.convert("RGB")        # fixes RGBA, grayscale, palette
    image = image.resize((224, 224))    # resize AFTER convert (cleaner)
    image = np.array(image, dtype="float32") / 255.0
    return np.expand_dims(image, axis=0)



# -------------------------
# UI
# -------------------------

# ---- STATS ----
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">98.81%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">🫘 Kidney Stone Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a kidney image — the model will predict kidney condition using a custom VRF-Net architecture.</div>', unsafe_allow_html=True)

# Load model
model, load_error = load_model()

if load_error:
    st.error(f"❌ Failed to load model: `{load_error}`")
    st.info("Make sure `best_kidney_model.keras` is in the same directory as this app.")
    st.stop()

# Upload
uploaded_file = st.file_uploader(
    "Choose an kidney image",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG"
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
    except Exception as e:
        st.error(f"❌ Could not read image: {e}")
        st.stop()

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.image(image, caption="Uploaded Kidney Image", use_container_width=True)

    with col2:
        with st.spinner("Running inference..."):
            try:
                processed = preprocess_image(image)
                prediction = model.predict(processed, verbose=0)
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")
                st.stop()

        predicted_index = int(np.argmax(prediction))
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = float(np.max(prediction)) * 100

        # Result
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">Prediction</div>
            <div class="result-value">{predicted_class}</div>
            <div style="margin-top:0.4rem; font-size:0.85rem; color:#888;">
                {CLASS_INFO[predicted_class]}
            </div>
        </div>
        <div class="result-box">
            <div class="result-label">Confidence</div>
            <div class="confidence-value">{confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Probability bars
    st.markdown("#### Class Probabilities")

    for i, cls in enumerate(CLASS_NAMES):
        prob = float(prediction[0][i]) * 100

        color = "#00e5ff" if i == predicted_index else "#aaa"

        # Class name and percentage on the same line
        st.markdown(
            f"""
            <div style="
                display:flex;
                justify-content:space-between;
                font-family:'IBM Plex Mono', monospace;
                font-size:0.85rem;
                color:{color};
                margin-bottom:3px;
            ">
                <span>{cls.upper()}</span>
                <span>{prob:.2f}%</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Progress bar for THIS class
        st.progress(float(prob) / 100)

        
    # Disclaimer
    st.markdown("""
    <div class="disclaimer">
        ⚠️ <strong>Medical Disclaimer:</strong> This tool is for research and educational purposes only.
        It is <strong>not</strong> a substitute for professional medical diagnosis.
        Always consult a qualified healthcare professional for medical decisions.
    </div>
    """, unsafe_allow_html=True)