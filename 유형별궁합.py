import streamlit as st

st.title("💞 MBTI 친구 궁합 테스트 💞")

# 사용자 A, B MBTI 입력받기
mbti_a = st.text_input("당신의 MBTI를 입력하세요 (예: INFP, ESTJ 등):").upper()
mbti_b = st.text_input("친구의 MBTI를 입력하세요 (예: INFP, ESTJ 등):").upper()

# MBTI 궁합 메시지 예시 데이터
compatibility_messages = {
    ("INFP", "ESTJ"): "INFP의 따뜻한 감성과 ESTJ의 현실적인 면이 서로를 보완해요!",
    ("ENFP", "INFJ"): "ENFP의 에너지와 INFJ의 깊이가 환상적인 궁합이에요!",
    ("INTJ", "ENFP"): "ENFP의 자유로운 영혼이 INTJ의 계획을 멋지게 흔들어줘요.",
    ("ISTJ", "ESFP"): "ISTJ의 꼼꼼함과 ESFP의 유쾌함이 의외의 시너지를 만들어요!",
    # 모든 조합을 다 작성하기 어렵다면 기본 메시지로!
}

def get_compatibility(mbti_a, mbti_b):
    # A-B, B-A 둘 다 가능하도록
    pair = (mbti_a, mbti_b)
    reverse_pair = (mbti_b, mbti_a)

    if pair in compatibility_messages:
        return compatibility_messages[pair]
    elif reverse_pair in compatibility_messages:
        return compatibility_messages[reverse_pair]
    else:
        return f"{mbti_a}와 {mbti_b}의 궁합은 서로를 알아가는 과정에서 더 특별해질 수 있어요! 🌟"

if mbti_a and mbti_b:
    result = get_compatibility(mbti_a, mbti_b)
    st.success(f"🌟 오늘의 궁합 메시지:\n\n> {result}")

st.markdown("---")
st.write("✅ **예시 MBTI 입력**: INFP, ESTJ, ENFP, INFJ 등 (대문자로 입력!)")
