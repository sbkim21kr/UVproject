import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="MES Dashboard",
    page_icon="🏭",
    layout="wide"
)

# 애플리케이션 제목
st.title("🏭 MES 생산 현황 대시보드")
st.markdown("---")

# 가상 생산 데이터
PRODUCTION_TARGET = 3000
current_production = 2350
achievement_rate = (current_production / PRODUCTION_TARGET) * 100

# 생산 현황 모니터링
st.header("📊 생산 현황 모니터링")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="일일 생산 목표", value=f"{PRODUCTION_TARGET} 개")
with col2:
    st.metric(label="현재 생산량", value=f"{current_production} 개", delta=f"{current_production - 2300} 개")
with col3:
    st.metric(label="달성률", value=f"{achievement_rate:.2f} %", delta=f"{achievement_rate - 75:.2f} %")
st.progress(achievement_rate / 100)
st.markdown("---")
# In tools like Streamlit, delta is used to show how much a value has changed compared to a reference.


# 품질/특이사항 보고 폼
st.header("📝 품질/특이사항 보고")
form_col1, form_col2 = st.columns(2)
with form_col1:
    line_option = st.selectbox("생산 라인", ("1번 라인", "2번 라인", "3번 라인"))
    issue_type = st.selectbox("문제 유형", ("단순 불량", "설비 고장", "원료 부족", "기타"))
with form_col2:
    issue_details = st.text_area("상세 내용 입력", placeholder="문제 상황을 구체적으로 기술하십시오...")

# 🧠 What It Does:

#     It creates three columns with relative widths: 2 units, 1 unit, and 2 units.

#     The underscores _ are placeholders for the left and right columns — you're not using them.

#     center_col is the middle column, which is narrower and used to center content.
# This layout centers a widget (like a button) horizontally on the page. For example:
# This places the button in the middle column, visually centered between the wider left and right columns.

_, center_col, _ = st.columns([2, 1, 2])
with center_col:
    submit_button = st.button("보고서 제출", use_container_width=True)

# 보고서 제출 로직
if submit_button:
    if not issue_details:
        st.warning("상세 내용을 입력해야 합니다.")
    else:
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success(f"[{report_time}] 보고서가 성공적으로 제출되었습니다!")
        st.info(f"**라인:** {line_option}")
        st.info(f"**문제 유형:** {issue_type}")
        st.info(f"**상세 내용:** {issue_details}")
