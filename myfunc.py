import streamlit as st

def range_bmi(bmi):
    if bmi >=25:
        st.error("비만입니다.",icon="🚨")
    elif bmi >= 23:
        st.warning("과체중입니다.",icon="⚠️")
    elif bmi >= 18.5:
        st.success("정상입니다.",icon="✅")
        st.balloons()
    else :
        st.warning("저체중입니다.",icon="⚠️")