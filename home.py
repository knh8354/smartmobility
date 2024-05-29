import streamlit as st
import pandas as pd
import matplotlib as plt


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


selected = st.sidebar.selectbox("목차",
    ("체질량 계산기", "갭마인더", "국가별 통계")
)
if selected=='체질량 계산기':
    st.header('체질량 계산기', divider='rainbow')
    st.info("체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.")
    height = st.number_input("신장(cm)",value=160,step=1)
    st.write(f"신장:{height}(cm)")
    weight = st.number_input("체중(kg)",value=60,step=1)
    st.write(f"체중:{weight}(kg)")

    if st.button("bmi 계산"):
        bmi=weight/(height/100)**2
        st.write(f"체질량 지수:{bmi:.2f}")
        range_bmi(bmi)
    st.image('image.jpg', caption='균형있는 식단을 추천합니다.')

if selected=='갭마인더':
    st.title("갭마인더")

    st.write("파일 불러오기")
    data=pd.read_csv('gapminder.csv')
    year=st.slider("select a Year",1952,2007,1952,step=5)
    data=data[data['year']==year]
    #fig,ax=plt.subplots()
    #ax.scatter(data['gdpPercap'],data['lifeExp'])
    #st.pyplot(fig)

    df =  data[["gdpPercap","lifeExp"]]
    st.scatter_chart(df)
    st.write(data)












if selected=='국가별 통계':
    st.title("국기별 통계")