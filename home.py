import streamlit as st

st.write('# Hi! welcome to My App!')

st.write('Nucd to meet you!.')


if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")


option = st.selectbox(
    "좋아하는 동물은?",
    ("강아지", "고양이", "물고기","토끼","코끼리"))

st.write("내가 좋아하는 동물은", option,"입니다.")

st.write(f"내가 좋아하는 동물은 {option} 입니다.")

txt = st.text_area("자신을 소개해보세요.",'''

    ''')

st.write('입력한 내용:',txt)

age = st.slider("나이를 선택하세요", 0, 130, 25)#범위는 0~130,초기 선택은 25
st.write(f"나이는 {age} 입니다.")
