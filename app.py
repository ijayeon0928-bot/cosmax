import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="메모박스", page_icon="🗒️", layout="wide")

# Streamlit 자체 여백을 최대한 없애서 HTML이 화면을 꽉 채우도록 함
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "memobox.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1600, scrolling=True)
