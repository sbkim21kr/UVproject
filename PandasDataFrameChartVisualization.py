# you’re running the script with /bin/python3,
# which bypasses uv and its virtual environment.
# That’s why it can’t find Streamlit, even though you installed it with uv add.

# When you use /bin/python3, you're using the system Python, 
# which doesn’t know about your uv environment or installed packages.
#  uv keeps everything isolated in .venv, so you need to run through 
# uv to access those packages.

import streamlit as st
import pandas as pd
import numpy as np

st.title("데이터 시각화")

# Pandas 데이터프레임 생성
data = {
    '첫 번째 컬럼': [1, 2, 3, 4],
    '두 번째 컬럼': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

st.write("Pandas 데이터프레임 표시:")
st.dataframe(df) # 스크롤 가능한 테이블 형식으로 표시

st.write("라인 차트:")
# 랜덤 시계열 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 20행 3열의 랜덤 데이터
    columns=['a', 'b', 'c']
)



st.line_chart(chart_data)

st.write("막대 차트:")
st.bar_chart(chart_data)


st.write("차트에 사용된 실제 데이터:")
st.dataframe(chart_data)
