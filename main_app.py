import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはサプーの動画用テストアプリです')


#画像
image = Image.open("./data/S__196018181.jpg")
st.image(image,width=200)