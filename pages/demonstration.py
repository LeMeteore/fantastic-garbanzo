import streamlit as st

st.title("this is the app title")
st.header("this is header")
st.subheader("this is the subheader")
st.markdown("this is a *markdown* **text**")
st.caption("this is the caption")
st.code("""
def program():
    return 42
""")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.image("uploads/chat1.jpeg")
st.image("uploads/dog1.jpg")
# st.audio("uploads/Audio.mp3")
# st.video("uploads/video.mp4")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


st.progress(5)
import time
with st.spinner('Wait for it...'):
    time.sleep(10)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

time.sleep(30)
st.balloons()
