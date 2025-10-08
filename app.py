# you’re running the script with /bin/python3,
# which bypasses uv and its virtual environment.
# That’s why it can’t find Streamlit, even though you installed it with uv add.

# When you use /bin/python3, you're using the system Python, 
# which doesn’t know about your uv environment or installed packages.
#  uv keeps everything isolated in .venv, so you need to run through 
# uv to access those packages.

import streamlit as st

# 최상위 제목 설정
st.title("Streamlit 애플리케이션")

# 헤더(소제목) 설정
st.header("헤더 컴포넌트")

# 서브헤더 설정
st.subheader("서브헤더 컴포넌트")

# 마크다운 적용
st.markdown("---") # 수평선
st.markdown("## 마크다운 제목 레벨 2")
st.markdown("*기울임꼴*, **굵은 글꼴** 스타일 적용 가능")
st.markdown("- 목록 항목 1\n- 목록 항목 2\n- 목록 항목 3") # 리스트
