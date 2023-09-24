# Youtbe reference: https://www.youtube.com/playlist?list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW

import streamlit as st
import pandas as pd
import time as ts
from datetime import time
# from matplotlib import pyplot as plt
import numpy as np

# Hide MainMenu item
st.markdown("""
<style>
.st-emotion-cache-iiif1v.ef3psqc3
{
    visibility: hidden          
}
</style>
""", unsafe_allow_html= True)

# Hide Deploy Button
st.markdown("""
<style>
.st-emotion-cache-1wbqy5l.e17vllj40
{
    visibility: hidden          
}
</style>
""", unsafe_allow_html= True)

# st.title("Hi! i am a streamlit web app!")

# # Hide Footer
# st.markdown("""
# <style>
# .st-emotion-cache-h5rgaw.ea3mdgi1
# {
#     visibility: hidden          
# }
# </style>
# """, unsafe_allow_html= True)

st.title("Hi! i am a streamlit web app!")

# Headers
st.header("Header", divider='rainbow')
st.header("Hi, i am Header")
st.subheader("Hi , i am your subheader")
st.text("Hi, i am text function and programmers use me inplace of paragrah tag")

# Markup
st.header("Markup Language", divider='blue')
st.markdown("## **Hello** *World*")
st.markdown("[Google](http://www.google.com)")

# Latex
st.header("Latex", divider='green')
st.markdown("[Latex](https://katex.org/docs/supported)")
st.latex(r"\begin{pmatrix}a & b \\c & d\end{pmatrix}")

# Json
st.header("Json", divider='orange')
json = {"a": "1,2,3", "b":"4,5,6"}
st.json(json)

# Code
st.header("Code", divider='red')
code= """
print("Hello World)
def fucn():
    return 0
"""
st.code(code, language="python")

# Swiss Army Knife
st.header("Swiss Army Knife", divider='violet')
st.write('Hello, *World!* :sunglasses:')
st.write(pd.DataFrame({'first column': [1, 2, 3, 4],
                       'second column': [10, 20, 30, 40]
                       }))

# Metric
st.header("Metric", divider='red')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
st.metric(label="wind speed", value="120ms⁻¹", delta="1.4ms⁻¹")

# DataFrame
st.header("Dataframe", divider='rainbow')
table = pd.DataFrame({"Column1" : [1,2,3,4],
                      "Column2": [5,6,7,8]
                     })
st.table(table) # Static Table
st.dataframe(table) # User Interaction

# Media Widget
st.header("Media Widget", divider='blue')
st.image("./Media/AI.jpg", caption="This is AI image")
st.audio("./Media/Romansy_melody4arab.com.mp3")
st.video("./Media/Robotplayback.mp4")

# Removing Streamlit Hamburger and Footer
st.header("Removing Streamlit Hamburger and Footer", divider="blue")
st.markdown("[Removing Streamlit Hamburger and Footer](https://www.youtube.com/watch?v=_b6nfGNcTdw&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=7)")

# Basic Interactive Widgets 
st.header("Basic Interactive Widgets", divider="red")

state = st.checkbox("checkbox", value= False,  key='checker')
if state:
    st.write("This checkbox is checked", )
else:
    st.write("Not Checked")

st.write(st.session_state['checker'])

radio_btn = st.radio("in which country do you live?",options=("uk", "us", "lebanon", "canada"))
st.write(radio_btn)

def btn_click():
    print("button clicked!")
btn = st.button("click me", on_click=btn_click)

select = st.selectbox("What is your favorite color?", options=["blue", "red", "yello"])
st.write(select)

multi_select = st.multiselect("What is your favourite cars? Select more than one",
                              options=["Pajero", "Honda", "BMW"])
st.write(multi_select)

# File Uploader Widget
st.header("File uploader Widget", divider='blue')
uploaded_files = st.file_uploader("Please upload a file", 
                                 type=["jpg","png", "mp3", "mp4"],
                                 accept_multiple_files=True)

for uploaded_file in uploaded_files:
    if uploaded_file:
        type = uploaded_file.type.split("/")[0]
        if type == "image":
            st.image(image=uploaded_file)
        if type == "video":
            st.video(uploaded_file)
        if type == "audio":
            st.audio(uploaded_file)

# Some More interactive widgets
st.header("Some more interactive widgets", divider="green")
## Slider
value = st.slider("Select a value", min_value=1, max_value=10,value=4, step=1)
st.write("selected value is: {}".format(value))

#text input
val = st.text_input("Enter you goal in life?", max_chars=60)
val1 = st.text_area("Describe your personality?")
val2 = st.date_input("Enter your expected date to achive you dream?")
val3 = st.time_input("At what time you usuall wake up?")

# Timer App With Progress Bar
st.header("Timer App With Progress Bar", divider='rainbow')

def convert_time_to_sec(value):
    m,s,ms = value.split(":")
    t_s = int(m)*60 + int(s) + int(ms)/1000
    return t_s
time_entered = st.time_input("Set Timer:",value=time(0,0,0))
if str(time_entered) == "00:00:00":
    st.write("you need to set a timer")
else:
    sec = convert_time_to_sec(str(time_entered))
    percentage = sec/100
    bar = st.progress(0)
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i) + "%")
        ts.sleep(percentage)


# Streamlit Forms-I
st.header("Streamlit Forms-I", divider="blue")

st.markdown("<h1 Style= 'text-align: Center;'>User Registration</h1>", unsafe_allow_html= True)

frm1 = st.form("frm1")
frm1.text_input("First Name")
frm1.form_submit_button("Submit")

with st.form("frm2", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        f_name = st.text_input("First Name")
    with col2:
        l_name = st.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm password")

    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    s_status = st.form_submit_button("Submit")
    if s_status:
        if f_name == "" and l_name =="":
            st.warning("Please enter first and last name")
        else:
            st.success("Submitted Successfully")

# Sidebar & Graphs In Streamlit
st.header("Sidebar & Graphs In Streamlit", divider="red" )
st.sidebar.write("This is my first side bar")
opt = st.sidebar.radio("Select any graph", options=["Line", "Bar", "H-Bar"])
if opt == "Line":
    st.write("line option was clicked")
    # fig = plt.figure()
    # # print(plt.style.available)
    # plt.style.use("fivethirtyeight")
    # x = np.linspace(0,10,100)
    # plt.plot(x, np.sin(x))
    # plt.plot(x, np.cos(x))
    # st.write(fig)

