import streamlit as st
import time as t

st.image("C:/Users/STRATAZON/Downloads/kumar/kumar.jpg")

# title
st.title("Welcome my page")

# header
st.header("machine learning")

# sub header
st.subheader("linear regression")

# info details
st.info("This is my first streamlit app")

# warning message
st.warning("come on time, else you will fail")

# error message
st.error("something went wrong")

# success message
st.success("successfully done")

# write 
st.write("Employee name")
st.write("range(50)")
st.write(range(50))

# markdown
st.markdown("markdown")
st.markdown("# markdown")
st.markdown("## markdown")
st.markdown("### markdown")
st.markdown(":moon:")

# text
st.text("hi i am kumar")

# to write caption
st.caption("caption is here")

# to display mathematical expression
st.latex(r''' a+bx^2+c''')


# widgets

# checkbox
st.checkbox('login')

# button
st.button('click me')

#radio
st.radio("Pick your gender", ["male", "female", "other"])

# select box
st.selectbox("pick your course", ["ML", "Cloud", "Cyber Security"])

# multi select
st.multiselect("Choose the department", ["Content", "Sales", "marketing"])

# select slider
st.select_slider("Pick your age", range(1, 21))

# slider
st.slider("Enter your Number", 0, 30)

# number_input
st.number_input("Pick a Nuber", 0, 100)

# text input\
st.text_input("Enter your email address")

# date input
st.date_input("Opening ceremony")

# time input
st.time_input("what the time")

# text area
st.text_area("welcome to the intellipatt website, hello learners..")

# file uploder
st.file_uploader("upload your file")

# color picker
st.color_picker("colour")

# progress
st.progress(75)

# spinner
with st.spinner("just wait"):
    t.sleep(1)

# ballon
st.balloons()

# side bar title
st.sidebar.title("welcome")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("password")
st.sidebar.button("login")
st.sidebar.radio("peofession expert", ["student", "Working"])

# Data visualization
import pandas as pd
import numpy as np
st.title("Bar chart")
data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
st.bar_chart(data)

st.title("Line chart")
st.line_chart(data)

st.title("area chart")
st.area_chart(data)