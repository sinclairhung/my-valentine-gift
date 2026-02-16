import streamlit as st
import random
import base64

# --- 1. 設定網頁基本資訊 ---
st.set_page_config(page_title="情人節快樂", page_icon="❤️", layout="centered")

# --- 2. 設定背景圖片與全域樣式的函數 ---
def set_bg_hack(main_bg):
    ext = 'png' if main_bg.endswith('png') else 'jpg'
    try:
        with open(main_bg, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{ext};base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            .stButton>button {{
                width: 100%;
                background-color: rgba(0, 0, 0, 0.6);
                color: white;
                border: 1px solid #d4af37;
                border-radius: 20px;
                font-size: 18px;
                transition: 0.3s;
            }}
            .stButton>button:hover {{
                background-color: rgba(0, 0, 0, 0.9);
                border-color: #ffd700;
                color: #ffd700;
            }}
            div[data-testid="stVerticalBlock"] button[kind="primary"] {{
                background-color: rgba(200, 50, 50, 0.8) !important;
                border: 1px solid red !important;
            }}
            .css-15zrgzn {{display: none}}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
         st.warning("⚠️ 找不到背景圖，請確認 GitHub 上有上傳 bg.jpg 或 bg.png")

set_bg_hack('bg.jpg')

# --- 3. 遊戲狀態初始化 ---
if 'finished' not in st.session_state:
    st.session_state.finished = False
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

# --- 4. 遊戲主邏輯 ---

# 標題區塊
st.markdown(
    """
    <div style="background-color: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
        <h1 style="color: white; margin:0; font-family: 'Times New Roman', serif;">💖 給最特別的妳 💖</h1>
    </div>
    """, 
    unsafe_allow_html=True
)


if not st.session_state.finished:
    # 問題區塊
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; text-align: center;">
            <h2 style="color: #f0f0f0; margin:0;">親愛的老婆，妳愛我嗎？</h2>
        </div>
        <br>
        """, 
        unsafe_allow_html=True
    )
    
    random_vertical_spacer = random.randint(0, 5)
    for _ in range(random_vertical_spacer):
        st.write("") 

    cols = st.columns([1, 1, 1, 1, 1])
    indices = list(range(5))
    random.shuffle(indices) 
    pos1 = indices.pop()
    pos2 = indices.pop()
    
    if random.random() > 0.5:
        yes_pos, no_pos = pos1, pos2
    else:
        yes_pos, no_pos = pos2, pos1

    with cols[yes_pos]:
        if st.button("愛！ ❤️", key=f"yes_btn_{st.session_state.click_count}", type="primary"):
            st.session_state.finished = True
            st.rerun()

    with cols[no_pos]:
        if st.button("不愛 💔", key=f"no_btn_{st.session_state.click_count}"):
            st.session_state.click_count += 1
            st.rerun()

else:
    # --- 成功後的畫面 (修正版) ---
    st.balloons()
    st.write("")
    
    # 這裡我把所有 HTML 擠在一起，避免因為縮排產生亂碼
    st.markdown(
        """
        <div style="background-color: rgba(20, 20, 20, 0.85); padding: 30px; border-radius: 15px; text-align: center; border: 2px solid #d4af37; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
            <h2 style="color: #d4af37; font-family: 'Times New Roman', serif; margin-bottom: 20px;">✨ 耶！我就知道妳愛我！ ✨</h2>
            <h3 style="color: #f5f5f5; font-weight: normal; margin-bottom: 10px;">情人節快樂！</h3>
            <hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(212, 175, 55, 0.75), rgba(0, 0, 0, 0)); margin: 20px 0;">
            <p style="color: #e0e0e0; font-size: 1.1em; line-height: 1.6; font-family: serif;">
                謝謝妳一直以來的包容與陪伴。<br>
                未來的日子，我們也要一直幸福地走下去喔！❤️
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("")
    st.write("")
    if st.button("再玩一次"):
        st.session_state.finished = False
        st.session_state.click_count = 0
        st.rerun()
