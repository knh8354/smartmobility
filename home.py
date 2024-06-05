import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import myfunc as mf

st.session_state.id = "김남현"#변수가 초기화 되지 않음
st.write(st.session_state.id,"님 환영합니다.")

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
        mf.range_bmi(bmi)
    st.image('image.jpg', caption='균형있는 식단을 추천합니다.')

if selected=='갭마인더':
    st.title("갭마인더")

    st.write("파일 불러오기")
    data=pd.read_csv('gapminder.csv')
    year=st.slider("select a Year",1952,2007,1952,step=5)
    st.write(f"{year}년도")
    data=data[data['year']==year]
    fig,ax=plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002)
    st.pyplot(fig)



if selected=='국가별 통계':
    st.title("국기별 통계")
    df=pd.read_csv('gapminder.csv')
    country=df["country"].unique()

    options = st.multiselect("나라를 선택하세요",country,["Korea, Rep."])
    
    st.write("You slelcted",options[0])

    fig, ax = plt.subplots()
    for x in options:
        ax.plot(df[df['country']==x]["year"],df[df['country']==x]["gdpPercap"])
    st.pyplot(fig)

    fig1, ax1 = plt.subplots()
    for x in options:
        ax1.plot(range(len(df[df['country']==x]['lifeExp'])),df[df["country"]==x]['lifeExp'],label=x)
    ax1.legend()
    ax1.set_xticks(range(len(df[df['country']==x]['pop'])),df[df["country"]==x]['year'])
    ax1.set_title('Life Expectancy')
    st.pyplot(fig1)