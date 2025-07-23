import streamlit as st
from PIL import Image
import numpy as np
from zeroscratches import EraseScratches
from streamlit_image_comparison import image_comparison

# Page config
st.set_page_config(page_title="Pixel Restoration", layout="wide", page_icon="🧠")

# --- Inject Animated Sci-Fi Background using Vanta.js ---
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
  overflow: hidden;
}
#vanta {
  width: 100vw;
  height: 100vh;
  position: fixed;
  z-index: -1;
}
</style>
</head>
<body>
<div id="vanta"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@0.5.21/dist/vanta.net.min.js"></script>
<script>
VANTA.NET({
  el: "#vanta",
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  color: 0x00ffff,
  backgroundColor: 0x0f0f0f,
  points: 12.0,
  maxDistance: 22.0,
  spacing: 15.0
})
</script>
</body>
</html>
""", height=0)

# --- Futuristic CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
        background-color: transparent !important;
        color: #00f0ff;
    }

    .main-title {
        font-size: 3rem;
        text-align: center;
        font-weight: bold;
        color: #00f0ff;
        text-shadow: 0 0 10px #00f0ff;
        margin-top: 2rem;
    }

    .upload-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #00f0ff22;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 0 25px #00f0ff33;
        margin: 2rem auto;
    }

    .stButton>button {
        border-radius: 8px;
        background: linear-gradient(90deg, #00f0ff, #ff00ff);
        color: black;
        font-weight: bold;
        padding: 0.6rem 1.5rem;
        border: none;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        box-shadow: 0 0 15px #00f0ff88;
        transform: scale(1.03);
    }

    .footer {
        text-align: center;
        font-size: 12px;
        color: #666;
        margin-top: 4rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="main-title">🧠 Pixel Restoration</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#bbb;">Futuristic AI-Powered Scratch Removal</p>', unsafe_allow_html=True)

# --- Upload ---
with st.container():
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📁 Upload your old, scratched image", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- Main logic ---
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    with st.spinner("🛠️ Activating Neural Repair Module..."):
        eraser = EraseScratches()
        restored_np = eraser.erase(image)
        restored_image = Image.fromarray(restored_np)

    st.markdown("### 🧪 Slide to Compare")
    image_comparison(
        img1=image,
        img2=restored_image,
        label1="Original",
        label2="Restored",
        width=700,
    )

    # Download
    st.markdown("### 📥 Download Restored Image")
    st.download_button(
        label="⬇️ Save to Cyberdeck",
        data=restored_image.convert("RGB").tobytes("jpeg", "RGB"),
        file_name="restored_image.jpg",
        mime="image/jpeg"
    )

# --- Footer ---
st.markdown('<div class="footer">PixelRestoration 2099™ | Built with ❤️ using Streamlit, AI, and future tech ⚡</div>', unsafe_allow_html=True)
