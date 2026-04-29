import streamlit as st
import cv2

st.title('Machine Learning')
st.write('Ram') 

st.write('SitaRam') 
st.write('Deep Learning')
st.image("img2.jpg")

import cv2 
img2 =cv2.imread("doremon.webp")

height = st.slider("select the Height",100,500)
width = st.slider("select the width",100,500)

img = cv2.resize(img2,(width,height))