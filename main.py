import streamlit as st
from PIL import Image
import random

st.title("오늘의 MBTI 밈 생성기 🎉")

# 사용자로부터 MBTI 입력 받기
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP, ESTJ 등):").upper()

# MBTI별 밈 사전 (예제: 실제로는 이미지 경로/URL로 대체)
mbti_memes = {
    "INFP": ["memes/infp_meme1.jpg", "memes/infp_meme2.jpg"],
    "ESTJ": ["memes/estj_meme1.jpg", "memes/estj_meme2.jpg"],
    "ENTP": ["memes/entp_meme1.jpg", "memes/entp_meme2.jpg"],
    # 더 많은 MBTI 유형 추가 가능!
}

if mbti:
    if mbti in mbti_memes:
        # MBTI에 따른 밈 리스트에서 랜덤으로 하나 선택
        meme_path = random.choice(mbti_memes[mbti])
        st.image(Image.open(meme_path), caption=f"오늘의 {mbti} 밈!", use_column_width=True)
    else:
        st.warning("죄송하지만 해당 MBTI 유형의 밈이 없어요! 다시 입력해 주세요.")

st.markdown("---")
st.write("🔹 **Tip:** 입력 예시: INFP, ESTJ, ENTP 등 (대문자로 입력!)")
