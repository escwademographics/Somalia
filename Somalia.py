#import the required libraries 

import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px  
import json
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="اســتـبـيـان المجتمع العربي",
    page_icon= "🇺🇳",
    layout='wide'
)

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)



left_co, cent_co,last_co = st.columns(3)
with last_co:
    st.image("https://i2.wp.com/ummah-futures.net/wp-content/uploads/2019/12/%D8%A7%D9%84%D9%84%D8%AC%D9%86%D8%A9-%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%D9%8A%D8%A9-%D9%84%D8%BA%D8%B1%D8%A8%D9%8A-%D8%A2%D8%B3%D9%8A%D8%A7-1.jpg?w=500&ssl=1")
with left_co:
    st.image("https://www.unescwa.org/sites/default/files/images/flags/Flag_of_Somalia.svg")
st.image("title.PNG")

# Create an empty container
placeholder = st.empty()

actual_email = "somalia"
actual_password = "somalia22"

# Insert a form in the container
with placeholder.form("login"):
    #st.markdown("#### الرجاء ادخال اسم المستخدم")
    st.markdown('<div style="text-align: right; font-size: 28px; font-weight: bold; color: blue;">الرجاء ادخال اسم المستخدم وكلمة المرور</div>', unsafe_allow_html=True)
    email = st.text_input("Username - اسم المستخدم")
    email = email.lower()
    password = st.text_input("Password - كلمة المرور", type="password")
    password = password.lower()
    submit = st.form_submit_button("Login - تسجيل الدخول")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("تم تسجيل الدخول بنجاح")
    leftt_co, centt_co,lastt_co = st.columns([1,1,2])
    with lastt_co :
        st.title('الصومال')
        st.image("SUB HEADER.PNG")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.write("[Population - السكان](https://docs.google.com/spreadsheets/d/1mLozQoVocbRclcX1JljemfTrY5m7wgqt/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col2:
        st.write("[Labor - العمالة](https://docs.google.com/spreadsheets/d/1RlvKf9gUkhr5S9LU5dqXwU-4eftmizbO/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col3:
        st.write("[Poverty - الفقر](https://docs.google.com/spreadsheets/d/1gFCvElIqpfyu9a1PkagtPNaQ1jX49UIu/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col4:
        st.write("[Education - التعليم](https://docs.google.com/spreadsheets/d/1AEyqZrCB_VpHBiffL9zHpH203ciBPfka/edit?usp=sharing&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col5:
        st.write("[Culture - الثقافة](https://docs.google.com/spreadsheets/d/1K2SFVvA_wkMeu-R5oVxtmO7T7WHofpcu/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col6:
        st.write("[Health - الصحة](https://docs.google.com/spreadsheets/d/1gbx0g59toYy8VAb8lE-DptnTXmfSl-JN/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col7:
        st.write("[Housing Conditions - المساكن](https://docs.google.com/spreadsheets/d/1J9895gzwq1m5Q5s9T0lpospxDutKY43_/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")   

    st.title("Questionnaires in English Language are available below:")

    
    coll1, coll2, coll3, coll4, coll5, coll6, coll7 = st.columns(7)
    with coll1:
        st.write("[Population - السكان](https://docs.google.com/spreadsheets/d/1Bwcs5OEtWJ_QO6852aIyoROg7B3pXdkw/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll2:
        st.write("[Labor - العمالة](https://docs.google.com/spreadsheets/d/1eyxUZrNEx6hS7c-YHTbZ-Q_yJG3f9Hl2/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll3:
        st.write("[Poverty - الفقر](https://docs.google.com/spreadsheets/d/12kpkS77CMXH-08N6pp0huwIVZPcauG81/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll4:
        st.write("[Education - التعليم](https://docs.google.com/spreadsheets/d/1pJM7-iPoTyXNiH8C8w8OzaR4NSPS7dGn/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll5:
        st.write("[Culture - الثقافة](https://docs.google.com/spreadsheets/d/1nccUwEdrEhmbEhkLLfuhXVueDxVb5QXQ/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll6:
        st.write("[Health - الصحة](https://docs.google.com/spreadsheets/d/1OnHnvseeDT3mMVPXt4dK7IERRoNAlKte/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll7:
        st.write("[Housing Conditions - المساكن](https://docs.google.com/spreadsheets/d/1v6EccXE9Ha5cf0a7t8vjAlrqPujiFdKq/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")

elif submit and email != actual_email and password != actual_password:
    st.error("هناك خطأ في اسم المستخدم او كلمة المرور، الرجاء المحاولة من جديد")
    
else:
    pass



#edit footer
page_style= """
    <style>
    footer{
        visibility: visible;
        }
    footer:after{
        content: 'Developed by ESCWA Statistics, Information Society and Technology Cluster';
        display:block;
        position:relative;
        color:#1e54e4;
    }
    </style>"""

st.markdown(page_style, unsafe_allow_html=True)
