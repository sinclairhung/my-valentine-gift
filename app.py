import streamlit as st
import random
import base64

# --- 1. 設定網頁基本資訊 ---
st.set_page_config(page_title="情人節快樂", page_icon="❤️")

# --- 2. 設定背景圖片的函數 (這是網頁專用的魔法) ---
def set_bg_hack(main_bg):
    '''
    這段程式碼會幫你把圖片設為網頁背景
    '''
    ext = 'png' if main_bg.endswith('png') else 'jpg'
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
        }}
        /* 讓文字背景變半透明黑，不然會看不清楚 */
        .stTitle, .stHeader, .stMarkdown {{
            background-color: rgba(255, 255, 255, 0.7); 
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 嘗試讀取背景圖片 (記得圖片要叫 bg.jpg 或 bg.png)
try:
    set_bg_hack('bg.jpg') # 如果你的圖是 png，請把這裡改成 'bg.png'
except:
    st.warning("⚠️ 找不到背景圖，請確認資料夾內有一張名為 bg.jpg 的圖片")

# --- 3. 遊戲邏輯 ---

# 檢查這是第幾次點擊，用來決定按鈕的位置
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

if 'finished' not in st.session_state:
    st.session_state.finished = False

# 標題
st.title("💖 給最特別的妳 💖")
st.write("\n") # 空行
st.write("\n")

# 如果還沒按到「愛」，就顯示問題
if not st.session_state.finished:
    st.header("親愛的老婆，妳愛我嗎？")
    st.write("\n")
    
    # 這裡我們用兩個「欄位」來放按鈕，這樣才可以左右互換
    col1, col2 = st.columns(2)
    
    # 隨機決定哪個欄位放「愛」，哪個放「不愛」
    # 每次點擊「不愛」，click_count 就會增加，按鈕就會換位置
    swap = st.session_state.click_count % 2 != 0
    
    if swap:
        # 這是「不愛」在左邊，「愛」在右邊的情況
        with col1:
            if st.button("不愛 💔", key="no_btn_1"):
                st.session_state.click_count += 1
                st.rerun() # 重新整理網頁，按鈕位置就會變
        with col2:
            if st.button("愛！ ❤️", key="yes_btn_1"):
                st.session_state.finished = True
                st.rerun()
    else:
        # 這是「愛」在左邊，「不愛」在右邊的情況
        with col1:
            if st.button("愛！ ❤️", key="yes_btn_2"):
                st.session_state.finished = True
                st.rerun()
        with col2:
            if st.button("不愛 💔", key="no_btn_2"):
                st.session_state.click_count += 1
                st.rerun() # 重新整理網頁，按鈕位置就會變

# 如果按到了「愛」，顯示結果
else:
    st.balloons() # 放氣球
    st.markdown("### 耶！我就知道妳愛我！ 😘")
    st.markdown("#### 情人節快樂！")
    # 這裡可以加一段感性的話
    st.write("謝謝妳包容我的一切，我們要一直幸福下去喔！")
    
    if st.button("再玩一次"):
        st.session_state.finished = False
        st.session_state.click_count = 0
        st.rerun()