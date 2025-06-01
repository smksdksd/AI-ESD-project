import streamlit as st
from PIL import Image
import random
import os

st.title("🎉 오늘의 MBTI 밈 생성기 🎉")

# 사용자로부터 MBTI 입력 받기
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP, ESTJ 등):").upper()

# MBTI별 밈 사전
mbti_memes = {
    "INFP": ["memes/infp_meme1.jpg", "memes/infp_meme2.jpg"],
    "INFJ": ["memes/infj_meme1.jpg", "memes/infj_meme2.jpg"],
    "INTP": ["memes/intp_meme1.jpg", "memes/intp_meme2.jpg"],
    "INTJ": ["memes/intj_meme1.jpg", "memes/intj_meme2.jpg"],
    "ISFP": ["memes/isfp_meme1.jpg", "memes/isfp_meme2.jpg"],
    "ISFJ": ["memes/isfj_meme1.jpg", "memes/isfj_meme2.jpg"],
    "ISTP": ["memes/istp_meme1.jpg", "memes/istp_meme2.jpg"],
    "ISTJ": ["memes/istj_meme1.jpg", "memes/istj_meme2.jpg"],
    "ENFP": ["memes/enfp_meme1.jpg", "memes/enfp_meme2.jpg"],
    "ENFJ": ["memes/enfj_meme1.jpg", "memes/enfj_meme2.jpg"],
    "ENTP": ["memes/entp_meme1.jpg", "memes/entp_meme2.jpg"],
    "ENTJ": ["memes/entj_meme1.jpg", "memes/entj_meme2.jpg"],
    "ESFP": ["memes/esfp_meme1.jpg", "memes/esfp_meme2.jpg"],
    "ESFJ": ["memes/esfj_meme1.jpg", "memes/esfj_meme2.jpg"],
    "ESTP": ["memes/estp_meme1.jpg", "memes/estp_meme2.jpg"],
    "ESTJ": ["memes/estj_meme1.jpg", "memes/estj_meme2.jpg"],
}

if mbti:
    if mbti in mbti_memes:
        # 이미지 랜덤 선택
        meme_path = random.choice(mbti_memes[mbti])

        # 파일이 실제로 있는지 확인
        if os.path.exists(meme_path):
            st.image(Image.open(meme_path), caption=f"오늘의 {mbti} 밈!", use_column_width=True)
        else:
            st.warning(f"⚠️ {mbti}의 밈 이미지가 존재하지 않아요!\n'`{meme_path}`' 경로를 확인해보세요.")
    else:
        st.warning("⚠️ 유효하지 않은 MBTI 유형이에요. 다시 입력해 주세요!")

st.markdown("---")
st.write("✅ **예시 MBTI 입력**: INFP, ESTJ, ENTP, INTJ 등 (대문자로 입력!)")
