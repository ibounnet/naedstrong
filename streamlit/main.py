import streamlit as st
from bmi import BMI_Calculator
from bmr import BMR_Calculator

# Create instances of BMI_Calculator and BMR_Calculator
bmi_app = BMI_Calculator()
bmr_app = BMR_Calculator()

page = st.session_state.get('page', 1)

if page == 1:
    st.empty()

    st.title("Welcome To FollowCal 🏃‍♀️")

    st.write("BMI คือ ค่าดัชนีที่ใช้ชี้วัดความสมดุลของน้ำหนักตัว เหมาะสำหรับใช้ประเมินผู้ที่มีอายุตั้งแต่ 20 ปีขึ้นไป ประโยชน์ของการวัดค่า BMI เพื่อดูอัตราเสี่ยงต่อการเกิดโรคต่าง ๆ ตรวจสอบภาวะไขมันและความอ้วน ดังนั้นการทำให้ร่างกายอยู่ในเกณฑ์ปกติจึงมีความสำคัญอย่างยิ่งกับผู้ที่ต้องการรักษาสุขภาพในระยะยาว")

    st.markdown("<div style='height: 2px; background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);'></div>", unsafe_allow_html=True)

    st.write("BMR คือ อัตราการความต้องการเผาผลาญของร่างกายในชีวิตประจำวัน หรือจำนวนแคลอรี่ขั้นต่ำที่ต้องการใช้ในชีวิตแต่ละวัน ดังนั้นการคำนวณ BMR จะช่วยให้คุณคำนวณปริมาณแคลอรี่ที่ใช้ต่อวันเพื่อรักษาน้ำหนักปัจจุบันได้")

    st.markdown("<style>.custom-line { border-top: 3px solid #777; }</style>", unsafe_allow_html=True)

    st.balloons()

    st.markdown("<hr class='custom-line'>", unsafe_allow_html=True)

    st.write("Let's calculate your BMI and BMR! 🧮")

    # If BMI button is clicked, set the page to 2 (BMI calculator)
    if st.button('BMI CALCULATE') :
        page = 2
    

    # If BMR button is clicked, set the page to 3 (BMR calculator)
    elif st.button('BMR CACULATE') :
        page = 3
       

elif page == 2:
    st.empty()  # Clear the page
    bmi_app.render_main_page()  # Render the BMI calculator

    if st.button('HOME 🏠'):
        page = 1

elif page == 3:
    st.empty()  # Clear the page
    bmr_app.render_bmr_page()  # Render the BMR calculator

    if st.button('HOME 🏠'):

        page = 1
       


# Save the current page to the session state
st.session_state['page'] = page